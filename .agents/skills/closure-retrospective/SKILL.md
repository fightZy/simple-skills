---
name: closure-retrospective
description: "Optimize agent environment context at task closure or on explicit review requests, using existing work evidence; propose scoped changes that improve future decisions or execution."
---

# Closure Retrospective

Use stable work evidence to optimize how an agent obtains, finds, interprets, and uses context and execution feedback. Choose the smallest justified change to the relevant guidance or environment mechanism. Improve future decisions or execution at justified context and maintenance cost. Generalize the decision method, not every resulting rule.

## Boundaries

- Default to non-trivial task closure. An explicit retrospective or context review may examine a stable work unit even when other work remains open.
- Use existing evidence. Do not expand the task, change evidence access, or run new domain experiments to justify a lesson.
- Anchor the review in the current task. When necessary, consult only relevant, traceable prior evidence within existing access and task scope; distinguish its source and applicability. Do not default to broad history searches.
- Unresolved diagnosis limits only conclusions that depend on it. This skill does not resume or take over unfinished work.
- Review environment mechanisms insofar as they affect context use or execution feedback; ordinary domain work remains in its owning task. This skill does not govern conversation compression or memory. Do not route output into memory workflows unless the user explicitly asks.
- Propose changes before applying them. Explicit approval of the proposed scope authorizes those changes and appropriate verification; reuse that approval while it remains applicable. Invoking a retrospective alone does not authorize changes.

## Workflow

### 1. Set the review frame

Identify the outcome or decision under review, the minimum complete decision span needed to explain it without omitting materially relevant prior context, and the outer evidence boundary. Completeness sets the lower bound; material relevance sets the upper bound. Do not assume that the latest change represents the whole context problem. When competing review frames would materially change the conclusion and cannot be resolved from the request or existing evidence, ask the user; otherwise state the chosen frame and proceed.

When the final state alone cannot explain how context or an environment mechanism affected the outcome—for example, a relevant decision changed, explanations conflict, or the relationship between the environment and outcome remains unclear—read [references/context-trace.md](references/context-trace.md). Keep the trace limited to decisions, actions, and evidence that could change the retrospective conclusion.

Completion criterion: the review has an explicit subject, a justified evidence span, and enough history to assess context without broadening into an unrestricted task history.

### 2. Identify a context problem

Identify environment context improvement opportunities from relevant evidence in the current task, using optional observation directions that include, but are not limited to, information supply, discoverability of entry points, context organization and loading, tool outputs, execution feedback, and repeated costs, and select candidates by their problem mechanism and expected decision or execution improvement.

For each candidate, connect the observation, the suspected or demonstrated contribution of context or an environment mechanism, and a specific future decision or execution outcome that a change would improve. A failed outcome, tool limitation, or execution mistake alone does not justify a durable change.

Completion criterion: every surviving candidate has evidence, an identified problem mechanism, and a concrete decision or execution improvement; otherwise use the no-change outcome in step 6.

### 3. Inspect existing coverage

Inspect the exact relevant guidance, information sources, tools, or feedback mechanisms, their authority, and how and when they are available to the agent. Distinguish a content or capability gap from a scope, discoverability, integration, or execution problem before proposing a remedy.

The existence of suitable wording or a mechanism does not by itself establish an execution problem. Check whether it was available at the relevant point, actionable, consistent with other applicable context, connected to the workflow, and carried through relevant handoffs.

Retain effective guidance and mechanisms. Existing coverage rules out redundant additions, but does not by itself rule out cleanup of duplication, conflict, stale content, or ineffective integration. Identify the authoritative source or mechanism to adjust; drop changes unlikely to improve the decision or execution.

Completion criterion: every surviving candidate names an evidenced environment context problem and its existing coverage, including absence of a suitable artifact or mechanism when verified.

### 4. Calibrate scope and choose the smallest change

Read [references/decision-rubric.md](references/decision-rubric.md) for surviving candidates. Determine supported scope, select a remedy for the evidenced mechanism, then choose its ownership, loading or activation time, and smallest change. Deletion, consolidation, relocation, and additions are all valid outcomes.

Completion criterion: each proposal has an exact target and change, supported scope and loading or activation conditions, a justified benefit over its costs, and a reconsideration condition when it depends on changeable assumptions.

### 5. Resolve material uncertainty

After coverage and scope are clear, decide whether independent review could materially change an unresolved, consequential decision. Read [references/independent-review.md](references/independent-review.md) only then; routine retention, relocation, or clarification normally needs no such review.

Dispatch subagents only when the user explicitly asks for subagent review or standing project instructions authorize it. Record review need, authorization, and availability separately. Evidence uncertainty limits conclusions; unavailable or unauthorized review is a process status, not evidence against an established fact.

Completion criterion: each proposal is ready, pending required review, or dropped. Narrowing may resolve uncertainty, but cannot waive an independently required review.

### 6. Present the decision

When nothing qualifies, finish normally; if the user explicitly requested the review, briefly explain why no change is warranted.

For surviving proposals or pending review, read [references/output-template.md](references/output-template.md). Present enough detail to review the proposed change and determine the next authorized action. Keep proposed changes, applied changes, and completed verification distinct.

Completion criterion: the user can assess the concrete change, its boundaries and costs, and any unresolved decision without reading the internal checklist.
