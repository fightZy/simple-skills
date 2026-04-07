# Decision Rubric

Use this rubric to decide whether a closure-stage lesson is worth codifying.

## Gate 1: Evidence

Ask:

- Did the lesson come from observable behavior in the current task?
- Is there concrete evidence such as repeated correction, repeated friction, or a clear before/after improvement?

Reject if the lesson is mostly intuition or post-hoc storytelling.

## Gate 2: Repeatability

Ask:

- Is this likely to recur across future tasks?
- Would another agent or contributor plausibly hit the same issue?

Reject if the lesson depends on one unusual environment or a narrow one-off circumstance.

## Gate 3: Net Benefit

Ask:

- Would codifying this improve maintainability, project health, performance, safety, consistency, or delivery speed?
- Is the expected benefit larger than the ongoing maintenance cost?

Reject if the lesson creates process weight without clear future payoff.

## Gate 4: Correct Placement

Choose the narrowest useful target.

| Target | Use when |
| --- | --- |
| Existing skill | The lesson improves a known workflow already covered by a skill |
| New skill | The lesson defines an independent, reusable workflow that deserves its own trigger |
| `AGENTS.md` / `CLAUDE.md` | The lesson is a repository-wide default behavior, constraint, or preference |
| No change | The lesson does not justify standing guidance |

Prefer `existing skill` over `new skill`, and prefer workflow-local guidance over repo-wide constraints.

## Lightweight Scoring

Score each candidate from `0` to `2` on each axis:

- `Evidence`
- `Repeatability`
- `Benefit`
- `Placement clarity`

Interpretation:

- `0-3`: reject
- `4-5`: usually reject unless the user explicitly wants a broad retrospective
- `6-8`: eligible to suggest

Even a high score should be rejected if the resulting rule would be noisy, redundant, or hard to maintain.

## Anti-Overfitting Checks

Before suggesting a codified change, ask:

- Am I reacting to a single mistake rather than a pattern?
- Would this still look useful a month from now?
- Does this create a rule someone will have to remember forever for a tiny gain?
- Could I solve the problem by strengthening an existing instruction instead of adding another artifact?

If these checks raise doubt, do not suggest the change.
