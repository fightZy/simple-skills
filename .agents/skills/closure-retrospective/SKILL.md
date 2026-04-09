---
name: closure-retrospective
description: Use when wrapping up a non-trivial task and deciding whether durable guidance from the work should be folded into an existing skill, repository instructions, or a new skill before final handoff.
---

# Closure Retrospective

Use this skill near task closure when the work exposed durable guidance that could improve future runs.

This skill is conservative by default:

- If the signal is weak, do nothing and finish normally.
- Prefer strengthening an existing artifact over creating a new one.
- This skill is not a memory system. Do not route output into memory workflows unless the user explicitly asks.

## Use This Skill For

- End-of-task reflection on whether the conversation exposed durable, reusable guidance
- Repeated correction patterns that suggest missing workflow guardrails
- Tool usage mistakes, command friction, or sequencing loops that future tasks should avoid
- Stable heuristics that would improve maintainability, health, performance, or delivery quality if reused
- Deciding whether a lesson belongs in an existing skill, a new skill, or `AGENTS.md` / `CLAUDE.md`

## Do Not Use This Skill For

- Trivial tasks or casual chat
- One-off user preferences with no broader reuse
- Temporary debugging notes
- Speculative improvements without evidence from the current task
- Silently editing rules or skills before user approval

## Closure Gate

Only run this skill when the task is substantively done or clearly entering wrap-up.

Good signals:

- The requested implementation, analysis, or answer is already complete
- Remaining work is limited to summary, verification, or handoff
- Blockers and open risks are already known

Bad signals:

- Core implementation is still in progress
- Key debugging is unresolved
- Major research questions are still open

If the task is not actually at closure, stop and finish the task first.

## What Counts As Codifiable

Promote a lesson only when it is both reusable and worth carrying.

Strong candidates:

- A repeated workflow mistake or correction pattern
- A recurring tool rule that should become default behavior
- A missing decision rubric that would prevent future churn
- A stable review or efficiency heuristic that improves project outcomes
- A clear scope boundary that prevents over-building or wasted loops

Weak candidates:

- A lesson that only mattered because of one unusual file or environment
- Vague advice such as `be more careful`
- Preferences with no durable benefit
- Optimizations that add maintenance cost without clear payoff

## Generalize Before Suggesting

Every surviving lesson must be rewritten into guidance that is:

- General: future agents can apply it outside the current task
- Durable: likely to stay useful beyond the immediate files and moment
- Actionable: phrased as a rule, rubric, routing decision, or placement heuristic

Rewrite candidates before presenting them:

- Strip task-local trivia unless it is essential to the rule
- Prefer workflow language over narrative retelling
- Convert a specific incident into a reusable constraint or decision rule

Reject the candidate if it only makes sense with current-task context.

Examples:

- Too specific: `When closing skill X, update section Y because this task needed it`
- Better: `When a retrospective reveals a repo-wide default, extend the matching AGENTS.md section before creating a new section`
- Too specific: `Mention command Z because it failed here`
- Better: `Codify repeated command pitfalls only when they are likely to recur across the repo workflow`

## Integrate With Existing Content First

Do not treat codification as greenfield writing. The recommendation must explain how it fits into what already exists.

For each qualified lesson:

- Identify the narrowest existing artifact that could absorb it
- Identify the specific existing section to extend when possible
- Recommend a new section only when no current section can hold the guidance cleanly
- Reject the change if the placement would be awkward, redundant, or noisy

Placement defaults:

- Existing skill: update the most relevant section first; add a new section only if the concept introduces a genuinely new concern inside that skill
- `AGENTS.md` / `CLAUDE.md`: map the lesson to an existing heading first; create a new heading only if the rule defines a durable new category of repository-wide guidance
- New skill: only when the lesson is an independent reusable workflow that does not fit an existing skill
- No change: when the lesson is real but still too narrow or costly to preserve

## Workflow

### 1. Gather candidate lessons

Review the current task only. Extract concrete observations, not generic morals.

Prefer evidence such as:

- Repeated user correction
- Repeated tool misuse or failed command patterns
- Unnecessary workflow loops
- Decisions that clearly improved the result

### 2. Score each candidate

Read [references/decision-rubric.md](references/decision-rubric.md).

Drop any candidate that fails the rubric or would likely create more rule weight than benefit.

### 3. Rewrite the lesson into durable guidance

Before routing the lesson, rewrite it so the output is not tied to this one task.

The recommendation should describe:

- The generalized rule or heuristic
- Why it is likely to recur
- What type of future mistake or churn it prevents

If the wording still depends on this task's local details, reject it.

### 4. Choose the correct target and insertion point

Use this routing preference:

- Existing skill: workflow-specific improvement to an already-existing capability
- New skill: an independent, reusable workflow that should stand alone
- `AGENTS.md` or `CLAUDE.md`: repository-wide default behaviors, constraints, or preferences
- No change: the lesson is too weak, too narrow, or too expensive to maintain

Prefer strengthening an existing artifact over creating a new one.

For `AGENTS.md` or `CLAUDE.md`, also decide:

- Which existing section should absorb the guidance
- Whether the existing section can be extended cleanly
- Whether a new section is justified because no current section matches

For an existing skill, also decide:

- Which current section should be amended
- Whether a new section is needed or would just fragment the skill

### 5. Format the recommendation for handoff

Read [references/output-template.md](references/output-template.md).

The final output must be easy to scan in Markdown and must include:

- A clear yes/no codification result
- Per-recommendation sections with evidence, generalized guidance, and placement
- An explicit placement decision such as `extend existing section` or `add new section`
- A confirmation request before any edits

## Output Contract

When suggestions qualify:

- Provide at most 3 suggestions
- State the evidence from the current task
- Rewrite each suggestion as generalized, reusable guidance
- Match the user's language preference; if no explicit preference is given, default to the language used in the user's request
- Name the recommended target
- Explain how the guidance should integrate with existing content
- Call out expected benefit and maintenance risk
- End by asking for confirmation before any edits

When nothing qualifies:

- If the user explicitly asked for a retrospective, say that no codifiable lesson met the bar
- Otherwise, do not surface a retrospective section; finish the task normally

## Hard Rules

- Do not confuse a single anecdote with a durable rule.
- Do not create a new skill when a smaller update to an existing skill would work.
- Do not update `AGENTS.md` or `CLAUDE.md` for narrow workflow details that belong in a skill.
- Do not recommend repo-level guidance without naming the target section or explaining why a new section is needed.
- Do not emit task-local advice as if it were a general rule.
- Do not make edits during the retrospective phase. Suggest first. Wait for approval.
- Optimize for long-term signal, not for documenting every interesting thought.
