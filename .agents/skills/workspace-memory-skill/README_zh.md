# Workspace Memory Skill

本文档面向这个 skill 的维护者，不用于运行时路由。运行时入口仍然是 [`SKILL.md`](./SKILL.md)。

## 这个 Skill 是什么

`workspace-memory-skill` 是一个面向共享工作区上下文的 repo-local memory 工作流。它面向的是在单个仓库或工作区内与 agent 协作的小团队，这类场景中的主要问题不是信息缺失，而是缺少可持续、可检索、结构化的长期记忆。

这个 skill 的定位，有意比通用的 “agent memory platform” 更窄。它聚焦于：

- 存储在工作区中的 Markdown-first memory
- 由脚本生成的元数据
- 针对 recent、archive 和 crystallized knowledge 的分层记忆
- 用于降低上下文成本的渐进式检索

## 设计演化链路

这个设计经历了几轮逐步收窄：

1. 通用 memory 想法
   最初的出发点，是一个通用的 AI memory 能力，用于保存会话、摘要和长期知识。

2. 工作区范围的 memory
   之后方向收窄到单个工作区，因为真正的痛点是在一个共享项目里反复解释背景、决策依据丢失，以及理解不一致。

3. Repo-local Markdown
   第一版设计刻意避开了外部存储和向量基础设施。首要目标是让团队更容易采用、内容可检查、工作流摩擦更低。

4. 分层 memory
   记忆模型被拆分为：
   - 用于一手记录的 session memory
   - 用于活跃上下文的 recent summary
   - 用于压缩历史的 archive summary
   - 用于沉淀长期知识的 crystals

5. 渐进式检索
   预期流程不再是“全部读完”，而是：
   - 先读 generated summary 或导航层
   - 再读 topic 或 crystal 层
   - 只有必要时才回看 source session

6. 脚本拥有的元数据
   早期设计中，模板更直接地暴露 frontmatter。后来这一点被收紧，变成尽可能把 metadata 视为 system-owned，而 agent 主要聚焦语义输入和正文内容。

7. 路由层加操作卡
   `SKILL.md` 被收敛成路由层。每个操作的详细说明被移动到 `references/operations/` 中，这样 agent 可以看到：
   - 什么时候该用某个操作
   - 应该调用哪个脚本
   - 需要哪些参数
   - 对应使用哪个正文模板

## 核心理念

这个 skill 受到几个约束的指导：

- 元数据应该稳定
  如果检索依赖 metadata，那 metadata 就不能随意漂移。应优先让脚本来生成它。

- 正文应保持可读
  这些 memory 文件应该仍然是可阅读的 Markdown 文档，而不只是机器记录。

- 原始来源与派生视图应保持分离
  Session 文件是 source。Recent summaries、archive summaries，以及可选的导航文件都是 derived views。

- 检索应该是渐进式的
  Agent 不应读取超过必要范围的内容。

- 避免过早的平台化设计
  第一版的目标并不是变成一个通用知识图谱、向量数据库，或多工作区 memory 服务。

## 当前工作模型

### Memory 类别

- `session`
  某个具体会话或工作时段的一手记录。

- `generated-summary`
  由脚本维护的视图，例如 `recent.md`。

- `archive-summary`
  对较旧记忆的压缩历史视图。

- `topic-summary`
  主题级聚合摘要。

- `crystal`
  应当影响后续工作的长期知识。

### Crystal 知识类型

当前 crystals 使用 `knowledge_type`，而不是 `crystal_type`，这样模型会更通用：

- `rule`
- `decision`
- `pattern`
- `insight`

这样可以让 crystals 不只适用于纯编码偏好，也能支持更一般化的工作区知识。

### 元数据归属

当前规则是：

- 能由脚本生成或更新 metadata 的地方，尽量由脚本完成
- templates 主要负责描述正文结构
- schema 规则定义在 `references/schema.md`

## 文件布局

主要的运行时组成部分包括：

- `SKILL.md`
  运行时入口和路由层

