from __future__ import annotations

from pathlib import Path


def test_workspace_memory_skill_runtime_directory_excludes_dev_tests() -> None:
    skill_dir = (
        Path(__file__).resolve().parents[2]
        / ".agents"
        / "skills"
        / "workspace-memory-skill"
    )

    assert skill_dir.exists()
    assert not (skill_dir / "tests").exists()
