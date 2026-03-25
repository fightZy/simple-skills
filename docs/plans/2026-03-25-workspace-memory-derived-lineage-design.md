# Workspace Memory Derived Lineage Design

**Date:** 2026-03-25

## Goal

Make derived workspace-memory files mechanically traceable by keeping `source_ids` and `updated_at` accurate for generated summaries, then use that lineage in query ranking.

## Problem

The workspace-memory skill now has:

- scripted source files: sessions
- scripted durable derived files: crystals and topic summaries
- scripted generated summaries: recent and archive
- a first query CLI

But two gaps remain:

1. `recent.md` does not maintain `source_ids`, so active derived context is not traceable
2. `archive.md` and `recent.md` do not refresh lineage and freshness metadata consistently during refinement
3. `query_memory.py` can rank by type and simple filters, but cannot use lineage overlap to promote the best derived files

## Scope

This batch adds:

- `source_ids` maintenance for `summaries/recent.md`
- `source_ids` and `updated_at` maintenance for `summaries/archive.md`
- lineage-aware ranking in `query_memory.py`
- regression tests for record-session, refine-memory, and query ranking
- docs updates reflecting the new lineage boundary

This batch does not add:

- generic graph traversal
- semantic ranking
- arbitrary cross-file dependency repair
- automatic topic-summary or crystal refresh from lineage alone

## Design Constraints

- keep the repo-local Markdown model
- preserve the narrow existing CLIs
- avoid introducing a database or global index
- derive lineage from existing stable identifiers, not fuzzy text links

## Options Considered

### Option 1: Query-only ranking tweaks

Improve `query_memory.py` heuristics without changing derived-file metadata.

Pros:
- smallest immediate change

Cons:
- ranking stays heuristic-only
- derived files remain untraceable
- future retrieval work still lacks reliable signals

### Option 2: Minimal derived lineage plus lineage-aware query

Maintain `source_ids` and `updated_at` on generated summaries and let query ranking consume them.

Pros:
- smallest end-to-end closed loop
- gives query a reliable signal
- improves freshness and traceability together

Cons:
- requires touching multiple scripts in one batch

### Option 3: Full lineage graph

Track broader relationships across sessions, summaries, crystals, and topic summaries with richer traversal.

Pros:
- best long-term retrieval foundation

Cons:
- too large for the current batch
- would force new abstractions before the current write path is mature

## Chosen Approach

Choose Option 2.

This is the first point where lineage becomes operationally useful without turning workspace memory into a graph system.

## Data Contract

### `summaries/recent.md`

- `source_ids` contains the session ids represented by the current `## Recent Sessions` list
- `updated_at` refreshes whenever the file content changes
- `created_at` remains stable

### `summaries/archive.md`

- `source_ids` contains the session ids represented by the archived `## Important History` entries
- `updated_at` refreshes whenever archive content changes
- `created_at` remains stable

## Derivation Rules

Recent and archive entries already carry stable date + topic shapes:

- recent entry: `- YYYY-MM-DD [topic]: ...`
- archive entry: `- YYYY-MM-DD [topic]: ...`

The scripts should derive a session id by combining:

- the date from the entry
- the slugified topic from inside `[...]`

Result:

- `session:YYYY-MM-DD:<topic-slug>`

This keeps lineage deterministic without opening every session file during summary maintenance.

## Query Ranking Rules

The first query CLI should remain file-centric, but it can use lineage in two ways:

1. If a session directly matches a query, promote topic summaries and crystals whose `source_ids` include that session id
2. If `recent.md` or `archive.md` is in the result set, treat their `source_ids` as active supporting evidence when ranking related derived files

The effect should be:

- directly related topic summaries and crystals rise above unrelated sessions
- raw sessions remain available as evidence, but lower in the result list unless no derived file is related

## Implementation Shape

### Shared helpers

Add small helper functions to `memory_ops.py` for:

- reading frontmatter metadata for generated summaries
- normalizing `source_ids`
- rebuilding metadata with refreshed `updated_at`
- deriving session ids from summary bullets

### `record_session.py`

- update `recent.md` frontmatter after inserting the new recent entry
- rebuild `source_ids` from the resulting recent entries
- refresh `updated_at`

### `refine_memory.py`

- rebuild `source_ids` for retained recent entries
- rebuild `source_ids` for archive entries after merge
- refresh `updated_at` on both files when rewritten

### `query_memory.py`

- calculate lineage overlap between candidate derived files and matched sessions / derived summaries
- use lineage overlap as a ranking boost, not as a replacement for the existing query-type order

## Risks

### Risk 1: Entry parsing drift

If generated entry formatting changes, lineage derivation can break.

Mitigation:
- parse only the existing stable bullet format
- cover both recent and archive entry shapes with tests

### Risk 2: Metadata rewrite clobbers fields

Mitigation:
- preserve untouched metadata fields
- explicitly preserve `created_at`

### Risk 3: Query becomes opaque

Mitigation:
- keep reason strings explicit
- describe lineage-based promotion in output text

## Self-Review

This design intentionally stops at generated-summary lineage and query ranking. It does not try to infer missing links across arbitrary manually edited files. That keeps the batch small enough to finish and strong enough to support the next retrieval iteration.
