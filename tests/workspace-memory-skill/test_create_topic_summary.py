from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_create_topic_summary_uses_default_topic_path(tmp_path: Path) -> None:
    script = (
        Path(__file__).resolve().parents[2]
        / ".agents"
        / "skills"
        / "workspace-memory-skill"
        / "scripts"
        / "create_topic_summary.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--root",
            str(tmp_path),
            "--topic",
            "architecture",
            "--title",
            "Architecture topic summary",
            "--summary",
            "Tracks active architecture decisions and reusable context.",
            "--source-id",
            "session:2026-03-23:workspace-memory-design",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    summary_path = (
        tmp_path / "docs" / "memory" / "summaries" / "topics" / "architecture.md"
    )

    assert result.returncode == 0, result.stderr
    assert summary_path.exists()
    text = summary_path.read_text(encoding="utf-8")
    assert "memory_type: topic-summary" in text
    assert "topic: 'architecture'" in text
    assert "source_ids:" in text
