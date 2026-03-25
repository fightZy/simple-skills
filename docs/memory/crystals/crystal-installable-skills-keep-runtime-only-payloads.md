---
id: 'crystal:installable-skills-keep-runtime-only-payloads'
memory_type: crystal
title: 'Installable skills keep runtime-only payloads'
summary: 'Treat .agents/skills/<skill> as the runtime boundary and keep development-only tests at the repository root.'
created_at: 2026-03-25
updated_at: 2026-03-25
knowledge_type: rule
source_ids:
  - 'session:2026-03-25:workspace-memory-runtime-boundary'
tags:
  - 'workspace-memory'
  - 'repo-structure'
applies_to:
  - '.agents/skills/*'
---

# Crystal: Installable skills keep runtime-only payloads

## Statement
- Installable skill directories should contain only runtime assets.
- Development-only tests belong at the repository root, not inside the shipped skill directory.

## Why It Matters
- Directory boundaries are the most reliable packaging boundary in this repository.
- Keeping tests out of runtime payloads reduces accidental install bloat and layout drift.

## When To Apply
- When adding a new skill or moving files across runtime and development boundaries.

## Provenance
- session:2026-03-25:workspace-memory-runtime-boundary

## Notes
- Assert the boundary with a regression test when restructuring skill contents.
