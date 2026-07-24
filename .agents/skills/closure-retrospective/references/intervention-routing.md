# Intervention Routing

Choose the intervention by lesson maturity, consequence, and earliest semantic owner. Do not choose a surface merely because it is easy to edit.

## Maturity ladder

| Intervention | Use when |
| --- | --- |
| Prompt adjustment and reroll | Task framing or the desired outcome is still being discovered; do not promote it yet |
| Routing document, skill, or runbook | Stable context must appear at a particular decision point |
| Blessed example | Accepted work carries information-dense taste, structure, or boundary decisions that prose cannot enumerate |
| Reviewer or evaluation | Judgment is qualitative, cross-cutting, consequential, or still gaining nuance |
| Type, API, or domain tool | A settled model or operation can make correct use natural and misuse difficult |
| Lint, test, or policy check | A deterministic invariant should return actionable feedback and block recurrence |
| Architecture or migration | Repeated defects expose the wrong owner, representation, dependency direction, or compatibility path |
| Maintenance loop | A settled condition must remain true while the repository, ecosystem, or external system changes |

Move upward in constraint only as evidence and maturity justify it. Keep contextual judgment in guidance, examples, and review. Move settled invariants into executable owners. Remove downstream defenses when a stronger upstream owner faithfully covers the requirement.

## Find the owner

1. Name the invariant or judgment and the decision point it governs.
2. Trace the symptom to the earliest boundary able to prevent, expose, or naturally represent it.
3. Use applicable repository instructions and explicit authority pointers to locate the real owner. Do not invent ownership from filenames or proximity.
4. Inspect only the bounded sibling population governed by that owner.
5. Name one target and ownership point. Stop and recommend clarification when ownership is ambiguous, cyclic, or missing.

For guidance reached through `AGENTS.md` or `CLAUDE.md`, update the final authoritative artifact rather than duplicating detail into routing files. For types, APIs, tools, checks, or architecture, name the concrete package, schema, command, suite, rule, or boundary that owns the behavior.

## Require two paths

Every promoted intervention needs both paths unless one is concretely inapplicable:

- **Backward path:** find the existing population governed by the principle, migrate or classify it, preserve legitimate exceptions, and remove contradictory precedent.
- **Forward path:** place a ratchet at the earliest reliable point so later work retrieves the judgment or receives actionable feedback before acceptance.

Also identify guidance, validators, exceptions, or migration machinery that become redundant. Coverage of known classes should accumulate while control count consolidates.

## Route changing conditions to a loop

Use a maintenance loop only when these are settled:

- the condition that should remain true;
- the drift signal and authoritative state;
- proof that a candidate restores the real condition;
- autonomous actions and approval boundaries;
- durable state carried to the next run; and
- escalation, recovery, completion, and retirement conditions.

If product intent, interface, architecture, or acceptance remains unresolved, route the result to investigation, a proposal, or human judgment instead of automation.
