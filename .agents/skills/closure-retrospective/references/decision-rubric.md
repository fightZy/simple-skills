# Decision Rubric

Apply every required gate. If a candidate fails one, use `Drop`.

## Required Gates

| Gate | Pass when | Drop when |
| --- | --- | --- |
| Evidence | Observable behavior in the current task supports the stated relationship between a decision and outcome | The candidate depends on intuition, correlation, speculation, or post-hoc storytelling |
| Mechanism | The candidate passes every required test in `mechanism-tests.md` and explains why the action affects the outcome | It restates an incident, cause label, preference, or result without an evidence-supported mechanism |
| Recurring decision point | The same decision structure recurs within the proposed target artifact's scope | Recurrence depends on the same unusual file, command, environment, or error text |
| Transfer and boundary | Two materially different in-scope situations can use the guidance, and a limiting or non-applicable situation is explicit | Transfer relies on surface similarity, or the guidance has no defensible boundary |
| Action delta | The trigger is observable before the outcome and the action changes a future decision with a verification signal | It only changes what an agent might consider, says to be more careful, or explains the outcome afterward |
| Net benefit | Expected maintainability, safety, consistency, or delivery benefit exceeds maintenance cost | It adds rule weight without clear payoff |
| Existing coverage | Relevant skills and applicable project guidance were checked for duplication or a clean extension point | Existing guidance already covers it completely |
| Placement fit | The narrowest target artifact and exact insertion point are clear | Placement would be redundant, fragmented, or awkward |

Existing artifacts establish coverage and placement; they do not supply evidence or prove the mechanism.

## Verdicts

| Verdict | Use when |
| --- | --- |
| `Update existing skill` | The lesson improves a workflow already covered by a skill |
| `Create new skill` | The lesson is an independent reusable workflow with its own trigger conditions |
| `Update existing constraint` | The lesson is repository-wide and fits an existing `AGENTS.md` or `CLAUDE.md` section |
| `Add constraint section` | The lesson is repository-wide and introduces a durable category no current section covers |
| `Drop` | Any required gate fails |

For a new skill, name the proposed skill, triggers, and minimum useful contents. For project guidance, name the authoritative file and existing or proposed section. Do not mirror the same rule across `AGENTS.md` and `CLAUDE.md` unless the repository explicitly requires synchronization.

## Final Check

Before suggesting a change, verify:

- The evidence and reusable mechanism are stated separately.
- The trigger, action, verification signal, expected outcome, and boundary are explicit.
- The recommendation transfers beyond the incident at the abstraction level of its target artifact.
- The target and insertion point are named.
- The proposal is smaller and cleaner than creating another artifact.

When in doubt, use `Drop`.
