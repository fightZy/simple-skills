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

## Gate 5: Integration Fit

Ask:

- Can this be added to an existing section or heading without creating clutter?
- If the target is `AGENTS.md` or `CLAUDE.md`, which current section should absorb it?
- If proposing a new section, is that section introducing a durable new category rather than a one-off note?
- Would the resulting placement still be easy for future agents to discover and maintain?

Reject if the recommendation does not have a clear insertion point or would fragment the existing structure.

## Lightweight Scoring

Score each candidate from `0` to `2` on each axis:

- `Evidence`
- `Repeatability`
- `Benefit`
- `Placement clarity`
- `Integration fit`

Interpretation:

- `0-4`: reject
- `5-6`: usually reject unless the user explicitly wants a broad retrospective
- `7-10`: eligible to suggest

Even a high score should be rejected if the resulting rule would be noisy, redundant, or hard to maintain.

## Anti-Overfitting Checks

Before suggesting a codified change, ask:

- Am I reacting to a single mistake rather than a pattern?
- Would this still look useful a month from now?
- Does this create a rule someone will have to remember forever for a tiny gain?
- Could I solve the problem by strengthening an existing instruction instead of adding another artifact?
- Do I know exactly where this should be inserted, or am I inventing a new section too early?

If these checks raise doubt, do not suggest the change.
