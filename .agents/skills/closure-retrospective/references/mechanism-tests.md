# Mechanism Tests

Apply every test before inspecting a target artifact. A reusable mechanism is an evidence-supported relationship explaining why a controllable decision tends to cause, protect, or improve an outcome. It may come from failure, success, scope preservation, or efficiency.

## Required Tests

1. **Support:** Name the observed decision and outcome. Use `Drop` when the evidence shows only that one followed the other, not why they are related.
2. **Pre-outcome action:** State a trigger observable before the outcome, an action the agent controls, and the signal that verifies the action resolved the decision.
3. **Structural transfer:** Identify two materially different situations within the intended reuse scope that share the same decision structure. Shared filenames, commands, tools, or error text alone do not establish transfer.
4. **Boundary:** Name a limiting condition or non-applicable situation. Guidance without a boundary is not ready to codify.
5. **Abstraction altitude:** Remove incidental task nouns. Keep the domain terms that define the target scope. The remaining guidance must still prescribe a concrete action; `be careful`, `check`, `consider`, and equivalent morals fail this test.
6. **Counterfactual:** Ask whether having the guidance at the start of the task would have changed an action before the outcome. Guidance that only improves the explanation after the fact fails this test.

Complete the synthesis only when the candidate has all four parts:

`evidence -> mechanism -> trigger/action/verification -> boundary`
