from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from scripts.benchmarks.workspace_memory.dataset import load_case_directory, load_case_file  # type: ignore[import-not-found]  # noqa: E402
from scripts.benchmarks.workspace_memory.locomo_adapter import convert_locomo_record  # type: ignore[import-not-found]  # noqa: E402
from scripts.benchmarks.workspace_memory.qa_adapter import run_qa_case  # type: ignore[import-not-found]  # noqa: E402
from scripts.benchmarks.workspace_memory.runner import run_case, run_suite  # type: ignore[import-not-found]  # noqa: E402
from scripts.benchmarks.workspace_memory.scoring import score_retrieval  # type: ignore[import-not-found]  # noqa: E402


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def memory_file(path: str, text: str) -> dict[str, str]:
    return {"path": path, "text": text}


def test_load_case_file_reads_query_and_gold_fields(tmp_path: Path) -> None:
    case_path = tmp_path / "current_state.json"
    write_json(
        case_path,
        {
            "case_id": "current-state-basic",
            "query": {
                "query_type": "current-state",
                "topic": "workspace",
                "limit": 3,
            },
            "memory_files": [
                memory_file(
                    "docs/memory/index.md",
                    """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: entry point
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Workspace Memory
""",
                )
            ],
            "expected_candidate_ids": ["generated-index:workspace-memory"],
            "expected_top_id": "generated-index:workspace-memory",
            "expected_layers": ["generated-index"],
            "bucket": "current-state",
            "forbidden_candidate_ids": ["session:2026-03-27:do-not-return"],
            "gold_answer": "The workspace memory index is the entry point.",
        },
    )

    case = load_case_file(case_path)

    assert case.case_id == "current-state-basic"
    assert case.query.query_type == "current-state"
    assert case.query.topic == "workspace"
    assert case.expected_candidate_ids == ["generated-index:workspace-memory"]
    assert case.expected_top_id == "generated-index:workspace-memory"
    assert case.expected_layers == ["generated-index"]
    assert case.bucket == "current-state"
    assert case.forbidden_candidate_ids == ["session:2026-03-27:do-not-return"]
    assert case.gold_answer == "The workspace memory index is the entry point."


def test_score_retrieval_computes_recall_and_mrr() -> None:
    metrics = score_retrieval(
        expected_candidate_ids=["topic-summary:workspace-memory"],
        actual_candidate_ids=[
            "generated-summary:recent",
            "topic-summary:workspace-memory",
            "session:2026-03-27:workspace-memory-benchmark",
        ],
        actual_layers=["generated-summary", "topic-summary", "session"],
        expected_layers=["topic-summary"],
    )

    assert metrics["recall_at_1"] == 0.0
    assert metrics["recall_at_3"] == 1.0
    assert metrics["mrr"] == 0.5
    assert metrics["top_hit"] is False
    assert metrics["layer_hit"] is True


def test_score_retrieval_checks_expected_top_id_after_base_results() -> None:
    metrics = score_retrieval(
        expected_candidate_ids=["topic-summary:gold"],
        actual_candidate_ids=[
            "generated-summary:recent",
            "topic-summary:gold",
            "topic-summary:noise",
        ],
        actual_layers=["generated-summary", "topic-summary", "topic-summary"],
        expected_layers=["topic-summary"],
        expected_top_id="topic-summary:gold",
    )

    assert metrics["expected_top_hit"] is True

    metrics = score_retrieval(
        expected_candidate_ids=["topic-summary:gold"],
        actual_candidate_ids=[
            "generated-summary:recent",
            "topic-summary:noise",
            "topic-summary:gold",
        ],
        actual_layers=["generated-summary", "topic-summary", "topic-summary"],
        expected_layers=["topic-summary"],
        expected_top_id="topic-summary:gold",
    )

    assert metrics["expected_top_hit"] is False


