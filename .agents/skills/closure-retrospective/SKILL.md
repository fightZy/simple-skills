---
name: closure-retrospective
description: Use when a non-trivial task is substantively complete and end-of-task evidence may justify durable guidance in a skill or applicable AGENTS.md / CLAUDE.md, especially after repeated corrections, tool friction, sequencing loops, or stable scope boundaries surface near closure.
---

# Closure Retrospective

## Core Principle

Codify only evidence-backed guidance that is reusable, actionable, and worth its maintenance cost. Prefer the narrowest existing artifact. This skill is not a memory workflow; do not propose or update memory unless the user explicitly requests it.

## Closure Gate

Run the retrospective only after the substantive task is complete or clearly entering final handoff. If implementation, debugging, or research remains unresolved, stop the retrospective and finish the task first.

Drop trivial work, one-off preferences, temporary debugging notes, and speculative lessons.

## Workflow

1. Gather observable evidence from the current task: repeated corrections, repeated command or tool friction, unnecessary loops, or decisions that clearly improved the result.
2. Read [references/decision-rubric.md](references/decision-rubric.md). Drop candidates that fail any required gate.
3. Inspect only the narrowest plausible targets:
   - For workflow guidance, shortlist skills by name and description, then inspect the most relevant sections.
   - For repository-wide guidance, inspect the `AGENTS.md` or `CLAUDE.md` files applicable to the current working directory.
   - If both project files exist, follow the repository's authority or synchronization convention. Do not duplicate guidance across them without an explicit convention.
   - Use the current task as evidence. Use existing artifacts only to check coverage and choose placement.
4. Rewrite each surviving lesson as guidance that is general, durable, and actionable. Include its future trigger and the concrete failure, churn, or delay it prevents.
5. Assign the rubric verdict and name the exact target artifact and insertion point. Reject recommendations with no clean placement.
6. If at least one candidate survives, read [references/output-template.md](references/output-template.md) and present at most three recommendations. Match the user's language.

## Output Behavior

- When the user explicitly requests a retrospective and nothing qualifies, output only this compact shape: title, `Worth codifying: no`, and one sentence naming the failed gate or reason.
- When the retrospective is implicit and nothing qualifies, surface no retrospective section.
- Keep the retrospective phase read-only. Present suggestions and wait for explicit approval before editing any skill or project guidance. A later approval begins a separate edit phase.

## Hard Boundaries

- Do not turn a single anecdote into a durable rule.
- Do not create a new skill when an existing skill can absorb the guidance cleanly.
- Do not put narrow workflow details in repository-wide guidance.
- Do not recommend repository guidance without naming the target file and section.
- Do not route retrospective output into memory workflows unless the user explicitly asks.
- Optimize for long-term signal, not exhaustive documentation.
