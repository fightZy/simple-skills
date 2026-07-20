---
name: closure-retrospective
description: Extract reusable mechanisms when a non-trivial task is substantively complete and evidence may justify durable guidance in a skill or applicable AGENTS.md / CLAUDE.md, especially after repeated corrections, tool friction, sequencing loops, stable scope boundaries, or decisions that clearly improved results.
---

# Closure Retrospective

## Core Principle

Treat an observed outcome as evidence. Codify only the reusable mechanism that explains why a controllable decision caused, protected, or improved that outcome. Prefer the narrowest existing artifact and require the expected benefit to exceed its maintenance cost. This skill is not a memory workflow; do not propose or update memory unless the user explicitly requests it.

## Closure Gate

Run the retrospective only after the substantive task is complete or clearly entering final handoff. If implementation, debugging, or research remains unresolved, stop the retrospective and finish the task first.

Drop trivial work, one-off preferences, temporary debugging notes, and unsupported interpretations.

## Workflow

1. **Gather evidence.** Record observable behavior from the current task and the resulting failure, success, protected boundary, or efficiency gain. Keep observation separate from interpretation. Complete this step when every candidate names its evidence and outcome.
2. **Locate the decision point.** Identify a choice, sequence, validation, or scope decision available before the outcome. Complete this step when the future trigger is observable before the outcome and the alternative action is under the agent's control. Drop candidates with no such decision point.
3. **Extract the reusable mechanism.** Explain the supported relationship between the decision and outcome. For every candidate reaching this step, read [references/mechanism-tests.md](references/mechanism-tests.md) and apply every test. Complete this step only when the candidate can be expressed as `trigger -> action -> verification` and passes every test.
4. **Inspect only the narrowest plausible targets after the mechanism survives:**
   - For workflow guidance, shortlist skills by name and description, then inspect the most relevant sections.
   - For repository-wide guidance, inspect the `AGENTS.md` or `CLAUDE.md` files applicable to the current working directory.
   - If both project files exist, follow the repository's authority or synchronization convention. Do not duplicate guidance across them without an explicit convention.
   - Use existing artifacts only to check coverage and choose placement; do not use them as evidence for the mechanism.
5. **Decide whether to codify.** Read [references/decision-rubric.md](references/decision-rubric.md), apply every required gate, and assign the verdict. Complete this step when every surviving candidate has one exact target and insertion point; use `Drop` otherwise.
6. **Present the result.** If at least one candidate survives, read [references/output-template.md](references/output-template.md) and present at most three recommendations. Treat three as a ceiling, not a quota. Match the user's language.

## Output Behavior

- When the user explicitly requests a retrospective and nothing qualifies, output only this compact shape: title, `Worth codifying: no`, and one sentence naming the failed gate or reason.
- When the retrospective is implicit and nothing qualifies, surface no retrospective section.
- Keep the retrospective phase read-only. Present suggestions and wait for explicit approval before editing any skill or project guidance. A later approval begins a separate edit phase.

## Hard Boundaries

- Promote a single observed event only when its evidence supports a reusable mechanism and recurring decision point; otherwise treat it as an incident fact and drop it.
- Do not create a new skill when an existing skill can absorb the guidance cleanly.
- Do not put narrow workflow details in repository-wide guidance.
- Do not recommend repository guidance without naming the target file and section.
- Do not route retrospective output into memory workflows unless the user explicitly asks.
- Prefer zero recommendations over incident-specific or vague guidance.
