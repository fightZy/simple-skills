# Workspace Memory Derived Lineage Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make generated workspace-memory summaries maintain accurate `source_ids` and `updated_at`, then use those lineage signals to improve query ranking.

**Architecture:** Extend the existing Markdown helper layer with small lineage utilities rather than adding a new storage abstraction. Update `record_session.py` and `refine_memory.py` to rebuild derived metadata from their rendered bullet sections, then teach `query_memory.py` to promote derived files whose `source_ids` overlap matched session evidence.

**Tech Stack:** Python 3, argparse, pathlib, existing `memory_ops.py`, pytest

---

### Task 1: Add failing regression tests for derived summary lineage

**Files:**
- Modify: `D:\code\simple-skills\tests\workspace-memory-skill\test_existing_scripts_smoke.py`

**Step 1: Write failing tests**

```python
def test_record_session_updates_recent_source_ids_and_updated_at(tmp_path):
    ...

def test_refine_memory_rebuilds_recent_and_archive_source_ids(tmp_path):
    ...
```

**Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/workspace-memory-skill/test_existing_scripts_smoke.py -q`
Expected: FAIL because the current scripts do not maintain derived lineage metadata

### Task 2: Add failing lineage-aware query ranking tests

**Files:**
- Modify: `D:\code\simple-skills\tests\workspace-memory-skill\test_query_memory.py`

**Step 1: Write failing tests**

```python
def test_query_memory_experience_promotes_topic_summary_with_lineage_overlap(tmp_path):
    ...
```

**Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/workspace-memory-skill/test_query_memory.py -q`
Expected: FAIL because `query_memory.py` does not rank by lineage overlap yet

### Task 3: Implement lineage helpers and generated-summary metadata maintenance

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\record_session.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\refine_memory.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\init_memory.py`

**Step 1: Add helper functions for metadata refresh and entry-to-session-id derivation**

```python
def source_ids_from_summary_entries(entries: list[str]) -> list[str]:
    ...
```

**Step 2: Rebuild `recent.md` metadata after session capture**

```python
metadata["source_ids"] = source_ids_from_summary_entries(recent_entries)
metadata["updated_at"] = session_date
```

**Step 3: Rebuild `recent.md` and `archive.md` metadata after refinement**

```python
archive_metadata["source_ids"] = source_ids_from_summary_entries(archive_entries)
```

**Step 4: Run the smoke tests**

Run: `python -m pytest tests/workspace-memory-skill/test_existing_scripts_smoke.py -q`
Expected: PASS

### Task 4: Implement lineage-aware query ranking

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\query_memory.py`

**Step 1: Compute matched session evidence**

```python
matched_session_ids = {...}
```

**Step 2: Boost derived files whose `source_ids` overlap that evidence**

```python
if overlap:
    score += 100
```

**Step 3: Update reason strings to mention lineage overlap**

```python
"topic summary matched via lineage overlap"
```

**Step 4: Run focused query tests**

Run: `python -m pytest tests/workspace-memory-skill/test_query_memory.py -q`
Expected: PASS

### Task 5: Sync docs and templates

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\README.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\README_zh.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\SKILL.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\schema.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\operations\refine-recent.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\operations\query-memory.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\templates\generated-recent.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\templates\archive-summary.md`

**Step 1: Document derived lineage expectations**

```md
- generated summaries now maintain `source_ids` for their represented session entries
```

**Step 2: Document lineage-aware query behavior**

```md
- query ranking now prefers derived files whose `source_ids` overlap matched session evidence
```

**Step 3: Run the full workspace-memory suite**

Run: `python -m pytest tests/workspace-memory-skill -q`
Expected: PASS

### Task 6: Record the completed lineage iteration and self-review

**Files:**
- Modify: `D:\code\simple-skills\docs\memory\summaries\recent.md`
- Modify: `D:\code\simple-skills\docs\memory\summaries\topics\workspace-memory.md`
- Create: `D:\code\simple-skills\docs\memory\sessions\2026\03\2026-03-25-workspace-memory-derived-lineage.md`

**Step 1: Record the implementation session**

```bash
python .agents/skills/workspace-memory-skill/scripts/record_session.py ...
```

**Step 2: Refresh the workspace-memory topic summary**

```bash
python .agents/skills/workspace-memory-skill/scripts/update_topic_summary.py ...
```

**Step 3: Perform a self-review over changed files before final reporting**

Run: `git diff -- . ':!AGENTS.md'`
Expected: the diff matches the planned lineage and query changes without unrelated regressions
