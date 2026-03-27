---
id: 'topic-summary:workspace-memory'
memory_type: 'topic-summary'
title: 'Workspace memory status'
summary: '写入路径、query 检索、benchmark harness 与 companion skills 已脚本化；benchmark 报告现已支持 bucket 级 diagnostics，下一步是接入固定 LLM QA 与 LoCoMo 适配。'
created_at: '2026-03-25'
updated_at: '2026-03-27'
topic: 'workspace memory'
source_ids:
  - 'session:2026-03-25:workspace-memory-maintenance-automation'
  - 'session:2026-03-25:workspace-memory-runtime-boundary'
  - 'session:2026-03-25:workspace-memory-query-automation'
  - 'session:2026-03-25:workspace-memory-derived-lineage'
  - 'session:2026-03-25:workspace-memory-query-boundary-fix'
  - 'session:2026-03-25:workspace-memory-language-config'
  - 'session:2026-03-27:workspace-memory-benchmark-companions'
  - 'session:2026-03-27:workspace-memory-benchmark-diagnostics'
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
- Workspace-memory 现在已有 repo 自建 retrieval benchmark，可按 current-state、lineage、norms-ordering、negative、exact-id 等 bucket 评测。
- Benchmark 工作流已拆为两个配套 skill：一个负责新增样例，一个负责运行并解读评测结果。
- Workspace-memory retrieval benchmark 报告现在会按 bucket 汇总 expected_top_hit、forbidden_hit，以及被 limit 裁掉的强候选类型。
## Key Decisions
- Treat runtime-vs-development layout as a durable repo rule for installable skills.
- Keep maintenance automation schema-scoped and narrow instead of introducing a generic patching layer.
- Keep the first query script file-centric and metadata-first instead of synthesizing final answers.
- Generated summary lineage should be rebuilt mechanically from rendered session-entry bullets instead of inferred heuristically.
- Lineage overlap should only boost derived files after the query has found real supporting session evidence.
- 将语言一致性收敛为配置文件、初始化约束和校验脚本，而不是引入 locale 渲染层。
- Keep benchmark authoring and benchmark analysis as companion skills instead of folding maintainer workflows into the main workspace-memory runtime skill.
- Add bucket and forbidden-candidate metadata so benchmark results can guide retrieval optimization instead of only reporting aggregate pass rates.
- Keep benchmark diagnostics in runner-level case and bucket summaries so retrieval regressions are diagnosable without changing the fixture schema or query CLI contract.
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
- session:2026-03-27:workspace-memory-benchmark-companions
- session:2026-03-27:workspace-memory-benchmark-diagnostics
