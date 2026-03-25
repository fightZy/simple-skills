#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from memory_ops import parse_frontmatter


@dataclass(frozen=True)
class MemoryRecord:
    path: Path
    rel_path: str
    metadata: dict[str, object]

    @property
    def memory_id(self) -> str:
        return str(self.metadata.get("id", ""))

    @property
    def memory_type(self) -> str:
        return str(self.metadata.get("memory_type", ""))

    @property
    def title(self) -> str:
        return str(self.metadata.get("title", ""))

    @property
    def summary(self) -> str:
        return str(self.metadata.get("summary", ""))

    @property
    def source_ids(self) -> list[str]:
        raw = self.metadata.get("source_ids", [])
        if isinstance(raw, list):
            return [str(item) for item in raw]
        if raw:
            return [str(raw)]
        return []


def main() -> int:
    parser = argparse.ArgumentParser(description="Query workspace memory using layered retrieval.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument(
        "--query-type",
        choices=["current-state", "experience", "norms"],
        default="current-state",
        help="Retrieval mode when --id is not used.",
    )
    parser.add_argument("--topic", help="Substring filter for topic, title, summary, id, or path.")
    parser.add_argument("--tag", action="append", default=[], help="Tag filter. Repeat to add multiple items.")
    parser.add_argument("--id", help="Exact memory id lookup.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of non-base results to print.")
    args = parser.parse_args()

    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    root = Path(args.root).resolve()
    memory_dir = root / args.memory_dir
    records = load_records(root, memory_dir)

    if args.id:
        record = find_by_id(records, args.id)
        if record is None:
            raise SystemExit(f"Memory id not found: {args.id}")
        print(format_record(record, "exact id match"))
        return 0

    results = query_records(records, args.query_type, args.topic, args.tag, args.limit)
    if not results:
        print("No matches.")
        return 0

    print(f"Query type: {args.query_type}")
    for record, reason in results:
        print()
        print(format_record(record, reason))
    return 0


def load_records(root: Path, memory_dir: Path) -> list[MemoryRecord]:
    candidates: list[Path] = []
    for relative in [
        Path("index.md"),
        Path("summaries") / "recent.md",
        Path("summaries") / "archive.md",
    ]:
        path = memory_dir / relative
        if path.exists():
            candidates.append(path)

    for pattern in [
        "summaries/topics/*.md",
        "crystals/*.md",
        "sessions/**/*.md",
    ]:
        candidates.extend(sorted(memory_dir.glob(pattern)))

    records: list[MemoryRecord] = []
    for path in candidates:
        metadata, _body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not metadata:
            continue
        records.append(
            MemoryRecord(
                path=path,
                rel_path=path.relative_to(root).as_posix(),
                metadata=metadata,
            )
        )
    return records


def find_by_id(records: list[MemoryRecord], memory_id: str) -> MemoryRecord | None:
    for record in records:
        if record.memory_id == memory_id:
            return record
    return None


def query_records(
    records: list[MemoryRecord],
    query_type: str,
    topic_filter: str | None,
    tag_filters: list[str],
    limit: int,
) -> list[tuple[MemoryRecord, str]]:
    filtered_topics = match_records(records, "topic-summary", topic_filter, tag_filters)
    filtered_crystals = match_records(records, "crystal", topic_filter, tag_filters)
    filtered_sessions = match_records(records, "session", topic_filter, tag_filters)

    base_results: list[tuple[MemoryRecord, str]] = []
    if query_type == "current-state":
        index_record = find_by_id(records, "generated-index:workspace-memory")
        recent_record = find_by_id(records, "generated-summary:recent")
        if index_record is not None:
            base_results.append((index_record, "default workspace-memory entry point"))
        if recent_record is not None:
            base_results.append((recent_record, "rolling summary of active context"))

        if filtered_topics:
            extras = [(record, "topic summary matched the current-state filters") for record in filtered_topics[:limit]]
        elif has_explicit_filters(topic_filter, tag_filters):
            extras = [(record, "session match used because no higher-level file matched") for record in filtered_sessions[:limit]]
        else:
            extras = []
        return dedupe_results(base_results + extras)

    if query_type == "experience":
        recent_record = find_by_id(records, "generated-summary:recent")
        if recent_record is not None:
            base_results.append((recent_record, "recent work summary for experience queries"))
        evidence_ids = session_evidence_ids(filtered_sessions)
        extras = (
            ranked_derived_results(
                records,
                "topic-summary",
                topic_filter,
                tag_filters,
                evidence_ids,
                "experience",
            )
            + ranked_derived_results(
                records,
                "crystal",
                topic_filter,
                tag_filters,
                evidence_ids,
                "experience",
            )
            + [(record, "session matched the experience filters") for record in filtered_sessions]
        )
        return dedupe_results(base_results + extras[:limit])

    evidence_ids = session_evidence_ids(filtered_sessions)
    extras = (
        ranked_derived_results(
            records,
            "crystal",
            topic_filter,
            tag_filters,
            evidence_ids,
            "norms",
        )
        + ranked_derived_results(
            records,
            "topic-summary",
            topic_filter,
            tag_filters,
            evidence_ids,
            "norms",
        )
        + [(record, "session matched the norms filters") for record in filtered_sessions]
    )
    return dedupe_results(extras[:limit])


