#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


INDEX_TEMPLATE = """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: Auto-generated navigation index for the workspace memory tree.
created_at: {today}
updated_at: {today}
generator: init_memory.py
---

# Workspace Memory

## Purpose
This directory stores repo-local project memory for agents and developers.

## Suggested Entry Points
- Current state: `summaries/recent.md`
- Historical context: `summaries/archive.md`
- Durable knowledge: `crystals/`
- Topic context: `summaries/topics/`

## Key Files
- `summaries/recent.md`
- `summaries/archive.md`
- `crystals/`
"""


RECENT_TEMPLATE = """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: Auto-generated view of active recent sessions and pending follow-ups.
created_at: {today}
updated_at: {today}
generator: init_memory.py
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


ARCHIVE_TEMPLATE = """---
id: archive-summary:root
memory_type: archive-summary
title: workspace archive summary
summary: Compressed historical memory for this workspace.
created_at: {today}
updated_at: {today}
source_ids: []
---

# Archived Memory

## Important History
- None yet.

## Reusable Context
- None yet.
"""


def build_files(today: str) -> dict[str, str]:
    return {
        "index.md": INDEX_TEMPLATE.format(today=today),
        "summaries/recent.md": RECENT_TEMPLATE.format(today=today),
        "summaries/archive.md": ARCHIVE_TEMPLATE.format(today=today),
    }


def write_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return f"skip  {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"write {path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize repo-local workspace memory.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument(
        "--memory-dir",
        default="docs/memory",
        help="Memory directory relative to the workspace root.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing seeded files.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    memory_dir = root / args.memory_dir
    today = str(date.today())

    dirs = [
        memory_dir / "sessions",
        memory_dir / "summaries" / "topics",
        memory_dir / "crystals",
    ]
    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"mkdir {directory}")

    for rel_path, content in build_files(today).items():
        print(write_file(memory_dir / rel_path, content, args.force))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
