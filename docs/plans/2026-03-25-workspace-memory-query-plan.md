# Workspace Memory Query Script Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a minimal metadata-first `query_memory.py` CLI that returns the most relevant workspace-memory files for current-state, experience, norms, or exact-id lookup.

**Architecture:** Reuse typed Markdown metadata from the existing memory files and apply deterministic retrieval order per query type. Keep the first version human-readable and narrow: metadata loading, filtering, ordering, and result printing only.

**Tech Stack:** Python 3, argparse, pathlib, existing `memory_ops.py`, pytest

---

### Task 1: Add failing query script tests

**Files:**
- Create: `D:\code\simple-skills\tests\workspace-memory-skill\test_query_memory.py`

**Step 1: Write the failing tests**

```python
def test_query_memory_current_state_prefers_recent_and_topic_summaries(tmp_path):
    ...

def test_query_memory_exact_id_returns_single_match(tmp_path):
    ...
```

**Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/workspace-memory-skill/test_query_memory.py -q`
Expected: FAIL because `query_memory.py` does not exist yet

### Task 2: Implement the minimal query CLI

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\query_memory.py`

**Step 1: Load typed metadata from the workspace memory tree**

```python
metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
```

**Step 2: Add query-type retrieval ordering**

```python
QUERY_ORDER = {
    "current-state": [...],
    "experience": [...],
    "norms": [...],
}
```

**Step 3: Implement exact-id lookup and filtered layered retrieval**

```python
if args.id:
    ...
```

**Step 4: Run the focused query tests**

Run: `python -m pytest tests/workspace-memory-skill/test_query_memory.py -q`
Expected: PASS

### Task 3: Document the new query automation boundary

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\SKILL.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\README.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\operations\query-memory.md`

**Step 1: Update the current automation boundary**

```md
Script-supported today:
- ...
- query retrieval via `scripts/query_memory.py`
```

**Step 2: Add command examples for query flows**

```md
python3 scripts/query_memory.py --root <workspace> --query-type norms --tag workspace-memory
```

**Step 3: Run the workspace-memory test suite**

Run: `python -m pytest tests/workspace-memory-skill -q`
Expected: PASS
