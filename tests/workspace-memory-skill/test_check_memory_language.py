from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPTS_DIR = (
    Path(__file__).resolve().parents[2]
    / ".agents"
    / "skills"
    / "workspace-memory-skill"
    / "scripts"
)


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_check_memory_language_accepts_configured_chinese_body_with_english_headings(
    tmp_path: Path,
) -> None:
    memory_dir = tmp_path / "docs" / "memory"
    session_path = memory_dir / "sessions" / "2026" / "03" / "2026-03-25-language.md"
    session_path.parent.mkdir(parents=True, exist_ok=True)
    (memory_dir / "config.toml").write_text(
        'content_language = "zh-CN"\n',
        encoding="utf-8",
    )
    session_path.write_text(
        """---
id: 'session:2026-03-25:language'
memory_type: session
title: 'language'
summary: 'summary'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags: []
---

# Session: language

## Goal
\u7edf\u4e00 memory \u6b63\u6587\u8bed\u8a00\u3002

## Key Decisions
- \u4fdd\u7559\u82f1\u6587\u6807\u9898\u3002

## Rationale
- \u907f\u514d\u4fee\u6539\u811a\u672c\u7684 section \u5339\u914d\u903b\u8f91\u3002

## Changes
- \u589e\u52a0\u914d\u7f6e\u6587\u4ef6\u3002

## Open Questions
- \u6682\u65e0\u3002

## Follow-up
- \u8865\u5145\u6821\u9a8c\u811a\u672c\u3002

## Crystallization Candidates
- \u6807\u9898\u56fa\u5b9a\u82f1\u6587\uff0c\u6b63\u6587\u8ddf\u968f\u914d\u7f6e\u3002
""",
        encoding="utf-8",
    )

    script = SCRIPTS_DIR / "check_memory_language.py"
    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
    )

    assert result.returncode == 0, result.stderr


def test_check_memory_language_rejects_translated_section_headings(
    tmp_path: Path,
) -> None:
    memory_dir = tmp_path / "docs" / "memory"
    session_path = memory_dir / "sessions" / "2026" / "03" / "2026-03-25-language.md"
    session_path.parent.mkdir(parents=True, exist_ok=True)
    (memory_dir / "config.toml").write_text(
        'content_language = "zh-CN"\n',
        encoding="utf-8",
    )
    session_path.write_text(
        """---
id: 'session:2026-03-25:language'
memory_type: session
title: 'language'
summary: 'summary'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags: []
---

# Session: language

## \u76ee\u6807
\u7edf\u4e00 memory \u6b63\u6587\u8bed\u8a00\u3002

## Key Decisions
- \u4fdd\u7559\u82f1\u6587\u6807\u9898\u3002
""",
        encoding="utf-8",
    )

    script = SCRIPTS_DIR / "check_memory_language.py"
    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
    )

    assert result.returncode != 0
    assert "Unexpected heading" in result.stdout
