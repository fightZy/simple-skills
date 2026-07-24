# Lifecycle Tests

A proposed intervention begins as a hypothesis. Writing it, building it, or passing local checks does not prove that it improves later work.

## State the hypothesis

Record:

```text
If <intervention> is available at <authoritative owner>, then a fixed worker will
<observable behavior change> on <representative job>, because <mechanism>.

Evidence that supports this:
Evidence that would weaken this:
Claim boundary and expected outcome:
Carrying cost and owner:
Reconsideration trigger and retirement condition:
```

Match proof effort to consequence and carrying cost. A low-risk routing clarification may need a focused fresh use; a cross-cutting control, architecture change, or consequential runbook needs stronger target-native and real-outcome evidence.

## Compare later behavior

When safe and authorized:

1. Preserve a baseline from a known task or run a representative job before the intervention.
2. Apply and locally validate the intervention through the target's normal workflow.
3. Run a fresh trajectory with the fixed worker, materially equivalent starting state, authority envelope, and external conditions.
4. Confirm that the intervention was actually retrieved or invoked. Unused context or tooling receives no credit.
5. Verify target-native contracts and the user or operational claim boundary separately.
6. Compare accepted outcome, human relay, repeated steering, retries, review convergence, risk, latency, and maintenance cost.
7. When uncertainty and risk justify it, use ablation or a test-without condition to check whether target-local evidence already supplies the behavior.

Do not overclaim from one before-and-after pair. It supports a bounded operational result, not a general causal estimate across workers and environments.

## Lifecycle states

- **Provisional:** The mechanism and placement survive review, but later effect evidence is pending.
- **Retain:** A fresh trajectory used the intervention, improved the bounded outcome at the claim boundary, and justified its carrying cost.
- **Revise:** The governing gap and owner appear correct, but retrieval, usability, precision, or proof remains weak.
- **Consolidate:** A stronger upstream owner now covers the requirement; migrate remaining cases and retire redundant guidance or controls.
- **Remove:** The intervention adds noise, overfits, duplicates a better owner, fails ablation, or repeatedly does not improve the job.

Record the state with its evidence, owner, follow-up case, reconsideration trigger, and retirement condition. A changed worker, requirement, architecture, authoritative source, or external risk can reopen qualification.

## Continuous-loop handoff

For a `Continuous maintenance` verdict, the follow-up must also define durable run states such as nothing needed, candidate proposed, change proved, approval requested, recovery required, and policy obsolete. Repeated rediscovery of the same facts indicates missing durable state.
