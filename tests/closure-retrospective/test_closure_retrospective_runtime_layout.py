from __future__ import annotations

from pathlib import Path


def test_closure_retrospective_skill_layout() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    skill_dir = repo_root / ".agents" / "skills" / "closure-retrospective"

    assert skill_dir.exists()
    assert (skill_dir / "SKILL.md").exists()
    assert (skill_dir / "agents" / "openai.yaml").exists()
    assert (skill_dir / "references" / "decision-rubric.md").exists()
    assert (skill_dir / "references" / "output-template.md").exists()
    assert not (skill_dir / "tests").exists()


def test_closure_retrospective_docs_are_discoverable() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    docs_dir = repo_root / "docs" / "skills" / "closure-retrospective"
    readme = (repo_root / "README.md").read_text(encoding="utf-8")

    assert (docs_dir / "README.md").exists()
    assert (docs_dir / "README_zh.md").exists()
    assert "closure-retrospective" in readme