def test_benchmark_runner_executes_query_cli_and_reports_metrics(tmp_path: Path) -> None:
    case_path = tmp_path / "experience.json"
    write_json(
        case_path,
        {
            "case_id": "experience-lineage",
            "query": {
                "query_type": "experience",
                "topic": "feedback",
                "limit": 5,
            },
            "memory_files": [
                memory_file(
                    "docs/memory/index.md",
                    """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: entry point
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Workspace Memory
""",
                ),
                memory_file(
                    "docs/memory/summaries/recent.md",
                    """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: active context
created_at: 2026-03-27
updated_at: 2026-03-27
source_ids:
  - 'session:2026-03-27:ranking-feedback'
---

# Recent Memory
""",
                ),
                memory_file(
                    "docs/memory/summaries/topics/workspace-memory.md",
                    """---
id: 'topic-summary:workspace-memory'
memory_type: topic-summary
title: Workspace memory status
summary: Retrieval should continue to improve.
created_at: 2026-03-27
updated_at: 2026-03-27
topic: workspace memory
source_ids:
  - 'session:2026-03-27:ranking-feedback'
tags:
  - 'workspace-memory'
---

# Topic Summary
""",
                ),
                memory_file(
                    "docs/memory/sessions/2026/03/2026-03-27-ranking-feedback.md",
                    """---
id: 'session:2026-03-27:ranking-feedback'
memory_type: session
title: ranking-feedback
summary: Need a better ordering signal for derived files.
session_date: 2026-03-27
created_at: 2026-03-27
updated_at: 2026-03-27
tags:
  - 'workspace-memory'
  - 'feedback'
---

# Session
""",
                ),
            ],
            "expected_candidate_ids": ["topic-summary:workspace-memory"],
            "expected_top_id": "topic-summary:workspace-memory",
            "expected_layers": ["topic-summary"],
        },
    )

    result = run_case(load_case_file(case_path))

    assert result["case_id"] == "experience-lineage"
    assert result["status"] == "passed"
    assert result["retrieved_ids"][0] == "generated-summary:recent"
    assert "topic-summary:workspace-memory" in result["retrieved_ids"]
    assert result["metrics"]["recall_at_3"] == 1.0
    assert result["metrics"]["layer_hit"] is True


def test_benchmark_runner_fails_when_expected_top_id_is_not_first_relevant_result(
    tmp_path: Path,
) -> None:
    query_script = tmp_path / "fake_query.py"
    query_script.write_text(
        """from __future__ import annotations

print("Query type: experience")
print()
print("- generated-summary generated-summary:recent")
print("  title: recent memory summary")
print("  path: docs/memory/summaries/recent.md")
print("  reason: recent work summary for experience queries")
print("  summary: active context")
print()
print("- topic-summary topic-summary:noise")
print("  title: rollback hygiene")
print("  path: docs/memory/summaries/topics/rollback-hygiene.md")
print("  reason: topic summary matched the experience filters")
print("  summary: noisy direct match")
print()
print("- topic-summary topic-summary:gold")
print("  title: workspace memory retrieval status")
print("  path: docs/memory/summaries/topics/workspace-memory-retrieval.md")
print("  reason: topic summary matched via lineage overlap")
print("  summary: correct result")
""",
        encoding="utf-8",
    )

    case_path = tmp_path / "top_id_case.json"
    write_json(
        case_path,
        {
            "case_id": "expected-top-id-enforced",
            "query": {"query_type": "experience", "topic": "rollback", "limit": 5},
            "memory_files": [],
            "expected_candidate_ids": ["topic-summary:gold"],
            "expected_top_id": "topic-summary:gold",
            "expected_layers": ["topic-summary"],
            "bucket": "ranking-contract",
        },
    )
    case = load_case_file(case_path)

    result = run_case(case, query_script=query_script)

    assert result["status"] == "failed"
    assert result["metrics"]["expected_top_hit"] is False


def test_run_qa_case_skips_when_model_config_missing() -> None:
    qa_result = run_qa_case(
        case_gold_answer="Expected answer.",
        question="What changed?",
        retrieved_context=["topic summary"],
        adapter=None,
        model_config=None,
    )

    assert qa_result["status"] == "skipped"
    assert qa_result["reason"] == "model configuration missing"


