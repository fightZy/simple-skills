---
name: closure-retrospective
description: Improve the context that shapes future decisions using evidence from a substantively completed non-trivial task. Use when completed-task evidence shows that changing what later workers encounter at a recurring decision point could improve their action before the outcome, or that effective context should be preserved. Route the smallest durable context change to the earliest semantic owner and define how later behavior will validate or retire it.
---

# Closure Retrospective

## Core Principle

Use completed-task evidence to improve the context that shapes future decisions. Determine how the current context influenced the run, define the desired future context at the same decision point, and route the smallest durable change to the earliest semantic owner. Optimize decision quality and system coherence, not artifact count.

Treat context as everything the worker can legitimately use at the decision point: governing facts, boundaries, judgment criteria, authority, feedback, and executable structure. Do not equate context with prose. Treat an observed outcome as evidence, not as a rule.

Raw trajectory material and agent self-reports are low-trust telemetry. Keep them attached to the run, corroborate them against diffs, tool output, checks, review, runtime evidence, and accepted outcomes, and never inject them directly into future context.

## Closure Gate

Run this skill only after the substantive task is complete or clearly entering final handoff. If implementation, debugging, research, product intent, architecture, or the acceptance boundary remains unresolved, finish or escalate that work first.

Drop trivial work, one-off preferences, temporary debugging notes, unsupported interpretations, and findings whose only evidence is an agent self-report.

## Workflow

1. **Build an evidence packet.** Record the promised outcome, observable trajectory, intervention or decision, result, proof, human steering, and accepted or rejected status. Preserve provenance and separate observation from interpretation.
2. **Reconstruct the decision context.** Locate the recurring controllable decision before the outcome. Identify what context was legitimately available then, how it influenced the action, and which boundary materially constrained the decision. Search for structurally related sibling cases and separate context effects from worker variance, external failure, and a bad premise.
3. **Define the desired context and smallest change.** Read [references/mechanism-tests.md](references/mechanism-tests.md) and apply every test before inspecting possible targets. Describe the causal context effect rather than starting from a defect label or the incident's nouns. Continue only when the candidate can be expressed as `evidence -> context influence -> desired future context -> smallest durable change -> boundary`.
4. **Route the context change.** Read [references/intervention-routing.md](references/intervention-routing.md). Match lesson maturity and consequence to the earliest semantic owner; do not default to prose. For repository guidance, begin with applicable `AGENTS.md` or `CLAUDE.md` files and follow only relevant explicit authority pointers to the final authoritative artifact. Stop on cycles, ambiguity, or missing ownership.
5. **Design for system convergence.** Name the backward path for the existing population, the forward ratchet for later work, and anything the proposed owner could make redundant. Do not add an artifact when changing or retiring an existing owner would create the desired context more directly.
6. **Decide and bound the lifecycle.** Apply every gate in [references/decision-rubric.md](references/decision-rubric.md), then read [references/lifecycle-tests.md](references/lifecycle-tests.md). State the context-change hypothesis, current evidence level, follow-up proof, owner, carrying cost, reconsideration trigger, and retirement condition. A newly proposed change is `Provisional` until later evidence supports retention.
7. **Present the result.** If at least one candidate survives, read [references/output-template.md](references/output-template.md). Lead with what should change and why it should change before any supporting analysis. State the desired future context and its smallest owning change, then explain why the observed context effect justifies it. Present at most three independent recommendations and match the user's language.

## Output Behavior

- When the user explicitly requests a retrospective and nothing qualifies, output only a conclusion-led title, a recommendation not to codify, and one brief reason naming the failed gate. Match the user's language and do not use a fixed retrospective title.
- When the retrospective is implicit and nothing qualifies, surface no retrospective section.
- Do not expose rubric field names, empty fields, or the literal text Not applicable in the user-facing result. Put only decision-useful evidence, boundaries, delivery, proof, or lifecycle material in optional supporting analysis.
- Keep this phase read-only. Present proposed context changes and wait for explicit approval before editing. Later approval authorizes only the named targets and insertion points.

## Hard Boundaries

- Do not treat raw telemetry, memory, existing guidance, or the proposed repair as evidence for the mechanism. Do not propose or update memory unless the user explicitly requests it.
- Do not assume improvement means addition; optimize the context state encountered at the decision point and retire anything the chosen owner makes redundant.
- Do not create a new skill when an existing owner can absorb the mechanism cleanly.
- Do not encode contextual judgment as a deterministic control merely because it can be checked mechanically.
- Do not recommend a maintenance loop until the desired condition, signal, proof, authority, durable state, and retirement condition are settled.
- Do not claim a context change works because it was written, built, or locally validated; later behavior and claim-boundary evidence decide retention.
- Prefer `Retain as evidence` or `Drop` over incident-specific guidance and prefer consolidation over accumulating parallel controls.
