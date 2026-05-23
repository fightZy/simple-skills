# Dispatching Code Review Subagents

本文档面向这个 skill 的维护者，不用于运行时路由。运行时入口仍然是 `SKILL.md`。

## 这个 Skill 是什么

`dispatching-code-review-subagents` 是一个轻量的 code review 派发 skill，用来判断如何把 review 任务交给 subAgent。

它的目标是让 agent：

- 判断一次 review 应该由单个 reviewer、多个主题 reviewer，还是分层 reviewer 完成
- 按风险主题拆分 review，而不是机械按文件数量拆分
- 给每个 reviewer 明确的范围、风险视角和输出格式
- 汇总 reviewer 结果时只做去重、排序、冲突和缺口标注，不再完整复审一遍

## 用途

在把 code review 派发给 subAgent 前使用这个 skill，尤其适用于实现里程碑之后，或复杂变更合并前。

这个 skill 不负责：

- 修复 review 发现的问题
- 替代常规 code review 输出格式
- 为小型局部 diff 强行启用多个 subAgent

## 设计原则

- 成本敏感：只有额外 reviewer 能提高信号时才拆分。
- 主题优先：按 contract、data、security、tests、UI、maintainability 等独立风险视角拆分。
- 可并发则并发：互不依赖的 review 主题并行执行。
- 必要时分层：只有第一层发现会影响第二层 review 时才做顺序分层。
- 主 Agent 只做综合：负责回收、去重、排序和标注缺口，不重复逐行复审。

## 验证

好的验证场景应检查这个 skill 是否能：

- 对小型局部 diff 选择单个 reviewer
- 对跨多领域变更选择多个主题 reviewer 并发
- 只在后续 review 依赖前一层发现时选择分层
- 让主 Agent 聚焦在派发与综合，而不是重新完整 review
