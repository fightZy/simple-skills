# OpenSpec Superpower Orchestration

本文档面向这个 skill 的维护者，不用于运行时路由。运行时入口仍然是 `SKILL.md`。

## 这个 Skill 是什么

`openspec-superpower-orchestration` 是正式变更工作的编排入口，将 OpenSpec 产物体系与 superpower skill 体系统一协调使用。

它的目标是让 agent：

- 在一个稳定的工作流中协调探索、正式产物、实现、评审和验证
- 将 OpenSpec 产物作为唯一正式的事实来源（不产生平行规划系统）
- 在正确阶段应用 superpower skill 作为纪律层，避免冲突
- 强制执行审批关卡、里程碑评审和完成前验证

## 用途

当工作涉及以下场景时使用此 skill：

- 需要正式规格产物的新功能、Bug 修复、重构或行为变更
- 改变业务能力、用户可见流程、API 或协议契约、状态语义、跨模块架构或持久化数据结构的变更
- 需要多个 skill 协调、探索/设计/实现/验证需要统一排序纪律的情况
- 需要 `proposal.md`、`design.md`、`spec.md`、`tasks.md` 或实现编排的正式变更

不适用于：

- 无正式变更的简短回答
- 无产物或后续实现的纯解释性工作
- 不改变需求语义的本地实现优化（样式调整、组件拆分、性能优化、测试覆盖加固）

## 设计原则

- OpenSpec 产物是唯一事实来源，不产生平行的 proposal/design/tasks 系统。
- 先发现、后产物：在关键决策稳定之前不写规格。
- 优先选择最轻量的工作流，但仍须保持清晰和正确。
- 工作流成本不应超过实现成本。流程服务于进展。
- Superpower skill 是纪律层，不是竞争性的产物系统。
- 未解决的开放问题默认是产物就绪的阻塞项。

## 工作流概要

此 skill 编排七个阶段：

1. **明确阶段** -- 如果范围不稳定，用 `brainstorming` 或 `openspec-explore` 进行探索；在创建产物前确认关键决策。
2. **应用本地覆盖** -- 仓库级 `AGENTS.md` 或 `CLAUDE.md` 优先于通用默认值。
3. **起草正式规格** -- 范围稳定后，在 `openspec/changes/<change-name>/` 下写 `proposal.md`、`design.md` 和 `spec.md`。
4. **一次性展示完整草案** -- 供用户整体评审（不逐节审批）。
5. **创建任务** -- 用户批准草案后写 `tasks.md`。仅在真正需要执行编排时才创建 `plan.md`。
6. **自审** -- 检查占位符、矛盾、范围漂移、规格到任务的可追溯性。
7. **进入实现** -- 视情况使用 `openspec-apply-change`、`executing-plans` 或 `subagent-driven-development`。

## 依赖

此 skill 依赖两个层次：

- **OpenSpec 产物体系**：`openspec/changes/<change-name>/` 存放 `proposal.md`、`design.md`、`spec.md`、`tasks.md` 和可选的 `plan.md`。
- **Superpower skill**：
  - 探索：`brainstorming`、`openspec-explore`
  - 实现入口：`openspec-apply-change`
  - 纪律层：`test-driven-development`、`executing-plans`、`subagent-driven-development`
  - 质量关卡：`requesting-code-review`、`receiving-code-review`、`verification-before-completion`、`openspec-verify-change`

此 skill 不替代这些 skill，而是定义何时使用它们、以何种顺序使用、以及哪个产物体系保持权威。

## 与其他 Skill 的关系

- `brainstorming` 用于探索，不是最终产物序列。
- `openspec-explore` 用于开放调查或重新框定。
- `openspec-apply-change` 用于已批准任务存在后的实现。
- `executing-plans` 或 `subagent-driven-development` 是可选纪律层，不替代 `tasks.md`。
- 仓库本地的 `AGENTS.md` 或 `CLAUDE.md` 可收紧或缩窄此工作流，其优先级更高。

## 验证

典型验证应检查：

- 正式变更请求产生的是 `openspec/changes/` 下的 OpenSpec 产物，而非临时文档
- 当范围不稳定时，在产物创建之前先进行发现/脑暴
- 阶段之间的用户确认关卡被强制执行
- `tasks.md` 随实现进展持续更新
- 在任何完成声明之前运行 `verification-before-completion`
- 归档冲突被显式解决，而非遗留为未解决状态
