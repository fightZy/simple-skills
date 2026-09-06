# Closure Retrospective

This maintainer overview is outside the runtime package. The authoritative entrypoint is [SKILL.md](../../../.agents/skills/closure-retrospective/SKILL.md).

## Purpose and scope

Use existing work evidence to improve durable guidance and the future decisions it supports. Retaining, deleting, merging, clarifying, narrowing, relocating, and supplementing guidance are all valid outcomes. Generalize the decision method while keeping each recommendation within its supported scope.

The default trigger is non-trivial task closure. An explicit retrospective or context review can also examine a stable work unit while other work remains open. Unresolved diagnosis limits only conclusions that depend on it; the retrospective does not take over unfinished work or run new domain experiments.

Anchor the review in the current task. Consult relevant, traceable prior evidence only when needed and within existing access and scope. This skill does not compress conversations. Do not route its output into memory workflows unless the user explicitly asks.

## Decision process

1. Identify an evidenced context problem and the future decision a change could improve. Failure alone does not justify more instructions.
2. Inspect existing guidance, authority, and availability. Existing coverage prevents redundant additions while still allowing useful cleanup.
3. Determine scope and loading time before choosing the smallest effective edit and its exact target.
4. Use independent review only for material unresolved questions or an applicable review requirement. Keep evidence uncertainty, dispatch authorization, and capability separate.
5. Present a proportionate recommendation with its evidence, boundary, benefit, cost, and any relevant reconsideration condition.

A new skill needs an independently invocable workflow. Project guidance belongs at its matching scope; neither file type takes precedence over the other.

## Approval and output

Propose edits before applying them. Approval of a concrete scope authorizes its edits and appropriate verification without repeated confirmation. Subagent review requires an explicit user request or standing project authorization.

Prefer zero or one recommendation when sufficient, with no quota or fixed cap. If nothing qualifies, explain briefly when the user explicitly requested a review; otherwise finish without a retrospective section.

For guidance that depends on changing tools, environments, processes, or responsibilities, identify what would make it obsolete or require reconsideration. This does not start a monitoring workflow.

## Runtime resources

- [Decision rubric](../../../.agents/skills/closure-retrospective/references/decision-rubric.md): read after existing coverage has been inspected and a candidate survives.
- [Independent review](../../../.agents/skills/closure-retrospective/references/independent-review.md): read only when review could materially change an unresolved consequential decision.
- [Output guidance](../../../.agents/skills/closure-retrospective/references/output-template.md): read for surviving proposals or pending review.

## Verification

Repository checks cover package layout and documentation discovery. Format and reference checks establish structural validity; they do not prove better decisions in later tasks. Report applied edits, completed checks, and observed behavioral effects separately.
