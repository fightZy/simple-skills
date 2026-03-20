#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


SESSION_TEMPLATE = """---
id: {session_id}
memory_type: session
title: {topic}
summary: {summary}
session_date: {session_date}
created_at: {session_date}
updated_at: {session_date}
tags:{tags_block}
---

# Session: {topic_heading}

## Goal
{goal}

## Key Decisions
{decisions}

## Rationale
{rationale}

## Changes
{changes}

## Open Questions
{open_questions}

## Follow-up
{follow_up}

## Crystallization Candidates
{crystallization}
{optional_sections}"""


RECENT_TEMPLATE = """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: Auto-generated view of active recent sessions and pending follow-ups.
created_at: {today}
updated_at: {today}
generator: record_session.py
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


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "session"


def bulletize(items: list[str], fallback: str = "- None") -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return fallback
    return "\n".join(f"- {item}" for item in cleaned)


def yaml_list(items: list[str]) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return " []"
    return "\n" + "\n".join(f"  - {yaml_scalar(item)}" for item in cleaned)


def yaml_scalar(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def optional_section(title: str, items: list[str]) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return ""
    return f"\n\n## {title}\n" + "\n".join(f"- {item}" for item in cleaned)


def replace_recent_placeholder(text: str, entry: str) -> str:
    marker = "- None yet."
    if marker in text:
        return text.replace(marker, entry, 1)
    return text


def insert_recent_entry(text: str, entry: str) -> str:
    header = "## Recent Sessions\n"
    if header not in text:
        return text.rstrip() + "\n\n## Recent Sessions\n" + entry + "\n"
    before, after = text.split(header, 1)
    next_header = "\n## "
    split_index = after.find(next_header)
    if split_index == -1:
        section_body = after.strip("\n")
        rest = ""
    else:
        section_body = after[:split_index].strip("\n")
        rest = after[split_index:]

    section_lines = [line for line in section_body.splitlines() if line.strip()]
    section_lines.insert(0, entry)
    rebuilt_section = "\n".join(section_lines)
    return (before + header + rebuilt_section + rest).rstrip() + "\n"


def update_pending_follow_ups(text: str, follow_ups: list[str]) -> str:
    if not follow_ups:
        return text

    header = "## Pending Follow-ups\n"
    if header not in text:
        return text.rstrip() + "\n\n## Pending Follow-ups\n" + bulletize(follow_ups) + "\n"

    before, after = text.split(header, 1)
    lines = after.splitlines()
    inserted_lines = [f"- {item.strip()}" for item in follow_ups if item.strip()]
    output = [before + header]
    wrote_new_items = False
    for line in lines:
        if not wrote_new_items:
            for item in inserted_lines:
                output.append(item + "\n")
            wrote_new_items = True
        if line.strip() == "- None yet.":
            continue
        output.append(line + "\n")

    if not wrote_new_items:
        for item in inserted_lines:
            output.append(item + "\n")

    return "".join(output).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Record a workspace memory session.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--date", default=str(date.today()), help="Session date in YYYY-MM-DD format.")
    parser.add_argument("--topic", required=True, help="Short session topic.")
    parser.add_argument("--goal", default="Capture a high-signal session summary.", help="Session goal.")
    parser.add_argument("--tag", action="append", default=[], help="Tag value. Repeat to add multiple items.")
    parser.add_argument("--decision", action="append", default=[], help="Key decision. Repeat to add multiple items.")
    parser.add_argument("--rationale", action="append", default=[], help="Decision rationale. Repeat to add multiple items.")
    parser.add_argument("--change", action="append", default=[], help="Code/doc/process change. Repeat to add multiple items.")
    parser.add_argument("--open-question", action="append", default=[], help="Open question. Repeat to add multiple items.")
    parser.add_argument("--follow-up", action="append", default=[], help="Follow-up item. Repeat to add multiple items.")
    parser.add_argument("--crystal", action="append", default=[], help="Crystallization candidate. Repeat to add multiple items.")
    parser.add_argument("--related-file", action="append", default=[], help="Related file path. Repeat to add multiple items.")
    parser.add_argument("--related-ref", action="append", default=[], help="Related issue/PR/reference. Repeat to add multiple items.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    memory_dir = root / args.memory_dir
    session_date = args.date
    year, month, _day = session_date.split("-", 2)
    slug = slugify(args.topic)
    session_id = f"session:{session_date}:{slug}"
    session_path = memory_dir / "sessions" / year / month / f"{session_date}-{slug}.md"
    session_path.parent.mkdir(parents=True, exist_ok=True)
    summary = args.decision[0].strip() if args.decision else args.goal.strip()
    optional_sections = "".join(
        [
            optional_section("Related Files", args.related_file),
            optional_section("Related References", args.related_ref),
        ]
    )

    session_text = SESSION_TEMPLATE.format(
        session_id=yaml_scalar(session_id),
        topic=yaml_scalar(args.topic),
        topic_heading=args.topic,
        summary=yaml_scalar(summary),
        session_date=session_date,
        tags_block=yaml_list(args.tag),
        goal=args.goal,
        decisions=bulletize(args.decision),
        rationale=bulletize(args.rationale),
        changes=bulletize(args.change),
        open_questions=bulletize(args.open_question),
        follow_up=bulletize(args.follow_up),
        crystallization=bulletize(args.crystal),
        optional_sections=optional_sections,
    )
    session_path.write_text(session_text, encoding="utf-8")
    print(f"write {session_path}")

    recent_path = memory_dir / "summaries" / "recent.md"
    recent_path.parent.mkdir(parents=True, exist_ok=True)
    if recent_path.exists():
        recent_text = recent_path.read_text(encoding="utf-8")
    else:
        recent_text = RECENT_TEMPLATE.format(today=session_date)

    next_step = args.follow_up[0].strip() if args.follow_up else "Review the session file if more detail is needed."
    related_files = ", ".join(args.related_file) if args.related_file else "none"
    entry = f"- {session_date} [{args.topic}]: {summary}; related files: {related_files}; next step: {next_step}"

    if "- None yet." in recent_text:
        updated_recent = replace_recent_placeholder(recent_text, entry)
    else:
        updated_recent = insert_recent_entry(recent_text, entry)
    updated_recent = update_pending_follow_ups(updated_recent, args.follow_up)
    recent_path.write_text(updated_recent, encoding="utf-8")
    print(f"update {recent_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
