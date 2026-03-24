from __future__ import annotations

from pathlib import Path
import sys


sys.path.insert(
    0,
    str(
        Path(__file__).resolve().parents[2]
        / ".agents"
        / "skills"
        / "workspace-memory-skill"
        / "scripts"
    ),
)

from memory_ops import dump_frontmatter, parse_frontmatter, update_section  # noqa: E402


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


def test_update_section_inserts_missing_heading_in_canonical_order() -> None:
    body = """# Crystal: Repo-local markdown first

## Statement
- Keep memory in the repository.

## When To Apply
- When choosing a memory system.

## Provenance
- session:2026-03-23:workspace-memory-design

## Notes
- None yet.
"""

    updated = update_section(
        body,
        "Why It Matters",
        ["Inspectability beats hidden infra."],
        mode="append",
    )

    expected = [
        "## Statement",
        "## Why It Matters",
        "## When To Apply",
        "## Provenance",
        "## Notes",
    ]
    positions = [updated.index(heading) for heading in expected]
    assert positions == sorted(positions)
