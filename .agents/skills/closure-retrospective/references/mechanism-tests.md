# Mechanism Tests

Apply every test before inspecting a target artifact. A reusable mechanism is an evidence-supported relationship between the context available at a recurring decision point, the action it shaped, and the outcome. It may show that the context should change, remain available, or be retired.

## Required Tests

1. **Support:** Name the context actually available, the observed action, and the outcome. Use `Drop` when the evidence shows only that one followed another, not how the context influenced the decision.
2. **Decision-time influence:** State the recurring decision point, the relevant context state at that moment, the action the worker controls, and the signal that verifies the decision was resolved.
3. **Structural transfer:** Identify two materially different situations within the intended reuse scope that share the same decision structure. Shared filenames, commands, tools, or error text alone do not establish transfer.
4. **Boundary:** Name a limiting condition or non-applicable situation. Guidance without a boundary is not ready to codify.
5. **Abstraction altitude:** Remove incidental task nouns. State the desired context as a decision-relevant condition, not a list copied from the case. Keep terms that define a real scope boundary or concrete action; `be careful`, `check`, `consider`, and equivalent morals fail this test.
6. **Counterfactual:** Ask whether encountering the desired context state at the decision point would have changed or preserved an action before the outcome. A proposal that only improves the explanation after the fact fails this test.

Complete the synthesis only when the candidate has all five parts:

`evidence -> context influence -> desired future context -> smallest durable change -> boundary`
