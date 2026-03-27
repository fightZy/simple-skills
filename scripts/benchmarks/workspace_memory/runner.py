from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from .dataset import BenchmarkCase, load_case_directory
from .scoring import score_retrieval


ROOT_DIR = Path(__file__).resolve().parents[3]
QUERY_SCRIPT = (
    ROOT_DIR
    / ".agents"
    / "skills"
    / "workspace-memory-skill"
    / "scripts"
    / "query_memory.py"
)


def parse_query_output(stdout: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for line in stdout.splitlines():
        if not line.startswith("- "):
            continue
        _prefix, memory_type, memory_id = line.split(" ", 2)
        results.append({"memory_type": memory_type, "memory_id": memory_id})
    return results


def build_query_command(
    case: BenchmarkCase,
    *,
    query_script: Path,
    workspace_root: Path,
    limit_override: int | None = None,
) -> list[str]:
    command = [sys.executable, str(query_script), "--root", str(workspace_root)]
    if case.query.memory_id:
        command.extend(["--id", case.query.memory_id])
        return command

    command.extend(["--query-type", case.query.query_type])
    if case.query.topic:
        command.extend(["--topic", case.query.topic])
    for tag in case.query.tags:
        command.extend(["--tag", tag])
    limit = case.query.limit if limit_override is None else limit_override
    command.extend(["--limit", str(limit)])
    return command


def execute_case_query(
    case: BenchmarkCase,
    *,
    query_script: Path,
    workspace_root: Path,
    limit_override: int | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        build_query_command(
            case,
            query_script=query_script,
            workspace_root=workspace_root,
            limit_override=limit_override,
        ),
        capture_output=True,
        text=True,
        check=False,
    )


def collect_case_diagnostics(
    *,
    case: BenchmarkCase,
    query_script: Path,
    workspace_root: Path,
    parsed_results: list[dict[str, str]],
) -> dict[str, object]:
    diagnostics: dict[str, object] = {
        "trimmed_strong_candidate_ids": [],
        "trimmed_strong_candidate_types": [],
    }
    if case.query.memory_id:
        return diagnostics

    expanded_limit = max(
        case.query.limit + 5,
        len(case.memory_files),
        len(case.expected_candidate_ids) + len(case.forbidden_candidate_ids) + 5,
    )
    if expanded_limit <= case.query.limit:
        return diagnostics

    expanded = execute_case_query(
        case,
        query_script=query_script,
        workspace_root=workspace_root,
        limit_override=expanded_limit,
    )
    if expanded.returncode != 0:
        diagnostics["expanded_limit_error"] = expanded.stderr
        return diagnostics

    expanded_results = parse_query_output(expanded.stdout)
    strong_candidate_ids = set(case.expected_candidate_ids)
    if case.expected_top_id:
        strong_candidate_ids.add(case.expected_top_id)
    if not strong_candidate_ids:
        return diagnostics

    retrieved_ids = {item["memory_id"] for item in parsed_results}
    trimmed_results = [
        item
        for item in expanded_results
        if item["memory_id"] in strong_candidate_ids and item["memory_id"] not in retrieved_ids
    ]
    diagnostics["trimmed_strong_candidate_ids"] = [
        item["memory_id"] for item in trimmed_results
    ]
    diagnostics["trimmed_strong_candidate_types"] = sorted(
        {item["memory_type"] for item in trimmed_results}
    )
    return diagnostics


def run_case(case: BenchmarkCase, query_script: Path = QUERY_SCRIPT) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="workspace-memory-benchmark-") as temp_dir:
        workspace_root = Path(temp_dir)
        for memory_file in case.memory_files:
            target = workspace_root / memory_file.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(memory_file.text, encoding="utf-8")

        completed = execute_case_query(
            case,
            query_script=query_script,
            workspace_root=workspace_root,
        )

        if completed.returncode != 0:
            return {
                "case_id": case.case_id,
                "status": "error",
                "stderr": completed.stderr,
                "stdout": completed.stdout,
                "returncode": completed.returncode,
            }

        parsed = parse_query_output(completed.stdout)
        retrieved_ids = [item["memory_id"] for item in parsed]
        retrieved_layers = [item["memory_type"] for item in parsed]
        diagnostics = collect_case_diagnostics(
            case=case,
            query_script=query_script,
            workspace_root=workspace_root,
            parsed_results=parsed,
        )
        metrics = score_retrieval(
            expected_candidate_ids=case.expected_candidate_ids,
            actual_candidate_ids=retrieved_ids,
            actual_layers=retrieved_layers,
            expected_layers=case.expected_layers,
            expected_top_id=case.expected_top_id,
            forbidden_candidate_ids=case.forbidden_candidate_ids,
        )
        passed = (
            not metrics["false_positive"]
            and not metrics["forbidden_hit"]
            and bool(metrics["expected_top_hit"])
            and (
                metrics["recall_at_5"] == 1.0
                or (not case.expected_candidate_ids and not retrieved_ids)
            )
        )
        return {
            "case_id": case.case_id,
            "bucket": case.bucket,
            "status": "passed" if passed else "failed",
            "retrieved_ids": retrieved_ids,
            "retrieved_layers": retrieved_layers,
            "metrics": metrics,
            "diagnostics": diagnostics,
            "stdout": completed.stdout,
        }


