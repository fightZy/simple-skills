from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_create_crystal_writes_expected_file(tmp_path: Path) -> None:
    script = (
        Path(__file__).resolve().parent.parent / "scripts" / "create_crystal.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--root",
            str(tmp_path),
            "--title",
            "Repo-local markdown first",
            "--summary",
            "Prefer repo-local Markdown memory over external systems.",
            "--knowledge-type",
            "rule",
            "--source-id",
            "session:2026-03-23:workspace-memory-design",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    crystal_path = (
        tmp_path
        / "docs"
        / "memory"
        / "crystals"
        / "crystal-repo-local-markdown-first.md"
    )

    assert result.returncode == 0, result.stderr
    assert crystal_path.exists()

    text = crystal_path.read_text(encoding="utf-8")
    assert "memory_type: crystal" in text
    assert "knowledge_type: rule" in text
    assert "source_ids:" in text
