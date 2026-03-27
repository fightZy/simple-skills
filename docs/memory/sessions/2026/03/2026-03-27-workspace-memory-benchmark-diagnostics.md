---
id: 'session:2026-03-27:workspace-memory-benchmark-diagnostics'
memory_type: session
title: 'workspace-memory-benchmark-diagnostics'
summary: '将 expected_top_hit、forbidden_hit 和被 limit 裁掉的强候选类型纳入 benchmark 报告，而不是只看聚合通过率。'
session_date: 2026-03-27
created_at: 2026-03-27
updated_at: 2026-03-27
tags:
  - 'workspace-memory'
  - 'benchmark'
  - 'diagnostics'
---

# Session: workspace-memory-benchmark-diagnostics

## Goal
增强 workspace-memory retrieval benchmark 的诊断输出，让回归时更快定位排序、噪声和 limit 截断问题。

## Key Decisions
- 将 expected_top_hit、forbidden_hit 和被 limit 裁掉的强候选类型纳入 benchmark 报告，而不是只看聚合通过率。
- 保持现有 fixture schema 不变，把诊断逻辑收敛在 runner 的 case 级补充查询和 bucket 级汇总里。

## Rationale
- 回归时仅看 pass/fail 无法快速判断是 top 排序错、forbidden 噪声泄漏，还是强候选被 limit 挤掉。
- 把诊断信息放在 runner 汇总层，可以增强可观测性，而不需要改 query_memory CLI 契约或重写 fixture。

## Changes
- 在 scripts/benchmarks/workspace_memory/runner.py 中增加 case 级 diagnostics，输出 trimmed_strong_candidate_ids 和 trimmed_strong_candidate_types。
- 在 bucket_summary 中聚合 expected_top_hit_cases、forbidden_hit_cases，以及按类型统计的 trimmed strong candidates。
- 在 tests/workspace-memory-skill/test_workspace_memory_benchmark.py 中补充红绿测试，覆盖诊断字段与 bucket 汇总合同。

## Open Questions
- None

## Follow-up
- 后续可把 diagnostics 继续扩展到 false_positive 和 layer_hit 的 bucket 级分布，进一步提高回归定位效率。
- 后续如果引入 Agent/QA 基准，可复用同一套 bucket 诊断命名，减少 retrieval 与 QA 两层报告割裂。

## Crystallization Candidates
- Workspace-memory benchmark 应输出 bucket 级 expected_top_hit、forbidden_hit 与 trimmed strong candidate 诊断，方便 retrieval 回归定位。


## Related Files
- scripts/benchmarks/workspace_memory/runner.py
- tests/workspace-memory-skill/test_workspace_memory_benchmark.py