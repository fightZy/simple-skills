---
id: 'session:2026-03-25:workspace-memory-query-automation'
memory_type: session
title: 'workspace-memory-query-automation'
summary: 'Implement query_memory.py as a metadata-first layered retrieval CLI instead of a free-form search or answer synthesizer.'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'query'
---

# Session: workspace-memory-query-automation

## Goal
Add the first dedicated query CLI for metadata-first workspace-memory retrieval.

## Key Decisions
- Implement query_memory.py as a metadata-first layered retrieval CLI instead of a free-form search or answer synthesizer.

## Rationale
- The first query batch should make the existing read-order model executable while keeping sessions behind summaries and crystals.

## Changes
- Added query_memory.py and focused tests for current-state ordering and exact id lookup.
- Updated skill docs and query operation guidance to document the scripted query path.

## Open Questions
- None

## Follow-up
- Improve richer ranking and derived lineage after the first query CLI is stable.

## Crystallization Candidates
- The first query script should return candidate memory files, not synthesize final answers.


## Related Files
- .agents/skills/workspace-memory-skill/scripts/query_memory.py
- tests/workspace-memory-skill/test_query_memory.py
- .agents/skills/workspace-memory-skill/references/operations/query-memory.md

## Related References
- topic-summary:workspace-memory