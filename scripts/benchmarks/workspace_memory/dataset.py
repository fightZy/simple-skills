from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BenchmarkQuery:
    query_type: str = "current-state"
    topic: str | None = None
    tags: list[str] | tuple[str, ...] = ()
    memory_id: str | None = None
    limit: int = 5


@dataclass(frozen=True)
class MemoryFile:
    path: str
    text: str


@dataclass(frozen=True)
class BenchmarkCase:
    case_id: str
    query: BenchmarkQuery
    memory_files: list[MemoryFile] | tuple[MemoryFile, ...]
    expected_candidate_ids: list[str] | tuple[str, ...]
    expected_top_id: str | None = None
    expected_layers: list[str] | tuple[str, ...] = ()
    bucket: str = "uncategorized"
    forbidden_candidate_ids: list[str] | tuple[str, ...] = ()
    gold_answer: str | None = None
    qa_enabled: bool = False


def load_case_file(path: Path) -> BenchmarkCase:
    payload = json.loads(path.read_text(encoding="utf-8"))
    query_payload = payload.get("query", {})
    raw_tags = query_payload.get("tags")
    if raw_tags is None:
        raw_tags = query_payload.get("tag", [])
    if isinstance(raw_tags, str):
        normalized_tags = [raw_tags]
    else:
        normalized_tags = list(raw_tags)
    memory_files = [
        MemoryFile(path=item["path"], text=item["text"])
        for item in payload.get("memory_files", [])
    ]
    return BenchmarkCase(
        case_id=payload["case_id"],
        query=BenchmarkQuery(
            query_type=query_payload.get("query_type", "current-state"),
            topic=query_payload.get("topic"),
            tags=normalized_tags,
            memory_id=query_payload.get("memory_id") or query_payload.get("id"),
            limit=int(query_payload.get("limit", 5)),
        ),
        memory_files=memory_files,
        expected_candidate_ids=list(payload.get("expected_candidate_ids", [])),
        expected_top_id=payload.get("expected_top_id"),
        expected_layers=list(payload.get("expected_layers", [])),
        bucket=str(payload.get("bucket", "uncategorized")),
        forbidden_candidate_ids=list(payload.get("forbidden_candidate_ids", [])),
        gold_answer=payload.get("gold_answer"),
        qa_enabled=bool(payload.get("qa_enabled", False)),
    )


def load_case_directory(path: Path) -> list[BenchmarkCase]:
    return [load_case_file(case_path) for case_path in sorted(path.glob("*.json"))]
