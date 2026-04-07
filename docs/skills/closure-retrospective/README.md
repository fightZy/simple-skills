# Closure Retrospective

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`closure-retrospective` is a lightweight wrap-up skill for deciding whether a finished task produced guidance worth codifying.

It is designed to make an agent:

- notice repeated correction and friction patterns near task closure
- separate durable lessons from one-off anecdotes
- choose the right landing zone for a suggestion
- ask for approval before changing any skill or instruction file

## Purpose

Use this skill when a non-trivial task is essentially done and there may be a reusable lesson worth carrying forward.

This skill is not for:

- project memory capture
- generic end-of-task summaries
- automatic rule editing without approval

## Design Principles

- Closure first: do not run it while core work is still unresolved.
- Conservative by default: weak signals should not create new rules.
- Suggestion before mutation: the first pass proposes changes but does not apply them.
- Narrowest useful target: prefer strengthening an existing artifact over adding a new one.
- Net-benefit filter: codify only when long-term value outweighs maintenance cost.

## Trigger Model

The runtime skill should activate only when both are true:

- the task is reaching final handoff
- there is evidence of a reusable lesson, not just an interesting observation

Typical signals:

- repeated user corrections
- repeated tool or command friction
- avoidable workflow loops
- a decision rule that clearly improved the outcome

## Target Selection

Use the narrowest correct destination:

- existing skill for workflow-local guidance
- new skill for an independent reusable workflow
- `AGENTS.md` or `CLAUDE.md` for repo-wide defaults or constraints

If none of these clearly win, the skill should recommend no change.

## Verification

Good verification should include wrap-up scenarios that tempt the agent to over-codify:

- a task with one interesting but narrow issue
- a task with repeated correction that does justify a rule suggestion
- a task that should produce no retrospective output at all

Good outputs should show:

- explicit evidence from the current task
- a clear reusable benefit
- correct target selection
- approval-first behavior instead of silent edits
