---
id: 'session:2026-03-27:workspace-memory-benchmark-companions'
memory_type: session
title: 'workspace-memory-benchmark-companions'
summary: '新增 retrieval benchmark harness，先支持 repo 自建样例，再为固定 LLM QA 与 LoCoMo 适配保留边界。'
session_date: 2026-03-27
created_at: 2026-03-27
updated_at: 2026-03-27
tags:
  - 'workspace-memory'
  - 'benchmark'
  - 'skills'
---

# Session: workspace-memory-benchmark-companions

## Goal
为 workspace-memory 建立可持续扩展的 benchmark 工作流，并将样例编写与结果分析沉淀为两个配套 skill。

## Key Decisions
- 新增 retrieval benchmark harness，先支持 repo 自建样例，再为固定 LLM QA 与 LoCoMo 适配保留边界。
- 将 benchmark 工作流拆为两个配套 skill：一个负责新增样例，一个负责运行并解读评测结果。
- 为 benchmark case 增加 bucket 和 forbidden_candidate_ids，使结果可以按失败类型聚合并辅助优化 retrieval。

## Rationale
- 将样例编写与评测分析拆开，可以让 agent 更稳定地选择正确流程，同时避免主 workspace-memory runtime skill 变得臃肿。
- bucket 化输出比单一总通过率更适合作为 retrieval 优化信号。

## Changes
- 新增 scripts/benchmarks/workspace_memory 下的数据集、计分、runner、QA adapter、LoCoMo adapter 与 bucket 聚合能力。
- 新增 tests/workspace-memory-skill/benchmark_fixtures 自建样例，并为 current-state、lineage、norms-ordering、negative、exact-id 建立覆盖。
- 新增 workspace-memory-benchmark-authoring 与 workspace-memory-benchmark-analysis 两个配套 skill 及其中英文维护文档。

## Open Questions
- None

## Follow-up
- 下一步可接入真实固定 LLM adapter，并将 LoCoMo 数据转换接到现有内部 case schema。
- 后续可继续扩展 benchmark bucket，并让 analysis skill 产出更强的优化优先级建议。

## Crystallization Candidates
- Benchmark 样例编写与结果分析应分成两个配套 skill，避免 workspace-memory 主 skill 混入维护流程。
- Workspace-memory benchmark 输出应按 bucket 聚合，并显式标注 forbidden candidates，才能稳定辅助 retrieval 优化。


## Related Files
- scripts/benchmarks/workspace_memory/dataset.py
- scripts/benchmarks/workspace_memory/runner.py
- tests/workspace-memory-skill/test_workspace_memory_benchmark.py
- .agents/skills/workspace-memory-benchmark-authoring/SKILL.md
- .agents/skills/workspace-memory-benchmark-analysis/SKILL.md

## Related References
- docs/plans/2026-03-27-workspace-memory-benchmark-design.md
- docs/plans/2026-03-27-workspace-memory-benchmark-companions-design.md