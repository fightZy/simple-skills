from __future__ import annotations

from .dataset import BenchmarkCase, BenchmarkQuery


def convert_locomo_record(record: dict[str, object]) -> BenchmarkCase:
    return BenchmarkCase(
        case_id=str(record["sample_id"]),
        query=BenchmarkQuery(
            query_type=str(record.get("query_type", "experience")),
            topic=str(record.get("topic", "")) or None,
            limit=int(record.get("limit", 5)),
        ),
        memory_files=[],
        expected_candidate_ids=[str(item) for item in record.get("evidence_ids", [])],
        gold_answer=str(record.get("answer", "")) or None,
        qa_enabled=True,
    )
