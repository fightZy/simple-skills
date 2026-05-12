---
name: openspec-superpower-orchestration
description: Use when a non-trivial change should follow an OpenSpec-plus-superpower workflow with formal specs, approval gates, implementation discipline, and no parallel planning system
---

# OpenSpec Superpower Orchestration

## Overview

This skill is the orchestration entrypoint for formal change work that uses `OpenSpec` plus superpower skills.

Use it when generic skill defaults are too local or too phase-specific, and you need one workflow that coordinates exploration, formal artifacts, implementation, review, and verification without creating a second source of truth.

Its purpose is to improve workflow quality: keep sequencing stable, reduce process loops, and ensure `OpenSpec` artifacts and superpower discipline layers work together instead of competing.

## When to Use

- New feature, bugfix, refactor, or behavior change
- Formal changes that alter business capability, user-visible flows, API or protocol contracts, state semantics, cross-module architecture, or persisted data shape
- The work needs `proposal`, `design`, `spec`, `tasks`, or implementation orchestration
- Multiple skills may apply, but they need one ordering discipline
- You want `OpenSpec` artifacts to remain the only formal source of truth

Do not use for:

- Tiny one-off answers with no formal change
- Pure explanation work with no artifact or implementation follow-up
- Local implementation-only improvements that do not change requirement semantics, such as style tweaks, component splitting, memo/render-boundary optimization, image preloading, computed-value caching, test coverage hardening, or performance bugfixes with no user-visible behavior change

## Dependencies

This skill depends on two layers:

- `OpenSpec`
  - `openspec/changes/<change-name>/` is the only formal artifact system
  - `proposal.md`, `design.md`, `spec.md`, `tasks.md`, and optional `plan.md` live there
