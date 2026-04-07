---
name: closure-retrospective
description: Use when wrapping up a non-trivial task and there may be reusable lessons worth codifying into project guidance, existing skills, a new skill, or agent instruction files before final handoff.
---

# Closure Retrospective

Use this skill near task closure when the work exposed reusable guidance that could improve future runs.

This skill is conservative by default. If the signal is weak, do nothing and finish normally.

This skill is not a memory system. Do not route output into memory workflows unless the user explicitly asks.

## Use This Skill For

- end-of-task reflection on whether the conversation exposed durable, reusable guidance
- repeated correction patterns that suggest missing workflow guardrails
- tool usage mistakes, command friction, or sequencing loops that future tasks should avoid
- stable heuristics that would improve maintainability, health, performance, or delivery quality if reused
- deciding whether a lesson belongs in an existing skill, a new skill, or `AGENTS.md` / `CLAUDE.md`

## Do Not Use This Skill For

- trivial tasks or casual chat
- one-off user preferences with no broader reuse
- temporary debugging notes
- speculative improvements without evidence from the current task
- silently editing rules or skills before user approval

## Closure Gate

Only run this skill when the task is substantively done or clearly entering wrap-up.

Good signals:

- the requested implementation, analysis, or answer is already complete
- remaining work is limited to summary, verification, or handoff
- blockers and open risks are already known

Bad signals:

- core implementation is still in progress
- key debugging is unresolved
- major research questions are still open

If the task is not actually at closure, stop and finish the task first.

## What Counts As Codifiable

Promote a lesson only when it is both reusable and worth carrying.

Strong candidates:

- a repeated workflow mistake or correction pattern
- a recurring tool rule that should become default behavior
- a missing decision rubric that would prevent future churn
- a stable review or efficiency heuristic that improves project outcomes
- a clear scope boundary that prevents over-building or wasted loops

Weak candidates:

- a lesson that only mattered because of one unusual file or environment
- vague advice such as `be more careful`
- preferences with no durable benefit
- optimizations that add maintenance cost without clear payoff

## Workflow

### 1. Gather candidate lessons

Review the current task only. Extract concrete observations, not generic morals.

Prefer evidence such as:

- repeated user correction
- repeated tool misuse or failed command patterns
- unnecessary workflow loops
- decisions that clearly improved the result

### 2. Score each candidate

Read [references/decision-rubric.md](references/decision-rubric.md).

Drop any candidate that fails the rubric or would likely create more rule weight than benefit.

### 3. Choose the correct target

Use this routing preference:

- existing skill: workflow-specific improvement to an already-existing capability
- new skill: an independent, reusable workflow that should stand alone
- `AGENTS.md` or `CLAUDE.md`: repository-wide default behaviors, constraints, or preferences
- no change: the lesson is too weak, too narrow, or too expensive to maintain

Prefer strengthening an existing artifact over creating a new one.

## Output Contract

Read [references/output-template.md](references/output-template.md).

When suggestions qualify:

- provide at most 3 suggestions
- state the evidence from the current task
- explain why the lesson is reusable
- name the recommended target
- call out expected benefit and maintenance risk
- end by asking for confirmation before any edits

When nothing qualifies:

- if the user explicitly asked for a retrospective, say that no codifiable lesson met the bar
- otherwise, do not surface a retrospective section; finish the task normally

## Hard Rules

- Do not confuse a single anecdote with a durable rule.
- Do not create a new skill when a smaller update to an existing skill would work.
- Do not update `AGENTS.md` or `CLAUDE.md` for narrow workflow details that belong in a skill.
- Do not make edits during the retrospective phase. Suggest first. Wait for approval.
- Optimize for long-term signal, not for documenting every interesting thought.
