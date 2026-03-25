---
id: 'session:2026-03-25:workspace-memory-runtime-boundary'
memory_type: session
title: 'workspace-memory-runtime-boundary'
summary: 'Treat .agents/skills/<skill> as the runtime installation boundary and keep development-only tests at the repository root.'
session_date: 2026-03-25
created_at: 2026-03-25
updated_at: 2026-03-25
tags:
  - 'workspace-memory'
  - 'repo-structure'
---

# Session: workspace-memory-runtime-boundary

## Goal
Keep installable skill payloads limited to runtime assets and capture the completed workspace-memory restructure.

## Key Decisions
- Treat .agents/skills/<skill> as the runtime installation boundary and keep development-only tests at the repository root.

## Rationale
- The repo has no separate packaging exclusion layer, so directory boundaries are the most reliable way to keep non-runtime files out of installed skills.

## Changes
- Moved workspace-memory-skill tests from .agents/skills/workspace-memory-skill/tests to tests/workspace-memory-skill and updated test path resolution to target the runtime scripts explicitly.
- Added a runtime layout regression test to assert that workspace-memory-skill no longer contains a tests directory.
- Updated the skill README, repository README, and .gitignore to document the runtime boundary and ignore pytest cache output.

## Open Questions
- None

## Follow-up
- Apply the same runtime-vs-development boundary to future skills added to this repository.

## Crystallization Candidates
- Installable skill directories should contain only runtime assets; development-only tests belong at the repository root.


## Related Files
- .agents/skills/workspace-memory-skill/README.md
- README.md
- .gitignore
- tests/workspace-memory-skill/test_runtime_layout.py

## Related References
- commit:80c529a