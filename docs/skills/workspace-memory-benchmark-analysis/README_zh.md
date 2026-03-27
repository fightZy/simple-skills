# Workspace Memory Benchmark Analysis

本文档面向这个 skill 的维护者，不用于运行时路由。运行时入口仍然是 `SKILL.md`。

## 这个 Skill 是什么

`workspace-memory-benchmark-analysis` 是 `workspace-memory-skill` 的配套 skill。它用于指导 agent 运行 benchmark、分类检索失败模式，并把评测结果转成具体的优化建议。

## 用途

当用户希望：

- 运行 workspace-memory benchmark
- 理解某个 benchmark case 为什么失败
- 将失败映射回 ranking、lineage 或 fallback 行为
- 决定下一步该优化哪一块检索逻辑

时，使用这个 skill。

## 设计原则

- 评测结果要按 bucket 读取，而不只是看总通过率。
- 失败应映射到可能原因，而不是只报原始分数。
- 真实 query script 输出里的 `reason` 是重要证据。
- 建议应尽量小、可验证、可回归。

## 与 Workspace Memory 的关系

这个 skill 依赖 `workspace-memory-skill` 的 benchmark harness 和真实检索行为，但关注点是诊断与优化建议，而不是写样例或执行 memory authoring。

## 验证

常用验证命令：

- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`
- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`
