# Workspace Memory Maintenance Scripts Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add script-supported creation and update flows for `crystal` and `topic-summary` memory files, backed by a shared Markdown maintenance helper and local automated tests.

**Architecture:** Keep the current narrow-script style and add one shared internal module for frontmatter parsing, section updates, de-duplication, placeholder management, and path/id helpers. Implement four dedicated CLIs on top of that helper, then update the runtime docs to reflect the new automation boundary.

**Tech Stack:** Python 3, argparse, pathlib, pytest, Markdown files with simple YAML frontmatter

---

### Task 1: Validate the local Python test environment

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\.gitkeep`

**Step 1: Check Python availability**

```powershell
python --version
```

**Step 2: Check pytest availability**

```powershell
python -m pytest --version
```

**Step 3: Create the test directory if it does not exist**

```powershell
New-Item -ItemType Directory -Force 'D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests'
```

**Step 4: Add a placeholder so the directory is tracked**

```text
# empty placeholder file
```

**Step 5: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/.gitkeep
git commit -m "chore: seed workspace-memory test directory"
```

### Task 2: Add failing tests for crystal creation

**Files:**
- Test: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_create_crystal.py`

**Step 1: Write the failing test**

```python
def test_create_crystal_writes_expected_file(tmp_path):
    ...
    assert crystal_path.exists()
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_crystal.py -q`
Expected: FAIL because `create_crystal.py` does not exist yet

**Step 3: Commit the failing test**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_create_crystal.py
git commit -m "test: add failing crystal creation coverage"
```

### Task 3: Implement the shared helper skeleton

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`

**Step 1: Write the minimal helper API**

```python
def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    ...

def dump_frontmatter(metadata: dict[str, object], body: str) -> str:
    ...

def slugify(value: str) -> str:
    ...
```

**Step 2: Run the crystal creation test**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_crystal.py -q`
Expected: FAIL because the create script is still missing

**Step 3: Commit**

```bash
git add .agents/skills/workspace-memory-skill/scripts/memory_ops.py
git commit -m "refactor: add workspace-memory helper module"
```

### Task 4: Implement `create_crystal.py`

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\create_crystal.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`

**Step 1: Write the minimal create CLI**

```python
parser.add_argument("--title", required=True)
parser.add_argument("--summary", required=True)
parser.add_argument("--knowledge-type", required=True)
parser.add_argument("--source-id", action="append", default=[])
```

**Step 2: Create the file with canonical metadata and body**

```python
metadata = {
    "id": f"crystal:{slug}",
    "memory_type": "crystal",
}
```

**Step 3: Run the crystal creation test**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_crystal.py -q`
Expected: PASS

**Step 4: Commit**

```bash
git add .agents/skills/workspace-memory-skill/scripts/create_crystal.py .agents/skills/workspace-memory-skill/scripts/memory_ops.py
git commit -m "feat: add crystal creation script"
```

### Task 5: Add failing tests for crystal update behavior

**Files:**
- Test: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_update_crystal.py`

**Step 1: Write failing tests for append and replace**

```python
def test_update_crystal_append_statement_keeps_existing_content(tmp_path):
    ...

def test_update_crystal_rejects_memory_type_mismatch(tmp_path):
    ...
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_update_crystal.py -q`
Expected: FAIL because `update_crystal.py` does not exist yet

**Step 3: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_update_crystal.py
git commit -m "test: add failing crystal update coverage"
```

### Task 6: Implement crystal update support

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\update_crystal.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`

**Step 1: Add section-level update helpers**

```python
def update_section(text: str, heading: str, entries: list[str], mode: str) -> str:
    ...
```

**Step 2: Implement target resolution by `--path` or `--id`**

```python
if args.path:
    target = Path(args.path)
else:
    target = resolve_crystal_path(...)
```

**Step 3: Implement metadata and body updates**

```python
metadata["updated_at"] = today
```

**Step 4: Run crystal tests**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_crystal.py .agents/skills/workspace-memory-skill/tests/test_update_crystal.py -q`
Expected: PASS

**Step 5: Commit**

```bash
git add .agents/skills/workspace-memory-skill/scripts/update_crystal.py .agents/skills/workspace-memory-skill/scripts/memory_ops.py
git commit -m "feat: add crystal update script"
```

### Task 7: Add failing tests for topic-summary creation

**Files:**
- Test: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_create_topic_summary.py`

**Step 1: Write the failing test**

```python
def test_create_topic_summary_uses_default_topic_path(tmp_path):
    ...
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_topic_summary.py -q`
Expected: FAIL because `create_topic_summary.py` does not exist yet

**Step 3: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_create_topic_summary.py
git commit -m "test: add failing topic summary creation coverage"
```

### Task 8: Implement `create_topic_summary.py`

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\create_topic_summary.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`

**Step 1: Add topic-summary metadata helpers**

```python
metadata = {
    "id": f"topic-summary:{topic_slug}",
    "memory_type": "topic-summary",
    "topic": args.topic,
}
```

**Step 2: Implement default topic-summary path resolution**

```python
path = memory_dir / "summaries" / "topics" / f"{topic_slug}.md"
```

**Step 3: Run the creation test**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_topic_summary.py -q`
Expected: PASS

