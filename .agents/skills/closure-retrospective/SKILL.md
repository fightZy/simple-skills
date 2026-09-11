---
name: closure-retrospective
description: "Review durable guidance at task closure, or when explicitly asked to optimize reusable context using existing work evidence; propose changes to content, scope, or loading."
---

# Closure Retrospective

Use stable work evidence to decide whether durable guidance should be retained, removed, merged, clarified, scoped, relocated, or supplemented. Improve future decisions at justified context and maintenance cost. Generalize the decision method, not every resulting rule.

## Boundaries

- Default to non-trivial task closure. An explicit retrospective or context review may examine a stable work unit even when other work remains open.
- Use existing evidence. Do not expand the task, change evidence access, or run new domain experiments to justify a lesson.
- Anchor the review in the current task. When necessary, consult only relevant, traceable prior evidence within existing access and task scope; distinguish its source and applicability. Do not default to broad history searches.
- Unresolved diagnosis limits only conclusions that depend on it. This skill does not resume or take over unfinished work.
- This skill governs durable guidance, not conversation compression or memory. Do not route output into memory workflows unless the user explicitly asks.
- Propose guidance edits before applying them. Explicit approval of the proposed scope authorizes those edits and appropriate verification; reuse that approval while it remains applicable. Invoking a retrospective alone does not authorize edits.

## Workflow

### 1. Set the review frame

Identify the outcome or decision under review, the minimum complete decision span needed to explain it without omitting materially relevant prior context, and the outer evidence boundary. Completeness sets the lower bound; material relevance sets the upper bound. Do not assume that the latest change represents the whole context problem. When competing review frames would materially change the conclusion and cannot be resolved from the request or existing evidence, ask the user; otherwise state the chosen frame and proceed.

When the final state alone cannot explain how context affected the decision—for example, a relevant decision changed, explanations conflict, or the relationship between guidance and outcome remains unclear—read [references/context-trace.md](references/context-trace.md). Keep the trace limited to decisions and evidence that could change the retrospective conclusion.

Completion criterion: the review has an explicit subject, a justified evidence span, and enough history to assess context without broadening into an unrestricted task history.

### 2. Identify a context problem

Look for evidence that context influenced a decision that could recur. Common signals include missing, repeated, conflicting, stale, overly broad, or poorly timed guidance. Ask what helped, what obstructed, and what was missing.

For each candidate, connect the observation, the suspected or demonstrated contribution of context, and a specific future decision that a change would improve. A failed outcome, tool limitation, or execution mistake alone does not justify more instructions.

Completion criterion: every surviving candidate has evidence and a concrete decision improvement; otherwise use the no-change outcome in step 6.

### 3. Inspect existing coverage

Read the exact relevant guidance, its authority, and when it is available to the agent. Distinguish a content gap from a scope, discoverability, or execution problem before proposing a remedy.

The existence of suitable wording does not by itself establish an execution problem. Check whether the guidance was available at the decision point, concrete enough to act on, consistent with other applicable context, and carried through relevant workflow handoffs.

Retain effective guidance. Existing coverage rules out redundant additions, but does not by itself rule out cleanup of duplication, conflict, or stale content. Identify the authoritative content to adjust; drop changes unlikely to improve the decision.

Completion criterion: every surviving candidate names an evidenced context problem and its existing coverage, including absence of a suitable artifact when verified.

### 4. Calibrate scope and choose the smallest change

Read [references/decision-rubric.md](references/decision-rubric.md) for surviving candidates. Determine supported scope and loading time before choosing the artifact and edit. Deletion, consolidation, relocation, and additions are all valid outcomes.

Completion criterion: each proposal has bounded wording, an exact target and change, a justified benefit over its costs, and a reconsideration condition when it depends on changeable assumptions.

### 5. Resolve material uncertainty

After coverage and scope are clear, decide whether independent review could materially change an unresolved, consequential decision. Read [references/independent-review.md](references/independent-review.md) only then; routine retention, relocation, or clarification normally needs no such review.

Dispatch subagents only when the user explicitly asks for subagent review or standing project instructions authorize it. Record review need, authorization, and availability separately. Evidence uncertainty limits conclusions; unavailable or unauthorized review is a process status, not evidence against an established fact.

Completion criterion: each proposal is ready, pending required review, or dropped. Narrowing may resolve uncertainty, but cannot waive an independently required review.

### 6. Present the decision

When nothing qualifies, finish normally; if the user explicitly requested the review, briefly explain why no change is warranted.

For surviving proposals or pending review, read [references/output-template.md](references/output-template.md). Present enough detail to review the proposed change and determine the next authorized action. Keep proposed guidance, applied edits, and completed verification distinct.

Completion criterion: the user can assess the concrete change, its boundaries and costs, and any unresolved decision without reading the internal checklist.
