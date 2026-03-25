---
id: 'topic-summary:workspace-memory'
memory_type: 'topic-summary'
title: 'Workspace memory status'
summary: 'Write paths, generated-summary lineage, first-pass retrieval, and language-policy enforcement are scripted; richer multi-candidate ranking remains the next iteration.'
created_at: '2026-03-25'
updated_at: '2026-03-25'
topic: 'workspace memory'
source_ids:
  - 'session:2026-03-25:workspace-memory-maintenance-automation'
  - 'session:2026-03-25:workspace-memory-runtime-boundary'
  - 'session:2026-03-25:workspace-memory-query-automation'
  - 'session:2026-03-25:workspace-memory-derived-lineage'
  - 'session:2026-03-25:workspace-memory-query-boundary-fix'
  - 'session:2026-03-25:workspace-memory-language-config'
tags:
  - 'workspace-memory'
  - 'roadmap'
---

# Topic Summary: workspace memory

## Current State
- Initialization, session capture, recent refinement, crystal maintenance, and topic-summary maintenance are script-supported.
- Current workspace memory is still shallow: summaries exist, but only a small set of sessions and no prior crystals/topics had been populated.
- The first dedicated query_memory.py CLI now retrieves candidate files by query type and exact id lookup.
- recent.md and archive.md now maintain source_ids and updated_at as derived lineage metadata.
- Experience queries no longer use recent.md lineage as a global fallback when there is no matching session evidence.
- docs/memory/config.toml 现在可以固定 workspace memory 正文语言，同时保留英文标题和 ASCII 文件名。
## Key Decisions
- Treat runtime-vs-development layout as a durable repo rule for installable skills.
- Keep maintenance automation schema-scoped and narrow instead of introducing a generic patching layer.
- Keep the first query script file-centric and metadata-first instead of synthesizing final answers.
- Generated summary lineage should be rebuilt mechanically from rendered session-entry bullets instead of inferred heuristically.
- Lineage overlap should only boost derived files after the query has found real supporting session evidence.
- 将语言一致性收敛为配置文件、初始化约束和校验脚本，而不是引入 locale 渲染层。
## Relevant Crystals
- crystal:installable-skills-keep-runtime-only-payloads
- crystal:workspace-memory-updates-stay-schema-scoped
- crystal:workspace-memory-content-language-is-config-driven
## Source Trail
- session:2026-03-25:workspace-memory-maintenance-automation
- session:2026-03-25:workspace-memory-runtime-boundary
- session:2026-03-25:workspace-memory-query-automation
- session:2026-03-25:workspace-memory-derived-lineage
- session:2026-03-25:workspace-memory-query-boundary-fix
- session:2026-03-25:workspace-memory-language-config
