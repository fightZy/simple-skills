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


def test_create_crystal_requires_root_argument(tmp_path: Path) -> None:
    script = (
        Path(__file__).resolve().parent.parent / "scripts" / "create_crystal.py"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(script),
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
        cwd=tmp_path,
    )

    assert result.returncode != 0
    assert "--root" in result.stderr or "--root" in result.stdout


def test_create_crystal_resolves_relative_path_from_root(tmp_path: Path) -> None:
    script = (
        Path(__file__).resolve().parent.parent / "scripts" / "create_crystal.py"
    )
    runner = tmp_path / "runner"
    runner.mkdir()

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--root",
            str(tmp_path),
            "--path",
            "docs/memory/crystals/custom-crystal.md",
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
        cwd=runner,
    )

    assert result.returncode == 0, result.stderr
    assert (tmp_path / "docs" / "memory" / "crystals" / "custom-crystal.md").exists()
    assert not (runner / "docs" / "memory" / "crystals" / "custom-crystal.md").exists()


def test_create_crystal_deduplicates_repeated_list_inputs(tmp_path: Path) -> None:
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
            "--source-id",
            "session:2026-03-23:workspace-memory-design",
            "--tag",
            "memory",
            "--tag",
            "memory",
            "--applies-to",
            "docs/memory/**",
            "--applies-to",
            "docs/memory/**",
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
    text = crystal_path.read_text(encoding="utf-8")
    assert text.count("session:2026-03-23:workspace-memory-design") == 2
    assert text.count("'memory'") == 1
    assert text.count("'docs/memory/**'") == 1