def match_records(
    records: list[MemoryRecord],
    memory_type: str,
    topic_filter: str | None,
    tag_filters: list[str],
) -> list[MemoryRecord]:
    matches: list[MemoryRecord] = []
    for record in records:
        if record.memory_type != memory_type:
            continue
        if not matches_topic(record, topic_filter):
            continue
        if not matches_tags(record, tag_filters):
            continue
        matches.append(record)
    return matches


def ranked_derived_results(
    records: list[MemoryRecord],
    memory_type: str,
    topic_filter: str | None,
    tag_filters: list[str],
    evidence_ids: set[str],
    query_label: str,
) -> list[tuple[MemoryRecord, str]]:
    ranked: list[tuple[tuple[int, int, str], MemoryRecord, str]] = []
    for record in records:
        if record.memory_type != memory_type:
            continue
        if not matches_tags(record, tag_filters):
            continue
        direct_match = matches_topic(record, topic_filter)
        overlap = lineage_overlap(record, evidence_ids)
        if not direct_match and overlap == 0:
            continue
        ranked.append(
            (
                (1 if overlap > 0 else 0, 1 if direct_match else 0, record.title.lower()),
                record,
                derived_reason(memory_type, query_label, direct_match, overlap),
            )
        )
    ranked.sort(reverse=True)
    return [(record, reason) for _score, record, reason in ranked]


def matches_topic(record: MemoryRecord, topic_filter: str | None) -> bool:
    if not topic_filter:
        return True
    needle = topic_filter.strip().lower()
    haystacks = [
        record.memory_id,
        record.title,
        record.summary,
        record.rel_path,
        str(record.metadata.get("topic", "")),
    ]
    return any(needle in value.lower() for value in haystacks if value)


def matches_tags(record: MemoryRecord, tag_filters: list[str]) -> bool:
    if not tag_filters:
        return True
    metadata_tags = record.metadata.get("tags", [])
    if isinstance(metadata_tags, list):
        existing = [str(item).lower() for item in metadata_tags]
    elif metadata_tags:
        existing = [str(metadata_tags).lower()]
    else:
        existing = []
    for tag in tag_filters:
        if tag.strip().lower() not in existing:
            return False
    return True


def session_evidence_ids(matched_sessions: list[MemoryRecord]) -> set[str]:
    return {record.memory_id for record in matched_sessions}


def lineage_overlap(record: MemoryRecord, evidence_ids: set[str]) -> int:
    return len(set(record.source_ids) & evidence_ids)


def derived_reason(
    memory_type: str, query_label: str, direct_match: bool, overlap: int
) -> str:
    label = "topic summary" if memory_type == "topic-summary" else "crystal"
    if overlap > 0 and direct_match:
        return f"{label} matched the {query_label} filters and lineage overlap"
    if overlap > 0:
        return f"{label} matched via lineage overlap"
    return f"{label} matched the {query_label} filters"


def has_explicit_filters(topic_filter: str | None, tag_filters: list[str]) -> bool:
    return bool((topic_filter and topic_filter.strip()) or tag_filters)


def dedupe_results(results: list[tuple[MemoryRecord, str]]) -> list[tuple[MemoryRecord, str]]:
    seen: set[str] = set()
    deduped: list[tuple[MemoryRecord, str]] = []
    for record, reason in results:
        if record.memory_id in seen:
            continue
        seen.add(record.memory_id)
        deduped.append((record, reason))
    return deduped


def format_record(record: MemoryRecord, reason: str) -> str:
    return "\n".join(
        [
            f"- {record.memory_type} {record.memory_id}",
            f"  title: {record.title}",
            f"  path: {record.rel_path}",
            f"  reason: {reason}",
            f"  summary: {record.summary}",
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
