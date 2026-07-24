---
name: closure-retrospective
description: Distill evidence from a substantively completed non-trivial task into a reusable mechanism and the smallest durable intervention that should shape later work. Use when repeated corrections, tool or context friction, sequencing loops, stable scope decisions, successful judgment, incidents, or accepted and rejected outcomes may justify changes to context, skills, runbooks, examples, reviews, evaluations, types, APIs, tools, tests, lints, architecture, migrations, or continuous maintenance.
---

# Closure Retrospective

## Core Principle

Treat an observed outcome as evidence, not as a rule. Promote only an evidence-supported reusable mechanism into the earliest semantic owner that can change a later decision. The durable result is a more coherent environment with fewer repeated relays and redundant controls, not another instruction by default.

Raw trajectory material and agent self-reports are low-trust telemetry. Keep them attached to the run, corroborate them against diffs, tool output, checks, review, runtime evidence, and accepted outcomes, and never inject them directly into future context.

## Closure Gate

Run this skill only after the substantive task is complete or clearly entering final handoff. If implementation, debugging, research, product intent, architecture, or the acceptance boundary remains unresolved, finish or escalate that work first.

Drop trivial work, one-off preferences, temporary debugging notes, unsupported interpretations, and findings whose only evidence is an agent self-report.

## Workflow

1. **Build an evidence packet.** Record the promised outcome, observable trajectory, intervention or decision, result, proof, human steering, and accepted or rejected status. Preserve provenance and separate observation from interpretation.
2. **Recover the governing class.** Trace the outcome to the earliest failed or protected handoff, identify the controllable pre-outcome decision, and search for bounded sibling cases governed by the same principle. Separate a harness gap from worker variance, external failure, and a bad premise.
3. **Extract the reusable mechanism.** Read [references/mechanism-tests.md](references/mechanism-tests.md) and apply every test before inspecting possible targets. Continue only when the candidate can be expressed as `evidence -> mechanism -> trigger/action/verification -> boundary`.
4. **Route the intervention.** Read [references/intervention-routing.md](references/intervention-routing.md). Match lesson maturity and consequence to the earliest semantic owner; do not default to prose. For repository guidance, begin with applicable `AGENTS.md` or `CLAUDE.md` files and follow only relevant explicit authority pointers to the final authoritative artifact. Stop on cycles, ambiguity, or missing ownership.
5. **Design for system convergence.** Name the backward path for the existing population, the forward ratchet for later work, and any weaker guidance or controls that the proposed owner could make redundant. Use `Not applicable` only with a concrete reason.
6. **Decide and bound the lifecycle.** Apply every gate in [references/decision-rubric.md](references/decision-rubric.md), then read [references/lifecycle-tests.md](references/lifecycle-tests.md). State the intervention hypothesis, current evidence level, follow-up proof, owner, carrying cost, reconsideration trigger, and retirement condition. A newly proposed intervention is `Provisional` until later evidence supports retention.
7. **Present the result.** If at least one candidate survives, read [references/output-template.md](references/output-template.md) and present at most three independent recommendations. Match the user's language.

## Output Behavior

- When the user explicitly requests a retrospective and nothing qualifies, output only a title, `Worth codifying: no`, and one sentence naming the failed gate.
- When the retrospective is implicit and nothing qualifies, surface no retrospective section.
- Keep this phase read-only. Present proposed interventions and wait for explicit approval before editing. Later approval authorizes only the named targets and insertion points.

## Hard Boundaries

- Do not treat raw telemetry, memory, existing guidance, or the proposed repair as evidence for the mechanism. Do not propose or update memory unless the user explicitly requests it.
- Do not create a new skill when an existing owner can absorb the mechanism cleanly.
- Do not encode contextual judgment as a deterministic control merely because it can be checked mechanically.
- Do not recommend a maintenance loop until the desired condition, signal, proof, authority, durable state, and retirement condition are settled.
- Do not claim an intervention works because it was written, built, or locally validated; later behavior and claim-boundary evidence decide retention.
- Prefer `Retain as evidence` or `Drop` over incident-specific guidance and prefer consolidation over accumulating parallel controls.
