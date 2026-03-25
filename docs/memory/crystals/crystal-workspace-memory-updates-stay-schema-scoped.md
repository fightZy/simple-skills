---
id: 'crystal:workspace-memory-updates-stay-schema-scoped'
memory_type: crystal
title: 'Workspace memory updates stay schema-scoped'
summary: 'Scripted maintenance should update only known metadata fields and canonical sections instead of patching Markdown freely.'
created_at: 2026-03-25
updated_at: 2026-03-25
knowledge_type: pattern
source_ids:
  - 'session:2026-03-25:workspace-memory-maintenance-automation'
tags:
  - 'workspace-memory'
  - 'automation'
applies_to:
  - 'docs/memory/**'
---

# Crystal: Workspace memory updates stay schema-scoped

## Statement
- Workspace-memory maintenance scripts should operate at metadata and known-section granularity.
- Missing sections inserted during maintenance should follow canonical section order.

## Why It Matters
- Schema-scoped updates are safer to test than free-form document rewrites.
- Stable structure gives later query and maintenance automation a predictable target.

## When To Apply
- When adding new maintenance scripts or evolving typed memory files.

## Provenance
- session:2026-03-25:workspace-memory-maintenance-automation

## Notes
- Do not expand into generic Markdown patching unless retrieval requirements clearly justify it.
