# Workspace Memory Skill

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`workspace-memory-skill` is a repo-local memory workflow for shared workspace context. It is designed for small teams working with agents inside a single repository or workspace, where the main problem is not lack of information but lack of durable, retrievable, structured memory.

The skill is intentionally narrower than a general "agent memory platform". It focuses on:
- Markdown-first memory stored in the workspace
- script-generated metadata
- layered memory for recent, archived, and crystallized knowledge
- progressive retrieval to reduce context cost

## Design Chain

The design evolved through several narrowing steps:

1. Generic memory idea
   The starting point was a general AI memory capability for saving sessions, summaries, and long-term knowledge.

2. Workspace-scoped memory
   The direction was narrowed to a single workspace because the real pain was repeated explanation, lost rationale, and inconsistent understanding inside one shared project.

3. Repo-local Markdown
   The design deliberately avoided external storage and vector infrastructure in the first version. The first priority was team adoption, inspectability, and low workflow friction.

4. Layered memory
   The memory model was split into:
   - session memory for first-party records
   - recent summary for active context
   - archive summary for compressed history
   - crystals for durable knowledge

5. Progressive retrieval
   Instead of reading everything, the intended flow became:
   - generated summary or navigation layer
   - topic or crystal layer
   - source session only when necessary

6. Script-owned metadata
   The design originally used templates that exposed frontmatter more directly. That was later tightened so metadata is treated as system-owned where possible, while the agent focuses on semantic inputs and body content.

7. Routing plus operation cards
   `SKILL.md` was reduced to a routing layer. Detailed instructions for each operation moved into `references/operations/` so the agent can see:
   - when to use an operation
   - which script to call
   - what parameters are required
   - which body template applies

## Core Philosophy

The skill is guided by a few constraints:

- Metadata should be stable
  If retrieval depends on metadata, metadata cannot drift casually. Prefer scripts to generate it.

- Bodies should stay human-readable
  The memory files should still work as Markdown documents, not just as machine records.

- Primary sources and derived views should stay separate
  Session files are the source. Recent summaries, archive summaries, and optional navigation files are derived views.

- Retrieval should be progressive
  The agent should not read more than necessary.

- Avoid premature platform design
  The skill is not trying to become a generic knowledge graph, vector database, or multi-workspace memory service in the first version.

## Current Working Model

### Memory categories

- `session`
  First-party record of a concrete session or work block.

- `generated-summary`
  A script-maintained view such as `recent.md`.

- `archive-summary`
  Compressed historical view of older memory.

- `topic-summary`
  Aggregated topic-level summary.

- `crystal`
  Durable knowledge that should influence future work.

### Crystal knowledge types

Crystals currently use `knowledge_type` rather than `crystal_type` to keep the model more general:
- `rule`
- `decision`
- `pattern`
- `insight`

This keeps crystals usable beyond pure coding preferences and allows the skill to support more general workspace knowledge.

### Metadata ownership

The current rule is:
- scripts should generate or update metadata whenever possible
- templates should primarily describe body structure
- schema rules live in `references/schema.md`

## File Layout

The main runtime pieces are:

- `SKILL.md`
  Runtime entrypoint and routing layer

- `references/schema.md`
  Metadata rules

- `references/templates.md`
  Template navigation

- `references/templates/`
  Body-first templates for each memory type

- `references/operations/`
  Operation cards that connect user intent to scripts and templates

- `scripts/`
  Deterministic helpers for initialization, session capture, and recent-memory refinement

Development-only assets stay outside the installable skill directory.
Tests for this skill live under `tests/workspace-memory-skill/` at the repository root so the runtime skill payload stays limited to files an agent actually needs to read or execute.

## Workflow Model

### 1. Initialize memory

The skill uses `scripts/init_memory.py` to create the memory tree and seed generated files.

### 2. Record a session

The skill uses `scripts/record_session.py` to:
- create the session file path
- generate session metadata
- update `summaries/recent.md`
- refresh `summaries/recent.md` lineage metadata

The agent should focus on:
- topic
- summary-relevant content
- decisions, rationale, changes, follow-up, crystallization candidates

### 3. Refine recent memory

The skill uses `scripts/refine_memory.py` to:
- keep recent memory small
- move older recent entries into archive history
- shrink pending follow-ups to match retained active context
- rebuild derived `source_ids` for recent and archive summaries

### 4. Query memory

Query retrieval is now script-supported through:
- `scripts/query_memory.py`

The first version is metadata-first and layered. It returns relevant memory files by query type instead of trying to synthesize a final answer inside the script.
It now also uses lineage overlap to promote related topic summaries and crystals above raw sessions when the evidence is traceable.

### 5. Maintain crystals

Crystal creation and maintenance are script-supported through:
- `scripts/create_crystal.py`
- `scripts/update_crystal.py`

The current implementation is intentionally narrow: updates operate on known metadata fields and known sections.

### 6. Maintain topic summaries

Topic summary creation and maintenance are script-supported through:
- `scripts/create_topic_summary.py`
- `scripts/update_topic_summary.py`

This gives the skill a first complete write path for both durable knowledge and aggregated topic views.

## Why `index.md` Still Exists

The design moved away from treating `index.md` as an authoritative manually maintained file.

Current position:
- `index.md` is optional and generated
- it is useful as a human-facing navigation page
- it should not be the canonical source of truth

The canonical source is the set of typed memory files with structured metadata.

## Current Automation Boundary

Implemented:
- `scripts/init_memory.py`
- `scripts/record_session.py`
- `scripts/refine_memory.py`
- `scripts/query_memory.py`
- `scripts/create_crystal.py`
- `scripts/update_crystal.py`
- `scripts/create_topic_summary.py`
- `scripts/update_topic_summary.py`

Partially designed but not fully implemented:
- broader derived-file freshness beyond recent/archive
- richer query ranking and answer synthesis

## Known Gaps

These parts are not yet complete:

1. Query automation
   The first query CLI now supports lineage-aware retrieval, but it still returns candidate files rather than synthesized answers.

2. Crystal write path
   The first scripted write path now exists, but broader maintenance and deduplication flows are still manual.

3. Topic summaries
   The first scripted creation/update flow now exists, but richer aggregation logic is still manual.

4. Derived-file freshness
   `recent.md` and `archive.md` now refresh `updated_at` and `source_ids`, but broader derived indexes are not yet built.

5. Source lineage completeness
   Generated summaries now maintain `source_ids`, but lineage is still not used to auto-refresh topic summaries or crystals.

6. Migration of existing memory
   Current scripts are oriented around fresh or lightly structured memory, not bulk migration from arbitrary existing notes.

## Non-Goals For Now

The skill is intentionally not doing these yet:
- external vector stores
- cross-workspace memory federation
- automatic semantic ranking
- complex graph storage
- mandatory human-maintained index files

## Suggested Next Steps

If the skill continues to evolve, the most natural next moves are:

1. Add a crystal creation/update script
   Done in the current implementation batch.

2. Add a query script
   Done in the current implementation batch.

3. Add topic-summary generation
   The first maintenance scripts now exist; the next step would be richer generation and refresh workflows.

4. Improve derived lineage
   Done for recent and archive summaries in the current implementation batch.

5. Improve richer ranking
   The next step is better ranking across multiple competing derived candidates, not just lineage overlap.

## Working Principle For Future Changes

Before adding fields, files, or scripts, prefer asking:
- does this reduce ambiguity in retrieval
- does this reduce maintenance burden
- can this be enforced mechanically
- is this necessary now, or only theoretically useful later

If the answer is mostly theoretical, the change should probably wait.
