---
id: 'generated-summary:recent'
memory_type: 'generated-summary'
title: 'recent memory summary'
summary: 'Auto-generated view of active recent sessions and pending follow-ups.'
created_at: '2026-03-25'
updated_at: '2026-03-27'
generator: 'init_memory.py'
source_ids:
  - 'session:2026-03-27:workspace-memory-benchmark-diagnostics'
  - 'session:2026-03-27:workspace-memory-benchmark-companions'
  - 'session:2026-03-25:workspace-memory-language-config'
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
- 2026-03-27 [workspace-memory-benchmark-diagnostics]: 将 expected_top_hit、forbidden_hit 和被 limit 裁掉的强候选类型纳入 benchmark 报告，而不是只看聚合通过率。; related files: scripts/benchmarks/workspace_memory/runner.py, tests/workspace-memory-skill/test_workspace_memory_benchmark.py; next step: 后续可把 diagnostics 继续扩展到 false_positive 和 layer_hit 的 bucket 级分布，进一步提高回归定位效率。
- 2026-03-27 [workspace-memory-benchmark-companions]: 新增 retrieval benchmark harness，先支持 repo 自建样例，再为固定 LLM QA 与 LoCoMo 适配保留边界。; related files: scripts/benchmarks/workspace_memory/dataset.py, scripts/benchmarks/workspace_memory/runner.py, tests/workspace-memory-skill/test_workspace_memory_benchmark.py, .agents/skills/workspace-memory-benchmark-authoring/SKILL.md, .agents/skills/workspace-memory-benchmark-analysis/SKILL.md; next step: 下一步可接入真实固定 LLM adapter，并将 LoCoMo 数据转换接到现有内部 case schema。
- 2026-03-25 [workspace-memory-language-config]: 用 docs/memory/config.toml 的 content_language 控制正文语言，缺省回退为英文。; related files: docs/memory/config.toml, .agents/skills/workspace-memory-skill/scripts/init_memory.py, .agents/skills/workspace-memory-skill/scripts/check_memory_language.py, .agents/skills/workspace-memory-skill/SKILL.md, tests/workspace-memory-skill/test_check_memory_language.py; next step: 后续新增 memory 时默认先读取 config.toml，并继续保持标题英文、正文按配置语言书写。
- 2026-03-25 [workspace-memory-query-boundary-fix]: Do not use recent.md source_ids as a global fallback evidence set for experience queries when no session matches the filter.; related files: .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_query_memory.py; next step: Continue improving richer ranking among multiple genuinely relevant derived candidates.
- 2026-03-25 [workspace-memory-derived-lineage]: Maintain source_ids and updated_at on recent and archive summaries through record_session.py and refine_memory.py.; related files: .agents/skills/workspace-memory-skill/scripts/memory_ops.py, .agents/skills/workspace-memory-skill/scripts/record_session.py, .agents/skills/workspace-memory-skill/scripts/refine_memory.py, .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_existing_scripts_smoke.py, tests/workspace-memory-skill/test_query_memory.py; next step: Improve richer ranking among multiple derived candidates after lineage signals are stable.
- 2026-03-25 [workspace-memory-query-automation]: Implement query_memory.py as a metadata-first layered retrieval CLI instead of a free-form search or answer synthesizer.; related files: .agents/skills/workspace-memory-skill/scripts/query_memory.py, tests/workspace-memory-skill/test_query_memory.py, .agents/skills/workspace-memory-skill/references/operations/query-memory.md; next step: Improve richer ranking and derived lineage after the first query CLI is stable.
- 2026-03-25 [workspace-memory-dogfood-query-foundation]: Promote the runtime-boundary and schema-scoped-maintenance rules into durable crystals.; related files: docs/memory/crystals/crystal-installable-skills-keep-runtime-only-payloads.md, docs/memory/crystals/crystal-workspace-memory-updates-stay-schema-scoped.md, docs/memory/summaries/topics/workspace-memory.md; next step: Design and implement a minimal metadata-first query_memory.py CLI next.
- 2026-03-25 [workspace-memory-maintenance-automation]: Add script-supported create/update flows for crystal and topic-summary memory files.; related files: .agents/skills/workspace-memory-skill/scripts/memory_ops.py, .agents/skills/workspace-memory-skill/scripts/update_crystal.py, .agents/skills/workspace-memory-skill/scripts/update_topic_summary.py, .agents/skills/workspace-memory-skill/references/operations/topic-summary-maintenance.md; next step: Use the new maintenance scripts when future workspace-memory sessions need durable knowledge extraction or topic aggregation.
- 2026-03-25 [workspace-memory-runtime-boundary]: Treat .agents/skills/<skill> as the runtime installation boundary and keep development-only tests at the repository root.; related files: .agents/skills/workspace-memory-skill/README.md, README.md, .gitignore, tests/workspace-memory-skill/test_runtime_layout.py; next step: Apply the same runtime-vs-development boundary to future skills added to this repository.
## Pending Follow-ups
- 后续可把 diagnostics 继续扩展到 false_positive 和 layer_hit 的 bucket 级分布，进一步提高回归定位效率。
- 后续如果引入 Agent/QA 基准，可复用同一套 bucket 诊断命名，减少 retrieval 与 QA 两层报告割裂。
- 下一步可接入真实固定 LLM adapter，并将 LoCoMo 数据转换接到现有内部 case schema。
- 后续可继续扩展 benchmark bucket，并让 analysis skill 产出更强的优化优先级建议。
- 后续新增 memory 时默认先读取 config.toml，并继续保持标题英文、正文按配置语言书写。
- Continue improving richer ranking among multiple genuinely relevant derived candidates.
- Improve richer ranking among multiple derived candidates after lineage signals are stable.
- Use the new maintenance scripts when future workspace-memory sessions need durable knowledge extraction or topic aggregation.
- Apply the same runtime-vs-development boundary to future skills added to this repository.
