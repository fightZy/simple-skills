# Closure Retrospective

This maintainer overview is outside the runtime package. The authoritative entrypoint is [SKILL.md](../../../.agents/skills/closure-retrospective/SKILL.md).

## Purpose and scope

Use existing work evidence to optimize how an agent obtains, finds, interprets, and uses context and execution feedback. Changes can address guidance or relevant environment mechanisms. Retaining, deleting, merging, clarifying, narrowing, relocating, and supplementing them are all valid outcomes. Generalize the decision method while keeping each recommendation within its supported scope.

The default trigger is non-trivial task closure. An explicit retrospective or context review can also examine a stable work unit while other work remains open. Unresolved diagnosis limits only conclusions that depend on it; the retrospective does not take over unfinished work or run new domain experiments.

Anchor the review in the current task. Consult relevant, traceable prior evidence only when needed and within existing access and scope. Review environment mechanisms insofar as they affect context use or execution feedback; ordinary domain work remains in its owning task. This skill does not compress conversations. Do not route its output into memory workflows unless the user explicitly asks.

## Decision process

1. Set the review frame around the outcome or decision, the minimum complete decision span needed to explain it, and the outer evidence boundary. If the final state is insufficient, trace only the earlier context that could change the conclusion.
2. Identify an evidenced environment context problem and the future decision or execution outcome a change could improve. Use observation examples as optional, non-exhaustive starting points, selecting candidates by evidence and mechanism. Failure alone does not justify a durable change.
3. Inspect existing guidance, information sources, tools, or feedback mechanisms, including authority, availability, actionability, integration, consistency, and handoffs. Suitable wording or a mechanism alone does not prove an execution problem.
4. Determine supported scope and select a remedy for the evidenced mechanism, then choose its ownership, loading or activation time, and smallest effective change.
5. Use independent review only for material unresolved questions or an applicable review requirement. Keep evidence uncertainty, dispatch authorization, and capability separate.
6. Present a proportionate recommendation with its evidence, boundary, benefit, cost, and any relevant reconsideration condition.

A new skill needs an independently invocable workflow. Guidance and environment mechanisms belong at their matching scope; choose a remedy by its mechanism and expected benefit rather than a fixed file type or preference for wording or automation.

## Approval and output

Propose changes before applying them. Approval of a concrete scope authorizes its changes and appropriate verification without repeated confirmation. Subagent review requires an explicit user request or standing project authorization.

Prefer zero or one recommendation when sufficient, with no quota or fixed cap. If nothing qualifies, explain briefly when the user explicitly requested a review; otherwise finish without a retrospective section.

For changes that depend on changing tools, environments, processes, or responsibilities, identify what would make them obsolete or require reconsideration. This does not start a monitoring workflow.

## Runtime resources

- [Context trace](../../../.agents/skills/closure-retrospective/references/context-trace.md): read when the final state alone cannot explain how context or an environment mechanism affected the outcome.
- [Decision rubric](../../../.agents/skills/closure-retrospective/references/decision-rubric.md): read after existing coverage has been inspected and a candidate survives.
- [Independent review](../../../.agents/skills/closure-retrospective/references/independent-review.md): read only when review could materially change an unresolved consequential decision.
- [Output guidance](../../../.agents/skills/closure-retrospective/references/output-template.md): read for surviving proposals or pending review.

## Verification

Repository checks cover package layout and documentation discovery. Format and reference checks establish structural validity; they do not prove better decisions or execution in later tasks. Report applied changes, completed checks, and observed behavioral effects separately.
