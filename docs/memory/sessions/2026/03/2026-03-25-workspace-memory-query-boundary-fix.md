---
id: 'session:2026-03-25:workspace-memory-query-boundary-fix'
memory_type: session
title: 'workspace-memory-query-boundary-fix'
summary: 'Do not use recent.md source_ids as a global fallback evidence set for experience queries when no session matches the filter.'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'query'
  - 'review-follow-up'
---

# Session: workspace-memory-query-boundary-fix

## Goal
Capture the review-driven boundary test and query fallback fix for workspace-memory retrieval.

## Key Decisions
- Do not use recent.md source_ids as a global fallback evidence set for experience queries when no session matches the filter.

## Rationale
- Lineage should refine relevant derived candidates, not bypass the query filter and recall unrelated files.

## Changes
- Added a boundary regression test covering no-match experience queries.
- Updated query_memory.py so lineage boosts only apply when actual session evidence exists.

## Open Questions
- None

## Follow-up
- Continue improving richer ranking among multiple genuinely relevant derived candidates.

## Crystallization Candidates
- None


## Related Files
- .agents/skills/workspace-memory-skill/scripts/query_memory.py
- tests/workspace-memory-skill/test_query_memory.py

## Related References
- review:local-boundary-finding