def test_run_qa_case_uses_adapter_when_enabled() -> None:
    class StubAdapter:
        def answer(
            self,
            *,
            question: str,
            retrieved_context: list[str],
            model_config: dict[str, str],
        ) -> dict[str, object]:
            return {
                "answer": f"{question} :: {retrieved_context[0]} :: {model_config['model']}",
                "latency_ms": 12,
            }

    qa_result = run_qa_case(
        case_gold_answer="What changed? :: topic summary :: test-model",
        question="What changed?",
        retrieved_context=["topic summary"],
        adapter=StubAdapter(),
        model_config={"model": "test-model"},
    )

    assert qa_result["status"] == "answered"
    assert qa_result["is_correct"] is True
    assert qa_result["latency_ms"] == 12


def test_run_suite_summarizes_multiple_cases(tmp_path: Path) -> None:
    fixtures_dir = tmp_path / "fixtures"
    write_json(
        fixtures_dir / "case_a.json",
        {
            "case_id": "current-state-basic",
            "query": {"query_type": "current-state", "topic": "workspace"},
            "memory_files": [
                memory_file(
                    "docs/memory/index.md",
                    """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: entry point
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Workspace Memory
""",
                ),
                memory_file(
                    "docs/memory/summaries/recent.md",
                    """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: active context
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Recent Memory
""",
                ),
            ],
            "expected_candidate_ids": ["generated-index:workspace-memory"],
            "expected_layers": ["generated-index"],
            "bucket": "current-state",
        },
    )
    write_json(
        fixtures_dir / "case_b.json",
        {
            "case_id": "negative-empty",
            "query": {"query_type": "experience", "topic": "nosuchtoken"},
            "memory_files": [],
            "expected_candidate_ids": [],
            "expected_layers": [],
            "bucket": "negative",
        },
    )

    summary = run_suite(load_case_directory(fixtures_dir))

    assert summary["total_cases"] == 2
    assert summary["passed_cases"] >= 1
    assert len(summary["results"]) == 2
    assert summary["bucket_summary"]["current-state"]["total_cases"] == 1
    assert summary["bucket_summary"]["negative"]["total_cases"] == 1


def test_benchmark_runner_reports_trimmed_strong_candidates_when_limit_hides_expected_type(
    tmp_path: Path,
) -> None:
    query_script = tmp_path / "fake_query.py"
    query_script.write_text(
        """from __future__ import annotations

import sys


limit = 5
argv = sys.argv[1:]
for index, token in enumerate(argv):
    if token == "--limit":
        limit = int(argv[index + 1])
        break

print("Query type: experience")
print()
print("- generated-summary generated-summary:recent")
print("  title: recent memory summary")
print("  path: docs/memory/summaries/recent.md")
print("  reason: recent work summary for experience queries")
print("  summary: active context")
print()
print("- topic-summary topic-summary:feedback-cleanup")
print("  title: feedback cleanup")
print("  path: docs/memory/summaries/topics/feedback-cleanup.md")
print("  reason: topic summary matched the experience filters")
print("  summary: noisy direct match")
if limit > 1:
    print()
    print("- crystal crystal:derived-promotion-needs-lineage")
    print("  title: derived promotion needs lineage")
    print("  path: docs/memory/crystals/derived-promotion-needs-lineage.md")
    print("  reason: crystal matched via lineage overlap")
    print("  summary: correct result hidden by the limit")
""",
        encoding="utf-8",
    )

    case_path = tmp_path / "trimmed_case.json"
    write_json(
        case_path,
        {
            "case_id": "lineage-cutoff-diagnostic",
            "query": {"query_type": "experience", "topic": "feedback", "limit": 1},
            "memory_files": [],
            "expected_candidate_ids": ["crystal:derived-promotion-needs-lineage"],
            "expected_top_id": "crystal:derived-promotion-needs-lineage",
            "expected_layers": ["crystal"],
            "bucket": "lineage-cutoff",
        },
    )

    result = run_case(load_case_file(case_path), query_script=query_script)

    assert result["status"] == "failed"
    assert result["diagnostics"]["trimmed_strong_candidate_ids"] == [
        "crystal:derived-promotion-needs-lineage"
    ]
    assert result["diagnostics"]["trimmed_strong_candidate_types"] == ["crystal"]


