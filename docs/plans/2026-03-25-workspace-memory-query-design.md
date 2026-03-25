# Workspace Memory Query Script Design

**Date:** 2026-03-25

## Goal

Add the first dedicated `query_memory.py` script for workspace-memory so agents can retrieve the most relevant memory files without relying only on prose reference cards.

## Problem

The workspace-memory skill now has scripted write paths for:

- initialization
- session capture
- recent/archive refinement
- crystal create/update
- topic-summary create/update

But retrieval is still manual and reference-driven. That leaves three practical gaps:

1. the retrieval order is documented but not executable
2. agents cannot ask for a narrow query result set from the command line
3. the new topic-summary and crystal layers are populated, but there is no script that prefers them over raw sessions

## Scope

This batch adds:

- `.agents/skills/workspace-memory-skill/scripts/query_memory.py`
- focused tests for query ordering, filtering, and exact id lookup
- docs updates describing the new query automation boundary

This batch does not add:

- semantic ranking
- free-form answer synthesis
- cross-workspace retrieval
- lineage repair

## Options Considered

### Option 1: Grep-style file scan

Search file contents or filenames and print matches.

Pros:
- smallest implementation

Cons:
- ignores typed memory layers
- does not encode the retrieval rules already documented
- tends to over-return session files

### Option 2: Metadata-first layered retrieval

Load typed memory files, apply the documented read order per query type, then print the best candidate files with reason strings.

Pros:
- matches the current skill model
- prefers summaries and crystals before raw sessions
- keeps implementation narrow and testable

Cons:
- requires a small retrieval model up front

### Option 3: Full ranking engine

Build a richer scorer with broader text matching and source graph traversal.

Pros:
- strongest long-term retrieval surface

Cons:
- too large for the first query batch
- drags lineage and freshness work into the critical path

## Chosen Approach

Choose Option 2.

The first query script should make the existing layered memory model executable, not replace it with a search engine.

## CLI Shape

`query_memory.py` should support:

- `--root`
- `--memory-dir`
- `--query-type current-state|experience|norms`
- `--topic`
- `--tag` repeatable
- `--id`
- `--limit`

## Retrieval Rules

### Exact id lookup

If `--id` is provided, return only the matching file.

### Current state

Prefer:
1. `index.md`
2. `summaries/recent.md`
3. matching topic summaries

Do not return sessions unless there are explicit filters and no higher-level match.

### Experience

Prefer:
1. `summaries/recent.md`
2. matching topic summaries
3. matching crystals
4. matching sessions

### Norms

Prefer:
1. matching crystals
2. matching topic summaries
3. matching sessions

## Matching Rules

Match against:

- metadata `id`
- `title`
- `summary`
- `tags`
- `topic`
- relative path

Use case-insensitive substring matching.

## Output

Keep the script human-readable and deterministic.

For each result, print:

- file kind
- id
- title
- relative path
- short reason
- summary

The script should not print the full file body in this batch.

## Risks

### Risk 1: Over-returning sessions

Mitigation:
- encode shallow-layer preference directly in query-type ordering
- keep sessions last in all non-id flows

### Risk 2: Query semantics drift from docs

Mitigation:
- mirror the existing query reference wording closely
- update operation cards and README in the same batch

### Risk 3: Needing lineage before query works

Mitigation:
- keep the first version metadata-first and local
- defer source graph traversal to a later batch

## Self-Review

This design intentionally stays below "answer generation". It returns relevant memory files in a way that future agent prompts can consume directly, while keeping the current repo-local Markdown model intact.
