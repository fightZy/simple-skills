# Decision Rubric

Apply every required gate. If a candidate fails one, use `Drop`.

## Required Gates

| Gate | Pass when | Drop when |
| --- | --- | --- |
| Evidence | Observable behavior in the current task supports the lesson | The lesson depends on intuition, speculation, or post-hoc storytelling |
| Repeatability | Another agent or future task could plausibly encounter the same situation | It depends on an unusual file, environment, or one-off preference |
| Action delta | The guidance would change a future agent's behavior and prevent a named failure, churn loop, or delay | It only says to be more careful or has no concrete effect |
| Net benefit | Expected maintainability, safety, consistency, or delivery benefit exceeds maintenance cost | It adds rule weight without clear payoff |
| Existing coverage | Relevant skills and applicable project guidance were checked for duplication or a clean extension point | Existing guidance already covers it completely |
| Placement fit | The narrowest target artifact and exact insertion point are clear | Placement would be redundant, fragmented, or awkward |

Existing artifacts establish coverage and placement; they do not replace evidence from the current task.

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

- The evidence, future trigger, prevented failure, and action delta are explicit.
- The recommendation is generalized beyond the current task.
- The target and insertion point are named.
- The proposal is smaller and cleaner than creating another artifact.

When in doubt, use `Drop`.
