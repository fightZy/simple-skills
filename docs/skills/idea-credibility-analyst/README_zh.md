# Idea Credibility Analyst

`Idea Credibility Analyst` 是一个用于评估产品、创业、功能或工作流想法是否值得继续推进的可复用 skill。

## 功能介绍

这个 skill 的目标，是把模糊的“想法讨论”收敛成一份结构化的可行性判断。

它会引导 agent：

- 通过聚焦式对话澄清想法
- 调研竞品、开源项目和社区讨论
- 从定位、成熟度、优势和空白机会等角度比较替代方案
- 判断赛道拥挤程度
- 给出 `continue`、`pivot` 或 `stop` 的结论

## 能力特性

这个 skill 强调的是有证据的判断，而不是迎合式建议。

- 聚焦澄清
  一次只问一个高价值问题，而不是抛出一整套大问卷。
- 基于当前证据调研
  优先查看官网、文档、代码仓库、版本记录和近期社区讨论。
- 结构化竞品比较
  不只列名字，而是比较目标用户、定位、成熟度和差异点。
- 拥挤度判断
  判断市场是 `uncrowded`、`moderately crowded`、`crowded` 还是 `hyper-competitive`。
- 明确结论输出
  最终必须给出结论和理由，而不是停留在模糊建议。

## 使用场景

当用户需要严谨的 go / no-go 判断，而不是泛泛 brainstorming 时，适合使用这个 skill。

常见场景包括：

- 评估一个创业或 SaaS 想法是否值得做
- 判断某个功能方向是否有足够差异化
- 在正式开发前验证一个自动化工作流思路
- 分析一个想法是否有清晰切入口，还是已经过于拥挤

常见问题包括：

- 这个想法是不是已经太拥挤了？
- 现在有哪些产品在解决同类问题？
- 这个方向最合理的切入点是什么？
- 这个想法应该继续、转向，还是停止？

## 目录内容

- [`SKILL.md`](../../../.agents/skills/idea-credibility-analyst/SKILL.md)：主 skill 说明
- [`README.md`](./README.md)：英文介绍
- [`agents/openai.yaml`](../../../.agents/skills/idea-credibility-analyst/agents/openai.yaml)：agent 元数据
- [`references/interview-playbook.md`](../../../.agents/skills/idea-credibility-analyst/references/interview-playbook.md)：访谈引导
- [`references/rubric.md`](../../../.agents/skills/idea-credibility-analyst/references/rubric.md)：评估标准
- [`references/report-template.md`](../../../.agents/skills/idea-credibility-analyst/references/report-template.md)：输出模板

## 说明

这个文件是中文介绍页，实际运行规则仍以 [`SKILL.md`](../../../.agents/skills/idea-credibility-analyst/SKILL.md) 为准。
