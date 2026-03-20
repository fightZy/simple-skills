---
name: workspace-memory-skill
description: Use when the task involves creating, maintaining, or querying repo-local workspace memory for a project. This skill organizes team-shared agent memory as Markdown files under the current workspace, captures session summaries, maintains layered memory indexes, crystallizes durable team conventions and design rationale, and retrieves memory progressively to reduce context and token cost.
---

# Workspace Memory Skill

## Overview

This skill manages project memory inside the current workspace as Markdown files. It is for small-team workflows where agents and developers need shared, durable context without turning the repo into an unstructured dump of transcripts.

Prefer script-generated metadata. The agent should focus on semantic inputs and body content, not on hand-writing frontmatter.

Read [references/layout.md](references/layout.md) for the memory tree.
Read [references/templates.md](references/templates.md) for schema and body-template navigation.

## Routing

Pick the narrowest operation that matches the request:

- Initialize workspace memory:
  Read [references/operations/initialize-memory.md](references/operations/initialize-memory.md)
- Record a new session:
  Read [references/operations/session-capture.md](references/operations/session-capture.md)
- Compress recent memory into archive:
  Read [references/operations/refine-recent.md](references/operations/refine-recent.md)
- Query existing memory:
  Read [references/operations/query-memory.md](references/operations/query-memory.md)
- Maintain or deduplicate memory:
  Read [references/maintenance.md](references/maintenance.md)
- Extract durable knowledge:
  Read [references/operations/crystal-maintenance.md](references/operations/crystal-maintenance.md)

## Core Rules

- Keep memory `repo-local` and Markdown-first.
- Treat structured metadata as system-owned fields. Generate or update them through scripts whenever possible.
- Treat body sections as content-owned fields. The agent should focus on the actual summary, rationale, decisions, and follow-ups.
- Prefer updating existing files over creating near-duplicates.
- Do not invent unsupported scripts. If an operation card says the flow is currently manual, follow the manual flow.
- Use script `--help` output as the final parameter contract when there is any ambiguity.

## Current Automation Boundary

Script-supported today:
- initialization via `scripts/init_memory.py`
- session capture via `scripts/record_session.py`
- recent-to-archive compression via `scripts/refine_memory.py`

Manual or partial today:
- query routing is still reference-driven
- crystal creation and updates are still manual
- topic-summary generation is still manual

## Expected Outputs

Common outputs for this skill are:
- a new or updated memory directory under the current workspace
- one or more session files with script-generated metadata
- updated recent or archived summaries
- updated crystal or topic-summary files when the task requires durable knowledge extraction

Use file paths in your response when you create or update memory files.
