# Decision Rubric

Apply every required gate. If a candidate fails one, use `Retain as evidence` when the run remains useful telemetry; otherwise use `Drop`.

## Required Gates

| Gate | Pass when | Do not promote when |
| --- | --- | --- |
| Evidence | Corroborated observable behavior supports the relationship between a decision and outcome | The claim depends on self-report, intuition, correlation, or post-hoc storytelling |
| Mechanism | Every test in `mechanism-tests.md` passes | The candidate restates an incident, preference, result, or cause label |
| Recurring decision point | The same decision structure can recur within the intended owner's scope | Recurrence depends on one unusual file, command, environment, or error text |
| Transfer and boundary | Two materially different in-scope situations share the structure and a non-applicable case is explicit | Transfer relies on surface similarity or lacks a defensible limit |
| Action delta | An observable trigger changes a controllable pre-outcome action with a verification signal | The lesson only changes explanation after the outcome |
| Intervention maturity | The lesson's stability and consequence justify the proposed degree of constraint | Unsettled judgment is forced into a deterministic control or settled behavior remains vague prose |
| Earliest semantic owner | One authoritative context, example, review, domain, executable, architectural, or maintenance surface owns the decision | Placement defaults to a convenient document or creates a parallel owner |
| System convergence | The proposal addresses the existing population, future recurrence, and redundant controls proportionally | It adds another defense while contradictory precedent or weaker duplicates remain |
| Effect proof | Current evidence or a proportionate follow-up can test later behavior at the claim boundary | Success would mean only that a file exists or a proxy check passes |
| Lifecycle | An owner, carrying cost, reconsideration trigger, and retirement condition are named | The intervention would persist without maintenance responsibility |
| Net benefit | Expected safety, coherence, maintainability, or delivery gain exceeds attention and maintenance cost | Rule weight and latency exceed the supported benefit |
| Existing coverage | Relevant owners were checked for full coverage, extension, consolidation, or replacement | Existing behavior already covers the class completely |

Existing artifacts establish coverage, ownership, and placement; they do not supply evidence for the mechanism.

## Verdicts

| Verdict | Use when |
| --- | --- |
| `Retain as evidence` | The trajectory is useful telemetry but recurrence, mechanism, maturity, or effect evidence is insufficient |
| `Context intervention` | Stable knowledge must be retrieved at a decision point through a routing document, skill, or runbook |
| `Judgment intervention` | A blessed example, reviewer or evaluation must carry qualitative or still-evolving judgment |
| `Executable intervention` | A type, API, domain tool, lint, test, or policy check can own a settled invariant |
| `Architecture / migration` | Repeated defects expose the wrong representation, owner, dependency direction, or existing population |
| `Continuous maintenance` | A settled condition must remain true while repository or external state changes across runs |
| `Drop` | The candidate is trivial, unsupported, non-transferable, fully covered, or not worth its carrying cost |

Each promoted verdict must name one exact authoritative target, insertion or ownership point, backward path, forward ratchet, follow-up proof, lifecycle owner, and retirement condition. Use `Not applicable` only with a concrete reason. Do not mirror one rule across artifacts unless the repository explicitly requires synchronization.

## Final Check

Before suggesting an intervention, verify:

- Evidence, mechanism, repair, and later effect claim remain separate.
- The recommendation changes behavior before the outcome.
- The owner matches the lesson's maturity and consequence.
- Existing precedent and future recurrence are both addressed.
- Stronger ownership can consolidate or retire weaker controls.
- The proposal is smaller and more coherent than adding another artifact.

When in doubt, retain the run as evidence rather than promoting it.