def test_run_suite_bucket_summary_includes_diagnostic_hit_counts(tmp_path: Path) -> None:
    query_script = tmp_path / "fake_query.py"
    query_script.write_text(
        """from __future__ import annotations

import sys


query_type = "current-state"
topic = None
limit = 5
argv = sys.argv[1:]
for index, token in enumerate(argv):
    if token == "--query-type":
        query_type = argv[index + 1]
    elif token == "--topic":
        topic = argv[index + 1]
    elif token == "--limit":
        limit = int(argv[index + 1])

print(f"Query type: {query_type}")
print()
if topic == "forbidden":
    print("- generated-index generated-index:workspace-memory")
    print("  title: workspace memory index")
    print("  path: docs/memory/index.md")
    print("  reason: default workspace-memory entry point")
    print("  summary: entry point")
    print()
    print("- topic-summary topic-summary:forbidden")
    print("  title: forbidden topic")
    print("  path: docs/memory/summaries/topics/forbidden.md")
    print("  reason: topic summary matched the current-state filters")
    print("  summary: should not be returned")
elif topic == "cutoff":
    print("- generated-summary generated-summary:recent")
    print("  title: recent memory summary")
    print("  path: docs/memory/summaries/recent.md")
    print("  reason: recent work summary for experience queries")
    print("  summary: active context")
    print()
    print("- topic-summary topic-summary:noise")
    print("  title: noise")
    print("  path: docs/memory/summaries/topics/noise.md")
    print("  reason: topic summary matched the experience filters")
    print("  summary: noisy direct match")
    if limit > 1:
        print()
        print("- crystal crystal:gold")
        print("  title: gold crystal")
        print("  path: docs/memory/crystals/gold.md")
        print("  reason: crystal matched via lineage overlap")
        print("  summary: strong candidate cut off by the limit")
else:
    print("- generated-summary generated-summary:recent")
    print("  title: recent memory summary")
    print("  path: docs/memory/summaries/recent.md")
    print("  reason: recent work summary for experience queries")
    print("  summary: active context")
    print()
    print("- topic-summary topic-summary:noise")
    print("  title: rollback hygiene")
    print("  path: docs/memory/summaries/topics/rollback-hygiene.md")
    print("  reason: topic summary matched the experience filters")
    print("  summary: noisy direct match")
    print()
    print("- topic-summary topic-summary:gold")
    print("  title: workspace memory retrieval status")
    print("  path: docs/memory/summaries/topics/workspace-memory-retrieval.md")
    print("  reason: topic summary matched via lineage overlap")
    print("  summary: correct result")
""",
        encoding="utf-8",
    )

    fixtures_dir = tmp_path / "fixtures"
    write_json(
        fixtures_dir / "expected_top.json",
        {
            "case_id": "expected-top-id-enforced",
            "query": {"query_type": "experience", "topic": "rollback", "limit": 5},
            "memory_files": [],
            "expected_candidate_ids": ["topic-summary:gold"],
            "expected_top_id": "topic-summary:gold",
            "expected_layers": ["topic-summary"],
            "bucket": "diagnostics",
        },
    )
    write_json(
        fixtures_dir / "forbidden.json",
        {
            "case_id": "forbidden-hit",
            "query": {"query_type": "current-state", "topic": "forbidden", "limit": 5},
            "memory_files": [],
            "expected_candidate_ids": ["generated-index:workspace-memory"],
            "expected_top_id": "generated-index:workspace-memory",
            "expected_layers": ["generated-index"],
            "bucket": "diagnostics",
            "forbidden_candidate_ids": ["topic-summary:forbidden"],
        },
    )
    write_json(
        fixtures_dir / "trimmed.json",
        {
            "case_id": "trimmed-strong-type",
            "query": {"query_type": "experience", "topic": "cutoff", "limit": 1},
            "memory_files": [],
            "expected_candidate_ids": ["crystal:gold"],
            "expected_top_id": "crystal:gold",
            "expected_layers": ["crystal"],
            "bucket": "diagnostics",
        },
    )

    summary = run_suite(load_case_directory(fixtures_dir), query_script=query_script)

    bucket = summary["bucket_summary"]["diagnostics"]
    assert bucket["expected_top_hit_cases"] == 1
    assert bucket["expected_top_miss_cases"] == 2
    assert bucket["expected_top_miss_case_ids"] == [
        "expected-top-id-enforced",
        "trimmed-strong-type",
    ]
    assert bucket["forbidden_hit_cases"] == 1
    assert bucket["forbidden_hit_case_ids"] == ["forbidden-hit"]
    assert bucket["trimmed_strong_candidate_types"] == {"crystal": 1}
    assert bucket["trimmed_strong_candidate_type_case_ids"] == {
        "crystal": ["trimmed-strong-type"]
    }


