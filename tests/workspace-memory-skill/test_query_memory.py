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


def write_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def seed_memory_tree(root: Path) -> None:
    memory_dir = root / "docs" / "memory"
    write_file(
        memory_dir / "index.md",
        """---
id: generated-index:workspace-memory
memory_type: generated-index
title: workspace memory index
summary: Auto-generated navigation index for the workspace memory tree.
created_at: 2026-03-25
updated_at: 2026-03-25
generator: init_memory.py
---

# Workspace Memory
""",
    )
    write_file(
        memory_dir / "summaries" / "recent.md",
        """---
id: generated-summary:recent
memory_type: generated-summary
title: recent memory summary
summary: Auto-generated view of active recent sessions and pending follow-ups.
created_at: 2026-03-25
updated_at: 2026-03-25
generator: record_session.py
source_ids:
  - 'session:2026-03-25:ranking-feedback'
tags:
  - 'workspace-memory'
---

# Recent Memory

## Recent Sessions
- 2026-03-25 [ranking feedback]: Promote derived files using source lineage.
""",
    )
    write_file(
        memory_dir / "summaries" / "topics" / "workspace-memory.md",
        """---
id: 'topic-summary:workspace-memory'
memory_type: topic-summary
title: 'Workspace memory status'
summary: 'Write paths are scripted; retrieval should continue to improve.'
created_at: 2026-03-25
updated_at: 2026-03-25
topic: 'workspace memory'
source_ids:
  - 'session:2026-03-25:ranking-feedback'
tags:
  - 'workspace-memory'
---

# Topic Summary: workspace memory
""",
    )
    write_file(
        memory_dir / "crystals" / "crystal-workspace-memory-updates-stay-schema-scoped.md",
        """---
id: 'crystal:workspace-memory-updates-stay-schema-scoped'
memory_type: crystal
title: 'Workspace memory updates stay schema-scoped'
summary: 'Maintenance should update only known metadata fields and canonical sections.'
created_at: 2026-03-25
updated_at: 2026-03-25
knowledge_type: pattern
source_ids:
  - 'session:2026-03-25:ranking-feedback'
tags:
  - 'workspace-memory'
---

# Crystal: Workspace memory updates stay schema-scoped
""",
    )
    write_file(
        memory_dir / "sessions" / "2026" / "03" / "2026-03-25-ranking-feedback.md",
        """---
id: 'session:2026-03-25:ranking-feedback'
memory_type: session
title: 'ranking-feedback'
summary: 'Need a better ordering signal for derived files.'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'feedback'
---

# Session: ranking-feedback
""",
    )


def test_query_memory_current_state_prefers_recent_and_topic_summaries(
    tmp_path: Path,
) -> None:
    seed_memory_tree(tmp_path)
    script = SCRIPTS_DIR / "query_memory.py"

    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--query-type",
        "current-state",
        "--topic",
        "workspace",
    )

    assert result.returncode == 0, result.stderr
    assert "generated-index:workspace-memory" in result.stdout
    assert "generated-summary:recent" in result.stdout
    assert "topic-summary:workspace-memory" in result.stdout
    assert "session:2026-03-25:workspace-memory-maintenance-automation" not in result.stdout
    assert "crystal:workspace-memory-updates-stay-schema-scoped" not in result.stdout


def test_query_memory_exact_id_returns_single_match(tmp_path: Path) -> None:
    seed_memory_tree(tmp_path)
    script = SCRIPTS_DIR / "query_memory.py"

    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--id",
        "crystal:workspace-memory-updates-stay-schema-scoped",
    )

    assert result.returncode == 0, result.stderr
    assert "crystal:workspace-memory-updates-stay-schema-scoped" in result.stdout
    assert "topic-summary:workspace-memory" not in result.stdout
    assert "generated-summary:recent" not in result.stdout


def test_query_memory_experience_promotes_topic_summary_with_lineage_overlap(
    tmp_path: Path,
) -> None:
    seed_memory_tree(tmp_path)
    script = SCRIPTS_DIR / "query_memory.py"

    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--query-type",
        "experience",
        "--topic",
        "feedback",
    )

    assert result.returncode == 0, result.stderr
    assert "topic-summary:workspace-memory" in result.stdout
    assert "lineage overlap" in result.stdout
    assert result.stdout.index("topic-summary:workspace-memory") < result.stdout.index(
        "session:2026-03-25:ranking-feedback"
    )


def test_query_memory_experience_does_not_use_recent_lineage_as_global_fallback(
    tmp_path: Path,
) -> None:
    seed_memory_tree(tmp_path)
    script = SCRIPTS_DIR / "query_memory.py"

    result = run_script(
        str(script),
        "--root",
        str(tmp_path),
        "--query-type",
        "experience",
        "--topic",
        "nosuchtoken",
    )

    assert result.returncode == 0, result.stderr
    assert "generated-summary:recent" in result.stdout
    assert "topic-summary:workspace-memory" not in result.stdout
    assert "crystal:workspace-memory-updates-stay-schema-scoped" not in result.stdout
    assert "session:2026-03-25:ranking-feedback" not in result.stdout
