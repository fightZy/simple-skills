---
id: 'session:2026-03-25:workspace-memory-language-config'
memory_type: session
title: 'workspace-memory-language-config'
summary: '用 docs/memory/config.toml 的 content_language 控制正文语言，缺省回退为英文。'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'language-policy'
---

# Session: workspace-memory-language-config

## Goal
统一 workspace memory 的正文语言控制，保留 ASCII 文件名和英文标题。

## Key Decisions
- 用 docs/memory/config.toml 的 content_language 控制正文语言，缺省回退为英文。
- 保留英文标题和 ASCII 文件名，不引入 locale 渲染或 section key 映射。

## Rationale
- 这样可以避免改动现有脚本的 section 匹配逻辑，把成本收敛在初始化配置、文档约束和校验脚本。

## Changes
- init_memory.py 新增 --content-language 并生成 docs/memory/config.toml。
- 新增 check_memory_language.py，用于校验英文标题约束和明显的语言策略违规。
- 补充 workspace-memory-skill 文档、配置说明和回归测试。

## Open Questions
- None

## Follow-up
- 后续新增 memory 时默认先读取 config.toml，并继续保持标题英文、正文按配置语言书写。

## Crystallization Candidates
- 正文语言由 docs/memory/config.toml 的 content_language 驱动，标题和文件名保持稳定英文/ASCII。


## Related Files
- docs/memory/config.toml
- .agents/skills/workspace-memory-skill/scripts/init_memory.py
- .agents/skills/workspace-memory-skill/scripts/check_memory_language.py
- .agents/skills/workspace-memory-skill/SKILL.md
- tests/workspace-memory-skill/test_check_memory_language.py