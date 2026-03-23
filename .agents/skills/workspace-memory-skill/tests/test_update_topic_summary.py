from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def write_topic_summary(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """---
id: 'topic-summary:workspace-memory'
memory_type: topic-summary
title: 'Workspace memory'
summary: 'Summarize the current state of the workspace-memory system.'
created_at: 2026-03-23
updated_at: 2026-03-23
topic: 'workspace memory'
source_ids:
  - 'session:2026-03-23:workspace-memory-design'
tags: []
---

# Topic Summary: workspace memory

## Current State
- Crystal automation is now script-supported.

## Key Decisions
- Keep memory repo-local.

## Relevant Crystals
- crystal:repo-local-markdown-first

## Source Trail
- session:2026-03-23:workspace-memory-design
""",
        encoding="utf-8",
    )


def test_update_topic_summary_append_deduplicates_entries(tmp_path: Path) -> None:
    topic_path = (
        tmp_path / "docs" / "memory" / "summaries" / "topics" / "workspace-memory.md"
    )
    write_topic_summary(topic_path)
    script = (
        Path(__file__).resolve().parent.parent
        / "scripts"
        / "update_topic_summary.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--path",
            str(topic_path),
            "--append-current-state",
            "Crystal automation is now script-supported.",
            "--append-current-state",
            "Topic summaries are now script-supported.",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    text = topic_path.read_text(encoding="utf-8")
    assert text.count("- Crystal automation is now script-supported.") == 1
    assert "- Topic summaries are now script-supported." in text


def test_update_topic_summary_preserves_created_at(tmp_path: Path) -> None:
    topic_path = (
        tmp_path / "docs" / "memory" / "summaries" / "topics" / "workspace-memory.md"
    )
    write_topic_summary(topic_path)
    script = (
        Path(__file__).resolve().parent.parent
        / "scripts"
        / "update_topic_summary.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--path",
            str(topic_path),
            "--summary",
            "Updated topic summary.",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    text = topic_path.read_text(encoding="utf-8")
    assert "created_at: '2026-03-23'" in text
    assert "summary: 'Updated topic summary.'" in text
