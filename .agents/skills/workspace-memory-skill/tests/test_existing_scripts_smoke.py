from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_record_session_still_updates_recent_summary(tmp_path: Path) -> None:
    script = SCRIPTS_DIR / "record_session.py"

    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--topic",
        "workspace-memory-maintenance",
        "--goal",
        "Add maintenance scripts for crystals and topic summaries.",
        "--decision",
        "Use a shared helper module for metadata and section updates.",
        "--follow-up",
        "Add topic summary update coverage.",
        "--related-file",
        ".agents/skills/workspace-memory-skill/scripts/memory_ops.py",
    )

    recent_path = tmp_path / "docs" / "memory" / "summaries" / "recent.md"

    assert result.returncode == 0, result.stderr
    assert recent_path.exists()
    text = recent_path.read_text(encoding="utf-8")
    assert "workspace-memory-maintenance" in text
    assert "Add topic summary update coverage." in text


def test_refine_memory_still_archives_old_entries(tmp_path: Path) -> None:
    summary_dir = tmp_path / "docs" / "memory" / "summaries"
    summary_dir.mkdir(parents=True, exist_ok=True)
    recent_path = summary_dir / "recent.md"
    recent_path.write_text(
        """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: Auto-generated view of active recent sessions and pending follow-ups.
created_at: 2026-03-23
updated_at: 2026-03-23
generator: record_session.py
---

# Recent Memory

## Active Context
- Current priorities
- Current risks

## Recent Sessions
- 2026-03-23 [a]: one; related files: none; next step: keep a
- 2026-03-22 [b]: two; related files: none; next step: keep b
- 2026-03-21 [c]: three; related files: none; next step: archive c

## Pending Follow-ups
- keep a
- keep b
- archive c
""",
        encoding="utf-8",
    )

    script = SCRIPTS_DIR / "refine_memory.py"
    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--keep",
        "2",
        "--min-archive",
        "3",
    )

    archive_path = summary_dir / "archive.md"

    assert result.returncode == 0, result.stderr
    assert archive_path.exists()
    recent_text = recent_path.read_text(encoding="utf-8")
    archive_text = archive_path.read_text(encoding="utf-8")
    assert "[c]" not in recent_text
    assert "archive c" not in recent_text
    assert "[a]" in recent_text
    assert "[b]" in recent_text
    assert "[c]" in archive_text