- `references/schema.md`
  元数据规则

- `references/templates.md`
  模板导航

- `references/templates/`
  每种 memory type 的 body-first 模板

- `references/operations/`
  把用户意图连接到脚本和模板的操作卡

- `scripts/`
  用于初始化、记录 session 和 recent-memory refinement 的确定性辅助脚本

## 工作流模型

### 1. 初始化 memory

这个 skill 使用 `scripts/init_memory.py` 来创建 memory tree，并生成初始的派生文件。

### 2. 记录一次 session

这个 skill 使用 `scripts/record_session.py` 来：

- 创建 session 文件路径
- 生成 session metadata
- 更新 `summaries/recent.md`

agent 应该聚焦于：

- topic
- 与 summary 相关的内容
- 决策、理由、变更、后续事项、crystallization 候选项

### 3. 整理 recent memory

这个 skill 使用 `scripts/refine_memory.py` 来：

- 保持 recent memory 规模较小
- 把较旧的 recent 项移动到 archive history
- 收缩待处理 follow-ups，使其与保留的活跃上下文相匹配

### 4. 查询 memory

目前还没有专门的 query 脚本。当前查询主要依赖 reference-driven 的方式，按照操作卡和查询参考文档里描述的分层读取顺序执行。

### 5. 维护 crystals

Crystal 的创建和维护目前仍然是手工的。未来预期的方向，是也为 crystals 的 metadata 生成提供脚本支持。

## 为什么 `index.md` 仍然存在

这个设计已经不再把 `index.md` 视为一个权威的、手工维护的文件。

当前立场是：

- `index.md` 是可选的，并且应由生成过程产出
- 它作为一个面向人类的导航页仍然有用
- 它不应当是真正的权威来源

真正的权威来源，是那组带结构化 metadata 的 typed memory files。

## 当前自动化边界

已实现：

- `scripts/init_memory.py`
- `scripts/record_session.py`
- `scripts/refine_memory.py`

已部分设计、但尚未完整实现：

- crystal creation script
- topic summary generation script
- 基于 metadata-first retrieval 的 query script
- 更强的 derived files source tracking

## 当前已知缺口

这些部分目前还没有完成：

1. Query automation
   检索仍由 references 引导，而不是由专门的 query script 完成。

2. Crystal write path
   Crystals 已经有 schema 和 template，但还没有专门的创建 / 更新脚本。

3. Topic summaries
   Topic summaries 已经有 template，但还没有持续维护的生成流程。

4. Derived-file freshness
   `recent.md` 和 `archive.md` 会由现有脚本更新，但更广泛的派生索引还没有建立。

5. Source lineage completeness
   某些派生文件在概念上定义了 `source_ids`，但并不是所有更新路径都会维护它们。

6. 既有 memory 的迁移
   当前脚本更偏向新建或轻度结构化的 memory，而不是从任意现有笔记批量迁移。

## 当前的非目标

这个 skill 目前有意不做这些事情：

- 外部向量存储
- 跨工作区的 memory federation
- 自动语义排序
- 复杂图存储
- 强制要求人工维护的 index 文件

## 建议的下一步

如果这个 skill 继续演进，最自然的下一步包括：

1. 添加 crystal 创建 / 更新脚本
   这样可以让 crystal metadata 和 sessions 一样受到同样的约束。

2. 添加 query script
   这样 agent 就可以请求快照、过滤检索以及相关 memory，而不需要手工遍历。

3. 添加 topic-summary generation
   这样可以减少主题汇总的手工工作。

4. 改进 derived lineage
   让 archive 和 summary 生成路径中的 `source_ids` 保持准确。

## 未来变更的工作原则

在新增字段、文件或脚本之前，优先先问：

- 这是否减少了检索中的歧义
- 这是否减少了维护负担
- 这是否可以被机械性约束
- 这在现在是否必要，还是只是理论上有用

如果答案大多停留在理论层面，这个改动大概率就应该先等等。
