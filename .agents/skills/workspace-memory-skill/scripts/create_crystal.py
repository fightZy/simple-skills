#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from memory_ops import bullet_list, slugify, today_iso, write_text, yaml_list, yaml_scalar


TEMPLATE = """---
id: {memory_id}
memory_type: crystal
title: {title}
summary: {summary}
created_at: {today}
updated_at: {today}
knowledge_type: {knowledge_type}
source_ids:{source_ids}
tags:{tags}
applies_to:{applies_to}
---

# Crystal: {heading}

## Statement
{statement}

## Why It Matters
{why_it_matters}

## When To Apply
{when_to_apply}

## Provenance
{provenance}

## Notes
{notes}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a workspace-memory crystal.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--path", help="Explicit crystal file path.")
    parser.add_argument("--title", required=True, help="Crystal title.")
    parser.add_argument("--summary", required=True, help="One-line summary.")
    parser.add_argument(
        "--knowledge-type",
        required=True,
        choices=["rule", "decision", "pattern", "insight"],
        help="Crystal knowledge type.",
    )
    parser.add_argument("--source-id", action="append", default=[], help="Source session or summary id. Repeat to add multiple items.")
    parser.add_argument("--tag", action="append", default=[], help="Tag value. Repeat to add multiple items.")
    parser.add_argument("--applies-to", action="append", default=[], help="Path or glob where the crystal applies.")
    parser.add_argument("--statement", action="append", default=[], help="Statement bullet. Repeat to add multiple items.")
    parser.add_argument("--why-it-matters", action="append", default=[], help="Why it matters bullet. Repeat to add multiple items.")
    parser.add_argument("--when-to-apply", action="append", default=[], help="When to apply bullet. Repeat to add multiple items.")
    parser.add_argument("--note", action="append", default=[], help="Note bullet. Repeat to add multiple items.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing target file.")
    args = parser.parse_args()

    if not args.source_id:
        raise SystemExit("At least one --source-id is required")

    root = Path(args.root).resolve()
    slug = slugify(args.title)
    if args.path:
        target = Path(args.path)
    else:
        target = root / args.memory_dir / "crystals" / f"crystal-{slug}.md"

    content = TEMPLATE.format(
        memory_id=yaml_scalar(f"crystal:{slug}"),
        title=yaml_scalar(args.title),
        summary=yaml_scalar(args.summary),
        today=today_iso(),
        knowledge_type=args.knowledge_type,
        source_ids=yaml_list(args.source_id),
        tags=yaml_list(args.tag),
        applies_to=yaml_list(args.applies_to),
        heading=args.title,
        statement=bullet_list(args.statement),
        why_it_matters=bullet_list(args.why_it_matters),
        when_to_apply=bullet_list(args.when_to_apply),
        provenance=bullet_list(args.source_id),
        notes=bullet_list(args.note),
    )
    write_text(target, content, force=args.force)
    print(f"write {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