**Step 4: Commit**

```bash
git add .agents/skills/workspace-memory-skill/scripts/create_topic_summary.py .agents/skills/workspace-memory-skill/scripts/memory_ops.py
git commit -m "feat: add topic summary creation script"
```

### Task 9: Add failing tests for topic-summary update behavior

**Files:**
- Test: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_update_topic_summary.py`

**Step 1: Write failing tests for append, replace, and de-duplication**

```python
def test_update_topic_summary_append_deduplicates_entries(tmp_path):
    ...

def test_update_topic_summary_preserves_created_at(tmp_path):
    ...
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_update_topic_summary.py -q`
Expected: FAIL because `update_topic_summary.py` does not exist yet

**Step 3: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_update_topic_summary.py
git commit -m "test: add failing topic summary update coverage"
```

### Task 10: Implement topic-summary update support

**Files:**
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\update_topic_summary.py`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\scripts\memory_ops.py`

**Step 1: Implement target lookup by topic or path**

```python
if args.topic and not args.path:
    target = default_topic_summary_path(...)
```

**Step 2: Implement canonical section updates**

```python
body = update_section(body, "Current State", values, mode="append")
```

**Step 3: Run topic-summary tests**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_create_topic_summary.py .agents/skills/workspace-memory-skill/tests/test_update_topic_summary.py -q`
Expected: PASS

**Step 4: Commit**

```bash
git add .agents/skills/workspace-memory-skill/scripts/update_topic_summary.py .agents/skills/workspace-memory-skill/scripts/memory_ops.py
git commit -m "feat: add topic summary update script"
```

### Task 11: Add focused helper tests for parsing and placeholders

**Files:**
- Test: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_memory_ops.py`

**Step 1: Write helper tests**

```python
def test_parse_frontmatter_round_trips_simple_lists():
    ...

def test_replace_empty_section_restores_placeholder():
    ...
```

**Step 2: Run helper tests to verify behavior**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_memory_ops.py -q`
Expected: PASS

**Step 3: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_memory_ops.py
git commit -m "test: cover workspace-memory helper edge cases"
```

### Task 12: Update skill docs and operation cards

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\SKILL.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\operations\crystal-maintenance.md`
- Create: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\operations\topic-summary-maintenance.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\references\templates.md`
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\README.md`

**Step 1: Update automation-boundary text**

```md
Script-supported today:
- initialization
- session capture
- recent refinement
- crystal create/update
- topic-summary create/update
```

**Step 2: Add the new operation card**

```md
# Topic Summary Maintenance
...
```

**Step 3: Run the full test suite**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests -q`
Expected: PASS

**Step 4: Commit**

```bash
git add .agents/skills/workspace-memory-skill/SKILL.md .agents/skills/workspace-memory-skill/references/operations/crystal-maintenance.md .agents/skills/workspace-memory-skill/references/operations/topic-summary-maintenance.md .agents/skills/workspace-memory-skill/references/templates.md .agents/skills/workspace-memory-skill/README.md
git commit -m "docs: document maintenance automation scripts"
```

### Task 13: Run regression checks against existing scripts

**Files:**
- Modify: `D:\code\simple-skills\.agents\skills\workspace-memory-skill\tests\test_existing_scripts_smoke.py`

**Step 1: Add smoke tests for existing flows**

```python
def test_record_session_still_updates_recent_summary(tmp_path):
    ...

def test_refine_memory_still_archives_old_entries(tmp_path):
    ...
```

**Step 2: Run the smoke tests**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests/test_existing_scripts_smoke.py -q`
Expected: PASS

**Step 3: Run the full suite**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests -q`
Expected: PASS

**Step 4: Commit**

```bash
git add .agents/skills/workspace-memory-skill/tests/test_existing_scripts_smoke.py
git commit -m "test: add smoke coverage for existing memory scripts"
```

### Task 14: Final verification and cleanup

**Files:**
- Modify: `D:\code\simple-skills\docs\plans\2026-03-23-workspace-memory-maintenance-design.md`
- Modify: `D:\code\simple-skills\docs\plans\2026-03-23-workspace-memory-maintenance-plan.md`

**Step 1: Run the full suite one last time**

Run: `python -m pytest .agents/skills/workspace-memory-skill/tests -q`
Expected: PASS

**Step 2: Review the changed file list**

Run: `git status --short`
Expected: only the planned script, test, doc, and plan files are modified

**Step 3: Update the plan docs if any implementation details changed**

```md
## Implementation Notes
- note any deviation from the original design
```

**Step 4: Commit**

```bash
git add docs/plans/2026-03-23-workspace-memory-maintenance-design.md docs/plans/2026-03-23-workspace-memory-maintenance-plan.md
git commit -m "docs: finalize workspace-memory maintenance plan"
```
