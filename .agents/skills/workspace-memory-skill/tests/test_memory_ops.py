from __future__ import annotations

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from memory_ops import dump_frontmatter, parse_frontmatter  # noqa: E402


def test_frontmatter_round_trip_preserves_metadata_and_body() -> None:
    text = """---
id: 'crystal:repo-local-markdown-first'
memory_type: crystal
tags:
  - 'memory'
  - 'repo-local'
source_ids:
  - 'session:2026-03-23:workspace-memory-design'
---

# Crystal: Repo-local markdown first

## Statement
- Keep memory in the repository.
"""

    metadata, body = parse_frontmatter(text)

    assert metadata["id"] == "crystal:repo-local-markdown-first"
    assert metadata["memory_type"] == "crystal"
    assert metadata["tags"] == ["memory", "repo-local"]
    assert metadata["source_ids"] == ["session:2026-03-23:workspace-memory-design"]
    assert body.startswith("# Crystal: Repo-local markdown first")

    rebuilt = dump_frontmatter(metadata, body)
    rebuilt_metadata, rebuilt_body = parse_frontmatter(rebuilt)
    assert rebuilt_metadata == metadata
    assert rebuilt_body == body
