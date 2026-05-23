---
name: dispatching-code-review-subagents
description: Use when preparing to delegate code review to subagents, especially after implementation milestones, before merging complex changes, or when review scope may need thematic or layered parallel review.
---

# Dispatching Code Review Subagents

Core principle: split review only when independent reviewers can produce better signal than one reviewer. The main agent routes work and synthesizes results; it does not duplicate the reviewers' full review.

## Decide Reviewer Count

Use one reviewer when:

- The diff is small, localized, or owned by one domain.
- The risk is mostly generic correctness.
- Splitting would cost more than the review value.

Use multiple reviewers in parallel when:

- The change spans independent domains, packages, or workflows.
- Distinct lenses matter: contract, security, persistence, UI, tests, migrations, docs.
- The diff is large enough that one reviewer would likely sample instead of inspect.

Use layered review only when one pass changes the next pass:

- First: correctness, contract, data loss, security, migrations.
- Second: maintainability, test quality, ergonomics, docs, performance, cleanup.

If the second layer does not depend on first-layer findings, run reviewers in parallel by theme.

## Split By Theme

Give each reviewer a non-overlapping mission:

- Behavior and contracts: regressions, edge cases, API compatibility.
- Data and state: persistence, migrations, transactions, concurrency.
- Security and safety: auth, input handling, secrets, privilege boundaries.
- Tests: missing coverage, weak assertions, flaky paths.
- UI and product behavior: flows, accessibility, responsive layout, confusing states.
- Maintainability: coupling, unnecessary abstraction, local pattern mismatches.

Avoid sending every reviewer the same generic prompt. Duplicate prompts produce duplicate noise.

## Main Agent Contract

The main agent owns only:

1. Inspecting enough context to choose scopes.
2. Writing bounded prompts with explicit file paths, risk lens, and output format.
3. Running independent reviewers in parallel when scopes are independent.
4. Deduplicating findings and ordering by severity.
5. Calling out conflicts, low-confidence claims, and gaps.

The main agent does not:

- Re-review every line after subagents report.
- Run multiple review rounds for small fixes that can be batch-verified.
- Treat reviewer agreement as proof when both saw the same incomplete context.

## Reviewer Prompt Shape

Use a concrete brief:

```text
Review [files/area] for [theme].
Prioritize bugs, regressions, and missing tests over style.
Return findings first, ordered by severity, with file/line references and a short rationale.
Mention important gaps if the available context is insufficient.
```

## Synthesis Output

Return one consolidated review:

- Findings first, sorted by severity.
- Merge duplicates under the strongest rationale.
- Preserve file/line references.
- Separate disagreements and missing context.
- Keep cleanup suggestions non-blocking unless they create real risk.

## Red Flags

Stop and resize the review plan when:

- Review setup takes longer than the likely review itself.
- Reviewers have overlapping generic missions.
- The main agent starts doing a full independent review after receiving results.
- One small fix triggers another full review loop.
