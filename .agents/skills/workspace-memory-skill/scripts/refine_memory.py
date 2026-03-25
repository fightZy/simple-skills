#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from memory_ops import dump_frontmatter, parse_frontmatter, source_ids_from_summary_entries


DEFAULT_RECENT = """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: Auto-generated view of active recent sessions and pending follow-ups.
created_at: 1970-01-01
updated_at: 1970-01-01
generator: refine_memory.py
source_ids: []
---

# Recent Memory

## Active Context
- Current priorities
- Current risks

## Recent Sessions
- None yet.

## Pending Follow-ups
- None yet.
"""


DEFAULT_ARCHIVE = """---
id: archive-summary:root
memory_type: archive-summary
title: workspace archive summary
summary: Compressed historical memory for this workspace.
created_at: 1970-01-01
updated_at: 1970-01-01
source_ids: []
---

# Archived Memory

## Important History
- None yet.

## Reusable Context
- None yet.
"""


def split_section(text: str, heading: str) -> tuple[str, str, str]:
    marker = f"## {heading}\n"
    if marker not in text:
        return text, "", ""
    before, after = text.split(marker, 1)
    next_header = "\n## "
    split_index = after.find(next_header)
    if split_index == -1:
        body = after.strip("\n")
        rest = ""
    else:
        body = after[:split_index].strip("\n")
        rest = after[split_index:]
    return before + marker, body, rest


def parse_bullets(section_body: str) -> list[str]:
    lines = [line.strip() for line in section_body.splitlines() if line.strip()]
    return [line for line in lines if line.startswith("- ") and line != "- None yet."]


def rebuild_bullet_section(entries: list[str], placeholder: str) -> str:
    if not entries:
        return placeholder
    return "\n".join(entries)


def update_section(text: str, heading: str, entries: list[str], placeholder: str) -> str:
    prefix, _body, rest = split_section(text, heading)
    if not prefix:
        return text.rstrip() + f"\n\n## {heading}\n" + rebuild_bullet_section(entries, placeholder) + "\n"
    return (prefix + rebuild_bullet_section(entries, placeholder) + rest).rstrip() + "\n"


def load_text(path: Path, default: str) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(default, encoding="utf-8")
    return default


def to_archive_entry(recent_entry: str) -> str:
    body = recent_entry[2:].strip()
    if "; next step:" in body:
        body = body.split("; next step:", 1)[0].strip()
    return f"- {body}"


def collect_recent_follow_ups(entries: list[str]) -> list[str]:
    follow_ups: list[str] = []
    for entry in entries:
        if "; next step:" not in entry:
            continue
        follow_up = entry.split("; next step:", 1)[1].strip()
        if follow_up:
            follow_ups.append(f"- {follow_up}")
    return follow_ups


def main() -> int:
    parser = argparse.ArgumentParser(description="Compress older recent entries into archive memory.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--keep", type=int, default=5, help="How many recent session entries to keep in recent memory.")
    parser.add_argument(
        "--min-archive",
        type=int,
        default=7,
        help="Only archive when recent session count is at least this value.",
    )
    args = parser.parse_args()

    if args.keep < 1:
        raise SystemExit("--keep must be at least 1")
    if args.min_archive < args.keep:
        raise SystemExit("--min-archive must be greater than or equal to --keep")

    root = Path(args.root).resolve()
    memory_dir = root / args.memory_dir
    recent_path = memory_dir / "summaries" / "recent.md"
    archive_path = memory_dir / "summaries" / "archive.md"

    recent_text = load_text(recent_path, DEFAULT_RECENT)
    archive_text = load_text(archive_path, DEFAULT_ARCHIVE)

    _prefix, recent_body, _rest = split_section(recent_text, "Recent Sessions")
    recent_entries = parse_bullets(recent_body)

    if len(recent_entries) < args.min_archive:
        print(
            f"skip  {recent_path} (recent entries: {len(recent_entries)}, threshold: {args.min_archive})"
        )
        return 0

    keep_entries = recent_entries[: args.keep]
    archive_candidates = recent_entries[args.keep :]
    archive_entries = [to_archive_entry(entry) for entry in archive_candidates]

    recent_text = update_section(recent_text, "Recent Sessions", keep_entries, "- None yet.")
    recent_text = update_section(
        recent_text,
        "Pending Follow-ups",
        collect_recent_follow_ups(keep_entries),
        "- None yet.",
    )
    recent_metadata, recent_body = parse_frontmatter(recent_text)
    recent_metadata["updated_at"] = str(date.today())
    recent_metadata["source_ids"] = source_ids_from_summary_entries(keep_entries)
    recent_text = dump_frontmatter(recent_metadata, recent_body)
    recent_path.write_text(recent_text, encoding="utf-8")
    print(f"update {recent_path}")

    archive_prefix, archive_body, archive_rest = split_section(archive_text, "Important History")
    existing_archive_entries = parse_bullets(archive_body)
    merged_archive_entries = archive_entries + [
        entry for entry in existing_archive_entries if entry not in archive_entries
    ]
    if not archive_prefix:
        archive_text = archive_text.rstrip() + "\n\n## Important History\n" + rebuild_bullet_section(
            merged_archive_entries, "- None yet."
        ) + "\n"
    else:
        archive_text = (
            archive_prefix
            + rebuild_bullet_section(merged_archive_entries, "- None yet.")
            + archive_rest
        ).rstrip() + "\n"
    archive_metadata, archive_body = parse_frontmatter(archive_text)
    archive_metadata["updated_at"] = str(date.today())
    archive_metadata["source_ids"] = source_ids_from_summary_entries(
        merged_archive_entries
    )
    archive_text = dump_frontmatter(archive_metadata, archive_body)
    archive_path.write_text(archive_text, encoding="utf-8")
    print(f"update {archive_path}")

    print(
        f"archived {len(archive_candidates)} entries from {recent_path} into {archive_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
