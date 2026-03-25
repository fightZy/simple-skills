---
id: 'crystal:workspace-memory-content-language-is-config-driven'
memory_type: crystal
title: 'Workspace memory content language is config-driven'
summary: 'Use docs/memory/config.toml to control body language while keeping headings and filenames stable.'
created_at: 2026-03-25
updated_at: 2026-03-25
knowledge_type: rule
source_ids:
  - 'session:2026-03-25:workspace-memory-language-config'
tags:
  - 'workspace-memory'
  - 'language-policy'
applies_to: []
---

# Crystal: Workspace memory content language is config-driven

## Statement
- 正文语言由 docs/memory/config.toml 中的 content_language 控制。
- 标题保持脚本既定英文形式，文件名保持 ASCII。

## Why It Matters
- 这样可以避免修改现有的 section 匹配和更新逻辑。
- 语言策略变成 repo-local 配置后，后续 session 和维护动作更稳定。

## When To Apply
- 初始化新的 memory 树时，根据当前用户对话语言写入 content_language。
- 后续记录 session、crystal、topic summary 时，正文遵循配置语言。

## Provenance
- session:2026-03-25:workspace-memory-language-config

## Notes
- 第一版不引入 locale 渲染，也不把 section 标题本地化。
