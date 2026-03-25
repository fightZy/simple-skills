---
id: 'session:2026-03-25:workspace-memory-derived-lineage'
memory_type: session
title: 'workspace-memory-derived-lineage'
summary: 'Maintain source_ids and updated_at on recent and archive summaries through record_session.py and refine_memory.py.'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'lineage'
---

# Session: workspace-memory-derived-lineage

## Goal
Complete derived lineage maintenance for generated summaries and use it in query ranking.

## Key Decisions
- Maintain source_ids and updated_at on recent and archive summaries through record_session.py and refine_memory.py.
- Use lineage overlap as a ranking boost for topic summaries and crystals in query_memory.py.

## Rationale
- Generated summaries need traceable source metadata before query ranking can safely depend on them.

## Changes
- Added lineage helpers in memory_ops.py and refreshed recent/archive metadata maintenance in generated-summary scripts.
- Extended query_memory.py to promote derived files with source_ids overlap.

## Open Questions
- None

## Follow-up
- Improve richer ranking among multiple derived candidates after lineage signals are stable.

## Crystallization Candidates
- None


## Related Files
- .agents/skills/workspace-memory-skill/scripts/memory_ops.py
- .agents/skills/workspace-memory-skill/scripts/record_session.py
- .agents/skills/workspace-memory-skill/scripts/refine_memory.py
- .agents/skills/workspace-memory-skill/scripts/query_memory.py
- tests/workspace-memory-skill/test_existing_scripts_smoke.py
- tests/workspace-memory-skill/test_query_memory.py