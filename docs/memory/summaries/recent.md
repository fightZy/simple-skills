---
id: 'generated-summary:recent'
memory_type: 'generated-summary'
title: 'recent memory summary'
summary: 'Auto-generated view of active recent sessions and pending follow-ups.'
created_at: '2026-03-25'
updated_at: '2026-03-25'
generator: 'init_memory.py'
source_ids:
  - 'session:2026-03-25:workspace-memory-query-boundary-fix'
  - 'session:2026-03-25:workspace-memory-derived-lineage'
  - 'session:2026-03-25:workspace-memory-query-automation'
  - 'session:2026-03-25:workspace-memory-dogfood-query-foundation'
  - 'session:2026-03-25:workspace-memory-maintenance-automation'
  - 'session:2026-03-25:workspace-memory-runtime-boundary'
---

# Recent Memory

## Active Context
- Current priorities
- Current risks

## Recent Sessions
- 2026-03-25 [workspace-memory-query-boundary-fix]: Do not use recent.md source_ids as a global fallback evidence set for experience queries when no session matches the filter.; related files: .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_query_memory.py; next step: Continue improving richer ranking among multiple genuinely relevant derived candidates.
- 2026-03-25 [workspace-memory-derived-lineage]: Maintain source_ids and updated_at on recent and archive summaries through record_session.py and refine_memory.py.; related files: .agents/skills/workspace-memory-skill/scripts/memory_ops.py, .agents/skills/workspace-memory-skill/scripts/record_session.py, .agents/skills/workspace-memory-skill/scripts/refine_memory.py, .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_existing_scripts_smoke.py, tests/workspace-memory-skill/test_query_memory.py; next step: Improve richer ranking among multiple derived candidates after lineage signals are stable.
- 2026-03-25 [workspace-memory-query-automation]: Implement query_memory.py as a metadata-first layered retrieval CLI instead of a free-form search or answer synthesizer.; related files: .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_query_memory.py, .agents/skills/workspace-memory-skill/references/operations/query-memory.md; next step: Improve richer ranking and derived lineage after the first query CLI is stable.
- 2026-03-25 [workspace-memory-dogfood-query-foundation]: Promote the runtime-boundary and schema-scoped-maintenance rules into durable crystals.; related files: docs/memory/crystals/crystal-installable-skills-keep-runtime-only-payloads.md, docs/memory/crystals/crystal-workspace-memory-updates-stay-schema-scoped.md, docs/memory/summaries/topics/workspace-memory.md; next step: Design and implement a minimal metadata-first query_memory.py CLI next.
- 2026-03-25 [workspace-memory-maintenance-automation]: Add script-supported create/update flows for crystal and topic-summary memory files.; related files: .agents/skills/workspace-memory-skill/scripts/memory_ops.py, .agents/skills/workspace-memory-skill/scripts/update_crystal.py, .agents/skills/workspace-memory-skill/scripts/update_topic_summary.py, .agents/skills/workspace-memory-skill/references/operations/topic-summary-maintenance.md; next step: Use the new maintenance scripts when future workspace-memory sessions need durable knowledge extraction or topic aggregation.
- 2026-03-25 [workspace-memory-runtime-boundary]: Treat .agents/skills/<skill> as the runtime installation boundary and keep development-only tests at the repository root.; related files: .agents/skills/workspace-memory-skill/README.md, README.md, .gitignore, tests/workspace-memory-skill/test_runtime_layout.py; next step: Apply the same runtime-vs-development boundary to future skills added to this repository.
## Pending Follow-ups
- Continue improving richer ranking among multiple genuinely relevant derived candidates.
- Improve richer ranking among multiple derived candidates after lineage signals are stable.
- Use the new maintenance scripts when future workspace-memory sessions need durable knowledge extraction or topic aggregation.
- Apply the same runtime-vs-development boundary to future skills added to this repository.
