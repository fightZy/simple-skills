# OpenSpec Superpower Orchestration

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`openspec-superpower-orchestration` is the orchestration entrypoint for formal change work that uses OpenSpec artifacts plus superpower skills together.

It is designed to make an agent:

- coordinate exploration, formal artifacts, implementation, review, and verification in a single stable workflow
- keep OpenSpec artifacts as the only formal source of truth (no parallel planning systems)
- apply superpower skills as discipline layers at the right phases without conflict
- enforce approval gates, milestone reviews, and verification before declaring completion

## Purpose

Use this skill when the work involves:

- a new feature, bugfix, refactor, or behavior change that needs formal spec artifacts
- changes that alter business capability, user-visible flows, API or protocol contracts, state semantics, cross-module architecture, or persisted data shape
- multi-skill coordination where exploration, design, implementation, and verification need one ordering discipline
- formal changes where `proposal.md`, `design.md`, `spec.md`, `tasks.md`, or implementation orchestration are required

Do not use for:

- tiny one-off answers with no formal change
- pure explanation work with no artifact or implementation follow-up
- local implementation-only improvements that do not change requirement semantics (style tweaks, component splitting, performance optimization, test coverage hardening)

## Design Principles

- OpenSpec artifacts are the single source of truth. No parallel proposal/design/tasks system.
- Discovery before artifacts: do not write specs until key decisions are stable.
- Prefer the lightest workflow that still preserves clarity and correctness.
- Workflow cost must not exceed implementation cost. Process serves progress.
- Superpower skills are discipline layers, not competing artifact systems.
- Unresolved open questions are artifact-readiness blockers by default.

## Workflow Summary

The skill orchestrates seven phases:

1. **Clarify stage** -- explore with `brainstorming` or `openspec-explore` if scope is unstable; confirm key decisions before creating artifacts.
2. **Apply local overrides** -- repo-level `AGENTS.md` or `CLAUDE.md` takes priority over generic defaults.
3. **Draft formal specs** -- once scope is stable, write `proposal.md`, `design.md`, and `spec.md` in `openspec/changes/<change-name>/`.
4. **Present full draft** -- show the complete draft at once for user review (no section-by-section approval).
5. **Create tasks** -- after user approves the draft, write `tasks.md`. Only create `plan.md` when execution orchestration is genuinely needed.
6. **Self-review** -- check for placeholders, contradictions, scope drift, and spec-to-task traceability.
7. **Enter implementation** -- use `openspec-apply-change`, `executing-plans`, or `subagent-driven-development` as appropriate.

## Dependencies

This skill depends on two layers:

- **OpenSpec artifact system**: `openspec/changes/<change-name>/` holds `proposal.md`, `design.md`, `spec.md`, `tasks.md`, and optional `plan.md`.
- **Superpower skills**:
  - Exploration: `brainstorming`, `openspec-explore`
  - Implementation entry: `openspec-apply-change`
  - Discipline layers: `test-driven-development`, `executing-plans`, `subagent-driven-development`
  - Quality gates: `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `openspec-verify-change`

This skill does not replace those skills. It defines when to use them, in what order, and which artifact system remains authoritative.

## Relationship To Other Skills

- `brainstorming` is for exploration, not the final artifact sequence.
- `openspec-explore` is for open investigation or reframing.
- `openspec-apply-change` is for implementation after approved tasks exist.
- `executing-plans` or `subagent-driven-development` are optional discipline layers, not replacements for `tasks.md`.
- Repo-local `AGENTS.md` or `CLAUDE.md` may tighten or narrow this workflow; those are higher-priority supplements.

## Verification

Typical verification should check:

- formal change requests result in OpenSpec artifacts under `openspec/changes/`, not ad-hoc docs
- discovery/brainstorming happens before artifact creation when scope is unstable
- user confirmation gates are enforced before moving between phases
- `tasks.md` stays updated as implementation progresses
- `verification-before-completion` runs before any completion claim
- archive conflicts are resolved explicitly, not carried forward unresolved
