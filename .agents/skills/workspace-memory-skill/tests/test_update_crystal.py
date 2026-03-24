from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def write_crystal(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """---
id: 'crystal:repo-local-markdown-first'
memory_type: crystal
title: 'Repo-local markdown first'
summary: 'Prefer repo-local Markdown memory over external systems.'
created_at: 2026-03-23
updated_at: 2026-03-23
knowledge_type: rule
source_ids:
  - 'session:2026-03-23:workspace-memory-design'
tags: []
applies_to: []
---

# Crystal: Repo-local markdown first

## Statement
- Keep memory in the repository.

## Why It Matters
- Inspectability beats hidden infra.

## When To Apply
- When choosing a memory system.

## Provenance
- session:2026-03-23:workspace-memory-design

## Notes
- None yet.
""",
        encoding="utf-8",
    )


def test_update_crystal_append_statement_keeps_existing_content(tmp_path: Path) -> None:
    crystal_path = (
        tmp_path
        / "docs"
        / "memory"
        / "crystals"
        / "crystal-repo-local-markdown-first.md"
    )
    write_crystal(crystal_path)
    script = (
        Path(__file__).resolve().parent.parent / "scripts" / "update_crystal.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--path",
            str(crystal_path),
            "--append-statement",
            "Prefer typed memory files for durable knowledge.",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    text = crystal_path.read_text(encoding="utf-8")
    assert "- Keep memory in the repository." in text
    assert "- Prefer typed memory files for durable knowledge." in text


def test_update_crystal_rejects_memory_type_mismatch(tmp_path: Path) -> None:
    crystal_path = tmp_path / "docs" / "memory" / "crystals" / "bad-crystal.md"
    write_crystal(crystal_path)
    text = crystal_path.read_text(encoding="utf-8").replace(
        "memory_type: crystal", "memory_type: session"
    )
    crystal_path.write_text(text, encoding="utf-8")
    script = (
        Path(__file__).resolve().parent.parent / "scripts" / "update_crystal.py"
    )

    result = subprocess.run(
        [sys.executable, str(script), "--path", str(crystal_path), "--summary", "Updated"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "memory_type" in result.stderr or "memory_type" in result.stdout


def test_update_crystal_updates_metadata_lists_and_sections(tmp_path: Path) -> None:
    crystal_path = tmp_path / "docs" / "memory" / "crystals" / "crystal-repo-local-markdown-first.md"
    write_crystal(crystal_path)
    script = Path(__file__).resolve().parent.parent / "scripts" / "update_crystal.py"

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--path",
            str(crystal_path),
            "--add-tag",
            "memory",
            "--add-tag",
            "memory",
            "--add-source-id",
            "session:2026-03-24:crystal-maintenance",
            "--add-applies-to",
            "docs/memory/**",
            "--replace-why-it-matters",
            "Make durable guidance easier to retrieve.",
            "--append-note",
            "Keep updates section-scoped.",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    text = crystal_path.read_text(encoding="utf-8")
    assert text.count("'memory'") == 1
    assert "session:2026-03-24:crystal-maintenance" in text
    assert "'docs/memory/**'" in text
    assert "- Make durable guidance easier to retrieve." in text
    assert "- Keep updates section-scoped." in text


def test_update_crystal_rejects_missing_required_metadata(tmp_path: Path) -> None:
    crystal_path = tmp_path / "docs" / "memory" / "crystals" / "invalid-crystal.md"
    write_crystal(crystal_path)
    text = crystal_path.read_text(encoding="utf-8").replace(
        "source_ids:\n  - 'session:2026-03-23:workspace-memory-design'",
        "source_ids: []",
    )
    crystal_path.write_text(text, encoding="utf-8")
    script = Path(__file__).resolve().parent.parent / "scripts" / "update_crystal.py"

    result = subprocess.run(
        [sys.executable, str(script), "--path", str(crystal_path), "--summary", "Updated"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "source_ids" in result.stderr or "source_ids" in result.stdout
