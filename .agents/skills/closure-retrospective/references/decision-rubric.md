# Decision Rubric

Use this rubric to decide whether a closure-stage lesson is worth codifying.

## Gate 1: Evidence

Ask:

- Did the lesson come from observable behavior in the current task?
- Is there concrete evidence such as repeated correction, repeated friction, or a clear before/after improvement?

Intuition can start a candidate, but it is not evidence. Reject if the lesson cannot be tied to observable task behavior or becomes post-hoc storytelling.

## Gate 2: Repeatability

Ask:

- Is this likely to recur across future tasks?
- Would another agent or contributor plausibly hit the same issue?

Reject if the lesson depends on one unusual environment or a narrow one-off circumstance.

## Gate 3: Net Benefit

Ask:

- Would codifying this improve maintainability, project health, performance, safety, consistency, or delivery speed?
- Is the expected benefit larger than the ongoing maintenance cost?
- Would a future agent behave differently because this guidance exists?
- What specific failure, churn, or delay does this prevent?

Reject if the lesson creates process weight without clear future payoff.

## Gate 4: Existing Coverage

Check whether the lesson is already covered.

Ask:

- Does an existing skill, `AGENTS.md`, or `CLAUDE.md` already say this?
- Could the existing wording be tightened instead of adding new guidance?
- Is the candidate really new, or only a task-local example of an existing rule?

Reject duplicates. If the existing rule is close but incomplete, route the candidate as an update to that artifact.

## Gate 5: Correct Placement

Choose the narrowest useful action and target.

| Verdict | Use when |
| --- | --- |
| Create new skill | The lesson defines an independent, reusable workflow with its own trigger conditions |
| Update existing skill | The lesson improves a known workflow already covered by a skill |
| Update existing constraint | The lesson is repo-wide and fits an existing `AGENTS.md` / `CLAUDE.md` section |
| Add constraint section | The lesson is repo-wide and introduces a durable category no current section covers |
| Drop | The lesson does not justify standing guidance |

Check existing artifacts first, but do not force a standalone workflow or repo-wide category into an awkward location.

## Gate 6: Integration Fit

Ask:

- Can this be added to an existing section or heading without creating clutter?
- If the target is `AGENTS.md` or `CLAUDE.md`, which current section should absorb it?
- If proposing a new section, is that section introducing a durable new category rather than a one-off note?
- If proposing a new skill, what trigger conditions make it discoverable and independent?
- Would the resulting placement still be easy for future agents to discover and maintain?

Reject if the recommendation lacks a clear update location, proposed new artifact, or target artifact, or would fragment the existing structure.

## Checklist And Holistic Verdict

Before suggesting a codified change, verify:

- The candidate comes from current-task evidence, not only intuition.
- The candidate has a future trigger that another agent could recognize.
- The candidate prevents a concrete failure, churn loop, or delivery delay.
- The candidate would change future agent behavior.
- Existing guidance has been checked for duplication or absorption.
- The chosen target, proposed artifact, or update location is clear.
- The maintenance burden is smaller than the expected benefit.

Then choose one verdict:

- `Create new skill`
- `Update existing skill`
- `Update existing constraint`
- `Add constraint section`
- `Drop`

Use `Drop` when the lesson is real but still too narrow, redundant, expensive, or weakly evidenced.

## Optional Scoring

Score each candidate from `0` to `2` on each axis:

- `Evidence`
- `Repeatability`
- `Benefit`
- `Existing coverage check`
- `Placement clarity`
- `Integration fit`

Interpretation:

- `0-5`: reject
- `6-7`: usually reject unless the user explicitly wants a broad retrospective
- `8-12`: eligible to suggest

Use scoring only as a backstop. A high score should still be rejected if the holistic verdict is `Drop`.

## Anti-Overfitting Checks

Before suggesting a codified change, ask:

- Am I reacting to a single mistake rather than a pattern?
- Would this still look useful a month from now?
- Does this create a rule someone will have to remember forever for a tiny gain?
- Could I solve the problem by strengthening an existing instruction instead of adding another artifact?
- Am I avoiding a new skill even though the lesson is actually an independent workflow?
- Do I know exactly where this should be inserted, or am I inventing a new section too early?

If these checks raise doubt, do not suggest the change.
