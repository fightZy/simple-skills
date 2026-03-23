#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from memory_ops import bullet_list, resolve_path, slugify, today_iso, write_text, yaml_list, yaml_scalar


TEMPLATE = """---
id: {memory_id}
memory_type: topic-summary
title: {title}
summary: {summary}
created_at: {today}
updated_at: {today}
topic: {topic}
source_ids:{source_ids}
tags:{tags}
---

# Topic Summary: {topic_heading}

## Current State
{current_state}

## Key Decisions
{key_decisions}

## Relevant Crystals
{relevant_crystals}

## Source Trail
{source_trail}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a workspace-memory topic summary.")
    parser.add_argument("--root", required=True, help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--path", help="Explicit topic-summary file path.")
    parser.add_argument("--topic", required=True, help="Topic name.")
    parser.add_argument("--title", required=True, help="Topic-summary title.")
    parser.add_argument("--summary", required=True, help="One-line summary.")
    parser.add_argument("--source-id", action="append", default=[], help="Source session or summary id. Repeat to add multiple items.")
    parser.add_argument("--tag", action="append", default=[], help="Tag value. Repeat to add multiple items.")
    parser.add_argument("--current-state", action="append", default=[], help="Current-state bullet. Repeat to add multiple items.")
    parser.add_argument("--key-decision", action="append", default=[], help="Key-decision bullet. Repeat to add multiple items.")
    parser.add_argument("--relevant-crystal", action="append", default=[], help="Relevant crystal id or path. Repeat to add multiple items.")
    parser.add_argument("--source-trail", action="append", default=[], help="Source trail bullet. Repeat to add multiple items.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing target file.")
    args = parser.parse_args()

    if not args.source_id:
        raise SystemExit("At least one --source-id is required")

    root = Path(args.root).resolve()
    slug = slugify(args.topic)
    if args.path:
        target = resolve_path(root, args.path)
    else:
        target = root / args.memory_dir / "summaries" / "topics" / f"{slug}.md"

    content = TEMPLATE.format(
        memory_id=yaml_scalar(f"topic-summary:{slug}"),
        title=yaml_scalar(args.title),
        summary=yaml_scalar(args.summary),
        today=today_iso(),
        topic=yaml_scalar(args.topic),
        source_ids=yaml_list(args.source_id),
        tags=yaml_list(args.tag),
        topic_heading=args.topic,
        current_state=bullet_list(args.current_state),
        key_decisions=bullet_list(args.key_decision),
        relevant_crystals=bullet_list(args.relevant_crystal),
        source_trail=bullet_list(args.source_trail or args.source_id),
    )
    write_text(target, content, force=args.force)
    print(f"write {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