def test_benchmark_runner_fails_when_forbidden_candidate_is_returned(tmp_path: Path) -> None:
    case_path = tmp_path / "forbidden.json"
    write_json(
        case_path,
        {
            "case_id": "current-state-forbidden-topic-summary",
            "query": {
                "query_type": "current-state",
                "topic": "workspace",
                "limit": 5,
            },
            "memory_files": [
                memory_file(
                    "docs/memory/index.md",
                    """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: entry point
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Workspace Memory
""",
                ),
                memory_file(
                    "docs/memory/summaries/recent.md",
                    """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: active context
created_at: 2026-03-27
updated_at: 2026-03-27
---

# Recent Memory
""",
                ),
                memory_file(
                    "docs/memory/summaries/topics/workspace-memory.md",
                    """---
id: topic-summary:workspace-memory
memory_type: topic-summary
title: Workspace memory status
summary: topic summary should appear
created_at: 2026-03-27
updated_at: 2026-03-27
topic: workspace memory
---

# Topic Summary
""",
                ),
            ],
            "expected_candidate_ids": ["generated-index:workspace-memory"],
            "expected_layers": ["generated-index"],
            "bucket": "forbidden",
            "forbidden_candidate_ids": ["topic-summary:workspace-memory"],
        },
    )

    result = run_case(load_case_file(case_path))

    assert result["status"] == "failed"
    assert result["metrics"]["forbidden_hit"] is True


def test_locomo_adapter_converts_record_to_internal_case_schema() -> None:
    case = convert_locomo_record(
        {
            "sample_id": "locomo-001",
            "question": "What did the team decide about summaries?",
            "answer": "They decided to prefer derived summaries before sessions.",
            "query_type": "experience",
            "topic": "summaries",
            "evidence_ids": ["topic-summary:workspace-memory"],
        }
    )

    assert case.case_id == "locomo-001"
    assert case.query.query_type == "experience"
    assert case.query.topic == "summaries"
    assert case.expected_candidate_ids == ["topic-summary:workspace-memory"]
    assert case.gold_answer == "They decided to prefer derived summaries before sessions."


def test_load_case_directory_reads_repo_owned_fixture_files() -> None:
    fixture_dir = (
        ROOT_DIR / "tests" / "workspace-memory-skill" / "benchmark_fixtures"
    )
    cases = load_case_directory(fixture_dir)

    assert len(cases) == 10
    assert {case.case_id for case in cases} == {
        "current-state-layered-overview",
        "current-state-scoped-topic-summary",
        "current-state-session-fallback-when-topic-summary-missing",
        "exact-id-single-record",
        "experience-limit-prefers-lineage-crystal",
        "experience-lineage-beats-direct-keyword-noise",
        "experience-lineage-promotion",
        "experience-sparse-negative",
        "norms-requires-all-tags-not-any-tag",
        "norms-prefers-crystal",
    }


def test_run_suite_passes_repo_owned_fixture_files() -> None:
    fixture_dir = (
        ROOT_DIR / "tests" / "workspace-memory-skill" / "benchmark_fixtures"
    )

    summary = run_suite(load_case_directory(fixture_dir))

    assert summary["total_cases"] == 10
    assert summary["failed_cases"] == 0
    assert summary["error_cases"] == 0
    assert set(summary["bucket_summary"]) == {
        "current-state",
        "current-state-scoped",
        "current-state-fallback",
        "exact-id",
        "lineage-cutoff",
        "lineage",
        "lineage-disambiguation",
        "negative",
        "norms-ordering",
        "norms-tag-filter",
    }