- superpower skills
  - exploration: `brainstorming`, `openspec-explore`
  - implementation entry: `openspec-apply-change`
  - discipline layers: `test-driven-development`, `executing-plans`, `subagent-driven-development`
  - quality gates: `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `openspec-verify-change`

This skill does not replace those skills. It defines when to use them, in what order, and which artifact system remains authoritative.

## Core Rules

- `OpenSpec` artifacts are the only formal source of truth. Do not create a parallel proposal / design / tasks / spec system outside `openspec/changes/<change-name>/`.
- OpenSpec artifacts are required only for formal changes that affect capability, visible workflow, contract, state semantics, architecture, or persisted data shape. For local implementation optimization with unchanged semantics, skip artifacts and use the normal code-change, targeted-test, and verification loop.
- For any new or materially underspecified change request, do a lightweight discovery/brainstorming pass before creating OpenSpec artifacts. OpenSpec is the artifact system, not a substitute for requirement discovery.
- Do not create or update `proposal.md`, `design.md`, `spec.md`, or `tasks.md` until the user's key decisions are stable enough to make the artifact meaningful. If the request says "plan", "design", "architecture", "based on research", "start a change", or otherwise leaves product/technical direction open, treat scope as unstable by default.
- In planning or design stages, any unresolved `Open Questions` item is an artifact-readiness blocker by default. Do not treat the scope as stable unless the question is resolved, explicitly deferred as out of scope, or confirmed as non-blocking, and you have at least 95% confidence that you understand the user's intent.
- Unless the user explicitly requests it, do not write the default superpower artifact files as formal specs.
- Prefer the lightest workflow that still preserves clarity and correctness.
- Use superpower skills as discipline layers, not as competing artifact systems.
- Workflow cost must not exceed implementation cost. Process serves progress; do not run process for its own sake.
- The moment you notice "process loops outpacing code progress", shrink the process: fewer agents, fewer reviewer rounds, drive the remaining main path inline.

## Workflow

1. Clarify the stage first.
If scope is still unstable, explore with `brainstorming` or `openspec-explore`, but do not let their default artifact flow override this orchestration. This discovery step is mandatory for new architecture/planning/design requests unless the user has already provided explicit decisions that make the scope stable.

During discovery:
- Invoke and follow the appropriate exploration skill for mechanics: use `brainstorming` for user-facing design/architecture decisions and any unresolved `Open Questions`; use `openspec-explore` for open investigation or reframing that does not yet require a user decision.
- When judging artifact readiness, include existing OpenSpec state, research docs, and local workflow overrides as inputs.
- Identify the open decisions that would materially change `proposal.md`, `design.md`, `spec.md`, or `tasks.md`.
- Get explicit user confirmation that those artifact-shaping decisions are stable before creating or updating OpenSpec artifacts.
- If an artifact draft would contain an `Open Questions` section with unresolved items, pause artifact progression and discuss those questions through `brainstorming`. Only write "no blocking questions" after the user has confirmed the relevant decisions or explicitly accepted the remaining uncertainty as non-blocking.

At minimum, for architecture or planning work confirm:
- primary user / entrypoint
- in-scope and out-of-scope capabilities
- output or integration target
- first validation or benchmark scenarios
- important dependency or provider choices

Do not treat existing research documents as approval. Research docs are evidence for the discussion; the user still needs to confirm the decisions that become formal artifacts.

2. If the repo has local workflow overrides in `AGENTS.md` or `CLAUDE.md`, apply them before following generic skill defaults.

3. Once scope is stable and the user has confirmed the direction, draft the full formal spec set in `openspec/changes/<change-name>/`:
- `proposal.md`
- `design.md`
- related `spec.md`

4. Present the full draft at once.
Do not use section-by-section design approval. Do not create `tasks.md` or `plan.md` before the user reviews the full draft.
Skip the generic `Offer visual companion` step unless the user explicitly asks for one.

5. After the user approves the draft, create `tasks.md`.
Create `plan.md` only when execution orchestration is genuinely needed, such as multi-agent work, high-risk migration, long-running recovery, or complex debugging.

6. Before implementation, self-review `proposal.md`, `design.md`, `spec.md`, `tasks.md`, and `plan.md` if present.
Check for placeholders, contradictions, scope drift, spec-to-task traceability, executable tasks, and whether `plan.md` is only carrying execution orchestration.

7. Only after that review and user confirmation, enter implementation.
Use `tasks.md` as the progress baseline. Prefer `openspec-apply-change` when approved tasks already exist.

## Execution Rules

- Run an environment sanity check before starting work (e.g. importability of the module under test, availability of key tools); do not let environment issues surface late and amplify cost.
- For contracts, configuration, and base abstractions, build the minimum closure needed to unblock follow-up tasks; defer non-blocking polish, extra hardening, and edge validation to a later batch.
- Documentation updates, changelog entries, and incidental cleanup default to after the main path passes, unless they are a direct prerequisite of the current implementation.
- When `proposal.md`, `design.md`, `spec.md`, and `tasks.md` are sufficient, do not create `plan.md`.
- If `plan.md` is needed, keep it limited to execution orchestration:
  - inline vs subagent routing
  - worktree decisions
  - verification gates
  - risks and recovery
- Do not duplicate requirements, design, or task definitions in `plan.md`.
- Update `tasks.md` as state changes happen; do not leave progress only in chat.
- Use subagents only for genuinely independent side tasks that do not block the next step (e.g. independent review, doc migration, asset cleanup); for tightly coupled main-path implementation, drive it inline rather than mechanically splitting it across multiple subagent rounds with idle waits.
- Recommend an execution mode (inline / worktree / subagent) based on the task. For small, well-scoped work, use `openspec-apply-change` directly. For complex or multi-step work, use `executing-plans` or `subagent-driven-development` as a discipline layer, and always treat `tasks.md` as the high-level progress and scope baseline.

### Subagent Routing Rubric

Before spawning subagents, identify the main critical path and the immediate local task. Use subagents for bounded side tasks that can run in parallel while the main thread keeps making progress.

Good subagent candidates:

- The subtask is independent from the next local step.
- The write scope is explicit and preferably disjoint from other workers.
- The output is concrete, reviewable, and has an obvious verification command.
- The main thread can integrate the result without redoing the work.
- The work is a sidecar task such as tests, docs, isolated JS logic, native logging, read-only SDK comparison, asset cleanup, or independent review.

Keep work inline when:

- The task centers on one state machine, one tightly coupled file, or one abstraction boundary.
- The next local step depends on the result.
- Multiple agents would edit the same file or semantic contract.
- The work requires continuous judgment rather than a bounded deliverable.
- The process overhead is likely to exceed implementation time.

When using subagents:

- Assign explicit file or responsibility ownership.
- Tell workers that others may be editing the codebase and they must not revert unrelated changes.
- Continue non-overlapping local work immediately after spawning.
- Wait only when blocked on the result or ready to integrate.
- Review and integrate returned changes before final verification.

## Discipline Layers

- Default to `test-driven-development`: for new features, bugfixes, refactors, or behavior changes, write a failing test first, confirm it fails for the right reason, then write the minimum implementation and return to green. Only deviate when the user explicitly allows it, or when the task is inherently config / prototype / scaffolding work that is unsuitable for TDD. Keep TDD strict, but group test batches by behavior to avoid splitting one state machine into excessive micro red-green loops.
- Run review at milestones, not after every small fix:
  - after finishing a major task or a group of tasks
  - after a high-risk refactor or complex bugfix
  - before merging, archiving, or notifying the user for acceptance
  - default to `requesting-code-review`; when feedback comes back, use `receiving-code-review` and do not accept it mechanically.
- Before claiming "done", preparing a commit, archiving, or notifying the user for acceptance, you must run `verification-before-completion`.
- When you need to verify implementation alignment with OpenSpec artifacts, also use `openspec-verify-change`.

## OpenSpec Archive Conflict Handling

- `openspec/specs/` is the single main spec for currently active capabilities. `openspec/changes/<change-name>/specs/` only represents the delta of this change; it is not a second long-term source of truth.
- Before archiving, if the delta spec conflicts with the main spec under the same capability at the requirement, scenario, or semantic level, do not archive directly.
- Contradictory requirements must not coexist long-term in `openspec/specs/`, and "latest spec wins" is not an acceptable substitute for explicit merging.
- Resolve conflicts based on these facts:
  - the approved `proposal.md`, `design.md`, `tasks.md`
  - the actual behavior of the current implementation
  - the result of `openspec-verify-change`
- When merging, work at requirement / scenario granularity in the main spec:
  - keep existing content not touched by this change
  - explicitly rewrite requirements or scenarios that this change replaces
  - when only adding scenarios, append them under the existing requirement
  - explicitly delete deprecated content rather than leaving it for "later cleanup"
- If the delta spec is too coarse, has unclear boundaries, or disagrees with the implementation, first revise the change's `proposal.md`, `design.md`, and `specs/*.md`, then sync or archive.
- If you cannot decide which semantics to keep based on approved scope and implementation facts, stop and clarify before archiving; do not carry unresolved conflicts into archive.
- Archive is not a place to defer spec decisions. Archive consolidates an already-resolved change into the persistent spec set.

## Routing Notes

- `brainstorming` is for exploration, not the final artifact sequence.
- `openspec-explore` is for open investigation or reframing.
- `openspec-apply-change` is for implementation after approved tasks exist.
- `executing-plans` or `subagent-driven-development` are optional discipline layers, not replacements for `tasks.md`.
- Repo-local `AGENTS.md` or `CLAUDE.md` may tighten or narrow this workflow; treat those as higher-priority supplements.
