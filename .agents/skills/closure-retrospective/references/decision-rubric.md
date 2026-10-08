# Decision Rubric

Use after inspecting existing coverage, for candidates that could improve a future decision or execution.

## Evidence and transfer

Separate direct observations, inference, and intuition. Describe actual breadth across occurrences, tasks, or contexts, and distinguish contemporaneous records from later explanations. Reject intuition or retrospective storytelling as the sole basis for a durable change.

Identify the mechanism, decision structure, ownership boundary, or recurring constraint that explains the proposed improvement. Strip incidental filenames, tools, values, and chronology unless the change depends on them. Similar symptoms alone do not establish a shared mechanism.

A single direct observation may support a narrowly scoped change. Broader empirical claims need broader evidence; reviewer agreement over the same records and hypothetical substitutions do not increase observed coverage. A demonstrated logical invariant or an existing authoritative requirement can justify firm wording without repeated incidents.

## Scope and boundaries

Choose the narrowest useful scope supported by the evidence. Consider relevant substitutions, such as actor, domain, lifecycle stage, tool, reversibility, or evidence availability. Ask when the proposed change would help, become unnecessary, or cause harm.

State the governing condition, any known counterexample or failure boundary, and material unknowns. Uncertain boundaries call for narrower scope or softer wording, not universal application.

## Wording strength

Apply this section when a proposed change contains instructions.

| Wording | Basis |
| --- | --- |
| must / never | An applicable safety, permission, integrity, or logical invariant requires it, or strong cross-context evidence supports the stated scope without a reasonable exception |
| Conditional rule | The behavior is required when an explicit predicate holds |
| default / should | The behavior usually helps but legitimate exceptions exist |
| consider / example | Evidence is narrow, exploratory, or mainly diagnostic |

Use open discovery and explicit decisions: examples may illustrate a defined governing criterion, but actions, edits, permissions, and hard gates need explicit scope or predicates. Open-ended examples never expand authorization.

## Remedy, ownership, and activation

Choose a remedy for the evidenced mechanism before choosing a file. Consider relevant changes to guidance, context sources or entry points, tool interfaces or outputs, and execution feedback. For a stable condition that can be reliably checked at acceptable cost, consider deterministic validation or feedback; use guidance for decisions and exceptions that require judgment. Choose by mechanism and expected benefit rather than a fixed preference for wording or automation.

Treat inspectable configuration, tool interfaces, and observed environment state as potential sources of truth, with their authority and applicability verified. Cache their facts in guidance only when lookup cost or interpretation justifies it; retain useful rationale or conventions the environment does not expose, and identify when changeable cached facts need reconsideration.

Choose ownership from applicability, not from a ranking of file types:

| Supported scope | Suitable home |
| --- | --- |
| Current task only | Keep it local; no durable change |
| A reusable workflow | Its existing skill, supporting reference, or owned environment mechanism |
| A project or part of one | Existing project guidance, configuration, or tools at the matching scope |
| A shared agent environment | Its authoritative guidance or mechanism within the supported scope |

Then choose when the agent needs it. Keep guidance needed throughout its scope readily available; put workflow steps in the entrypoint and branch-specific detail behind an explicit loading condition. Place feedback where it can inform the relevant decision or action. Shared definitions should have one maintained source that callers can find.

Only then choose the smallest effective action: retain, delete, merge, clarify, narrow, strengthen, move, or add. Prefer an appropriate existing artifact or mechanism. A new skill requires an independently invocable workflow; a new project section requires a matching gap in project guidance. Neither file type takes precedence over the other.

Name the exact target and section or interface, or justify a new artifact or mechanism. Preserve the intent and applicability of established approval requirements and operational invariants when simplifying content. Treat guidance as a no-op only when existing evidence supports that it adds no decision or execution value within its scope; assumptions about default model behavior alone do not justify removal.

## Benefit, cost, and useful lifetime

Explain which future decision or execution outcome improves and whether the change prevents an error, detects it earlier, limits a claim, or improves interpretation. Do not claim prevention when the evidence supports only detection or explanation.

Compare that benefit with context and maintenance cost, repeated lookups or tool calls, irrelevant output, false triggering, unnecessary approvals, slower work, ownership conflicts, and constraints on exploration. Shorter wording or output alone is not proof of improvement. Reject changes whose expected benefit does not justify their costs.

Use existing cases and counterexample reasoning to check what should improve, what must remain valid, and what would overturn the recommendation. Distinguish this reasoning from observed behavioral validation; a numerical score cannot replace an unresolved qualitative condition.

When a change depends on changeable tools, environments, processes, or responsibilities, state what would make it obsolete or require reconsideration. Stable invariants need no arbitrary expiry date, and recording this condition does not start a monitoring workflow.
