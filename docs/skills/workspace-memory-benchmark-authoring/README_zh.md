# Workspace Memory Benchmark Authoring

本文档面向这个 skill 的维护者，不用于运行时路由。运行时入口仍然是 `SKILL.md`。

## 这个 Skill 是什么

`workspace-memory-benchmark-authoring` 是 `workspace-memory-skill` 的配套 skill。它用于指导 agent 如何扩展仓库内自建 benchmark fixtures，同时避免把“写样例”和“改检索实现”混在一起。

## 用途

当任务是为下面目录新增或调整 benchmark case 时使用：

- `tests/workspace-memory-skill/benchmark_fixtures/`

目标是补真实、可回归的检索覆盖，而不是堆砌样例数量。

## 设计原则

- 一个 fixture 只测一个检索行为。
- fixture 要模拟可信的分层 memory tree。
- 可以用 subagent 起草 fixture，但只能改 fixture 目录。
- 主代理负责本地 review 和最终验证。
- benchmark fixture 应该让回归更容易暴露，而不是更容易被掩盖。

## 与 Workspace Memory 的关系

这个 skill 依赖 `workspace-memory-skill` 的 benchmark harness 和真实检索行为，但它本身不是运行时 memory workflow 的一部分。它存在的目的，是让 benchmark 样例编写成为清晰、可发现、可约束的能力。

## 验证

常用验证命令：

- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`
- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`