def run_suite(
    cases: list[BenchmarkCase],
    query_script: Path = QUERY_SCRIPT,
) -> dict[str, object]:
    results = [run_case(case, query_script=query_script) for case in cases]
    passed_cases = sum(1 for result in results if result["status"] == "passed")
    failed_cases = sum(1 for result in results if result["status"] == "failed")
    error_cases = sum(1 for result in results if result["status"] == "error")
    bucket_summary: dict[str, dict[str, object]] = {}
    for case, result in zip(cases, results):
        bucket = case.bucket
        bucket_entry = bucket_summary.setdefault(
            bucket,
            {
                "total_cases": 0,
                "passed_cases": 0,
                "failed_cases": 0,
                "error_cases": 0,
                "failed_case_ids": [],
                "expected_top_hit_cases": 0,
                "expected_top_miss_cases": 0,
                "expected_top_miss_case_ids": [],
                "forbidden_hit_cases": 0,
                "forbidden_hit_case_ids": [],
                "trimmed_strong_candidate_types": {},
                "trimmed_strong_candidate_type_case_ids": {},
            },
        )
        bucket_entry["total_cases"] = int(bucket_entry["total_cases"]) + 1
        if result["status"] != "error":
            metrics = result["metrics"]
            if metrics["expected_top_hit"]:
                bucket_entry["expected_top_hit_cases"] = (
                    int(bucket_entry["expected_top_hit_cases"]) + 1
                )
            else:
                bucket_entry["expected_top_miss_cases"] = (
                    int(bucket_entry["expected_top_miss_cases"]) + 1
                )
                expected_top_miss_case_ids = list(bucket_entry["expected_top_miss_case_ids"])
                expected_top_miss_case_ids.append(result["case_id"])
                bucket_entry["expected_top_miss_case_ids"] = expected_top_miss_case_ids
            if metrics["forbidden_hit"]:
                bucket_entry["forbidden_hit_cases"] = (
                    int(bucket_entry["forbidden_hit_cases"]) + 1
                )
                forbidden_hit_case_ids = list(bucket_entry["forbidden_hit_case_ids"])
                forbidden_hit_case_ids.append(result["case_id"])
                bucket_entry["forbidden_hit_case_ids"] = forbidden_hit_case_ids

            diagnostics = result.get("diagnostics", {})
            trimmed_type_counts = dict(bucket_entry["trimmed_strong_candidate_types"])
            trimmed_type_case_ids = dict(
                bucket_entry["trimmed_strong_candidate_type_case_ids"]
            )
            for memory_type in diagnostics.get("trimmed_strong_candidate_types", []):
                trimmed_type_counts[memory_type] = trimmed_type_counts.get(memory_type, 0) + 1
                case_ids = list(trimmed_type_case_ids.get(memory_type, []))
                case_ids.append(result["case_id"])
                trimmed_type_case_ids[memory_type] = case_ids
            bucket_entry["trimmed_strong_candidate_types"] = trimmed_type_counts
            bucket_entry["trimmed_strong_candidate_type_case_ids"] = trimmed_type_case_ids
        if result["status"] == "passed":
            bucket_entry["passed_cases"] = int(bucket_entry["passed_cases"]) + 1
        elif result["status"] == "failed":
            bucket_entry["failed_cases"] = int(bucket_entry["failed_cases"]) + 1
            failed_case_ids = list(bucket_entry["failed_case_ids"])
            failed_case_ids.append(result["case_id"])
            bucket_entry["failed_case_ids"] = failed_case_ids
        else:
            bucket_entry["error_cases"] = int(bucket_entry["error_cases"]) + 1
    return {
        "total_cases": len(results),
        "passed_cases": passed_cases,
        "failed_cases": failed_cases,
        "error_cases": error_cases,
        "bucket_summary": bucket_summary,
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Run workspace-memory benchmark cases.")
    parser.add_argument("case_dir", help="Directory containing benchmark case JSON files.")
    parser.add_argument(
        "--query-script",
        default=str(QUERY_SCRIPT),
        help="Path to the query_memory.py script under test.",
    )
    args = parser.parse_args(argv)

    cases = load_case_directory(Path(args.case_dir))
    summary = run_suite(cases, query_script=Path(args.query_script))
    print(json.dumps(summary, indent=2))
    return 0 if summary["failed_cases"] == 0 and summary["error_cases"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
