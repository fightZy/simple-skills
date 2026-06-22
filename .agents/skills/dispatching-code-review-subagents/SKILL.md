---
name: dispatching-code-review-subagents
description: Use when preparing to delegate code review to subagents — after implementation milestones, before merging complex changes, or when the diff spans multiple domains.
---

# Dispatching Code Review Subagents

Core principle: split review only when independent reviewers can produce better signal than one reviewer. The main agent routes work and synthesizes results; it does not duplicate the reviewers' full review.

## Workflow

Execute these steps in order. Do not skip steps. Do not stop after synthesis.

```
Step 1: Scope       — Inspect diff, decide reviewer count and review lenses.
Step 2: Review      — Dispatch reviewer subagents in parallel.
Step 3: Synthesize  — Deduplicate findings, merge, spot gaps.
Step 4: Verify      — 4a: classify & plan; 4b: verify per 4a plan, produce report-ready fields; 4c: for subagent output only, confirm exists & sanity-check, filter rejected.
Step 5: Report      — Assemble verifier output into report table, no re-judgment.
```

## When NOT to Use This Skill

- The diff is trivial (typo, missing import, single-line config) — review inline directly.
- No subagent dispatch capability is available.
- A single localized change with no cross-domain risk — one quick self-review suffices.

## Decide Reviewer Count

**One reviewer** when the diff is small, localized, or owned by one domain. **Multiple in parallel** when the change spans independent domains, distinct lenses would produce different findings, or the diff is large enough that one reviewer would sample instead of inspect.

Use layered review only when one pass changes the next (e.g., correctness findings reshape how a second reviewer examines tests). If passes are independent, run in parallel.

## Choose Review Lenses

Determine which perspectives produce the most valuable, non-overlapping findings. If two lenses would find the same issues, merge them. Each reviewer should have a mission no other covers.

**Example lenses** (adapt or invent as needed): architectural fit, correctness/contracts, concurrency/state, security, data integrity, test quality, performance, UX/product behavior.

The right number is the minimum that covers the risk surface. Avoid sending every reviewer the same generic prompt — duplicate prompts produce duplicate noise.

## Main Agent Contract

The main agent **owns**: inspecting context to choose scopes/lenses, writing bounded prompts with explicit file paths and output format, running independent reviewers in parallel, deduplicating findings, calling out conflicts and gaps, and dispatching verification.

The main agent **does not**: re-review every line after subagents report, treat reviewer agreement as proof when both saw incomplete context, or stop after synthesis without verification.

## Reviewer Prompt Shape

Use a concrete brief:

```text
Review [files/area] for [theme/lens].
Prioritize bugs, regressions, and missing tests over style.
Return findings with file/line references, a short rationale, and an initial severity assessment (Critical/High/Medium/Low) based on the diff and available context.
Mention important gaps if the available context is insufficient.
```

Reviewers must give a grounded severity assessment, not vague hints. 

## Synthesis Output

Return one consolidated review:

- Merge duplicates under the strongest rationale.
- Preserve file/line references.
- Separate disagreements and missing context.
- Keep cleanup suggestions non-blocking unless they create real risk.

Note: Preserve reviewer severity assessments through synthesis — they are grounded initial judgments, not placeholders. Verifier (Step 4b) re-checks against actual source code and may confirm or correct.

## Verification Phase (Step 4)

Reviewers produce hypotheses, not facts. **Verification is mandatory** — "skip subagent dispatch" means verify inline (main agent reads cited code), not skip verification. The only trivial case: ALL findings self-evident from diff AND reviewer cited exact lines (typo, missing import) — even then, confirm each line.

### Step 4a: Classify & Plan — HARD GATE

**Produce the classification table below before any verification action.** If you are reading source or dispatching verifiers without this table, STOP — go back and classify. Every finding must be classified; unclassified = unverified. Do not proceed to 4b until the table is complete.

| Depth | Definition | Verify Strategy |
|-------|-----------|-----------------|
| **Shallow** | Line/function-level, ≤2 files | **Inline** — main agent reads lines directly (verifier = `self`); no subagent |
| **Deep** | Call-chain / cross-module, 3+ layers or files | Dedicated verifier per independent chain |

Also tag: **Packages** (which to read) and **Confidence** (High if multiple reviewers agree, Low if single-source). Low-confidence findings **must** be verified.

**Then decide verifier count** (after classification): all Shallow → self-inline. Homogeneous Deep → one verifier batching all. Independent chains or mixed packages → split by package then by chain. If plan yields more verifiers than findings, merge — review was over-split upstream.

Write one split-rationale line:

> Dispatching N verifier(s) [or "self-inline"]: V1 covers [packages/depth], V2 covers ...

Output the plan (gate artifact):

| Verifier | Finding IDs | Packages | Depth | Confidence | Rationale |
|----------|-------------|----------|-------|------------|-----------|

### Step 4b: Dispatch & Verify

Each verifier reads **actual source code** (not the diff) and confirms or rejects each finding. The verifier's structured output is the **direct input to the final report** — it must produce report-ready fields, not just yes/no:

```text
You are verifying code review findings. Read the actual source code and confirm each:
1. Does the issue actually exist? (cite exact file:line + code snippet)
2. How severe is the real-world impact? What scenario triggers it?

**Project root:** [path]

### Finding N: [title]
- **Claim:** [what the reviewer said]
- **Read:** [specific files to check]

**For each finding, return:**
- **Exists?** Yes / No / Uncertain (with exact code evidence or what's missing)
- **Severity** (if exists): Critical / High / Medium / Low
- **Impact** (if exists): trigger scenario + magnitude (1 sentence, e.g., "Network jitter causes repeated toast popups, blocking interaction for 10s+")
- **Fix Clarity** (if exists): Actionable (1-line fix description) / Needs Discussion (option A vs option B + key tradeoff)
```

If a verifier marks a finding **Uncertain**, you MAY dispatch one follow-up verifier scoped to that single finding only. At most one re-verification round. Do not re-dispatch the full batch.

### Step 4c: Confirm & Filter

Review verifier output. The 4c path depends on 4a classification:

**For Shallow (inline self-verified):** Main agent already read source and produced Severity/Impact/Fix Clarity directly — no third-party output to sanity-check. Skip 4c confirmation; these findings go straight to Step 5.

**For Deep (subagent verified):** Review each verifier's structured output:

1. **Exists? = No** → Reject. List under "Rejected" with verifier's one-line rationale.
2. **Exists? = Uncertain** → Dispatch follow-up verifier per Step 4b rules. Do not report directly.
3. **Exists? = Yes** → Sanity-check the three fields:
   - **Severity**: Does it match the Impact description? Correct and note reason if clearly over/understated.
   - **Impact**: Is the scenario and magnitude verifiable? Reject or downgrade exaggerated or unsupported claims.
   - **Fix Clarity**: If Actionable, confirm the fix path is feasible. If Needs Discussion, confirm real tradeoffs exist (not just missing info).

4c is still verification logic for subagent output — judging whether findings are real and whether severity/impact hold up. It is not passive passthrough. Confirmed fields become Step 5 report input; Step 5 does not re-judge.

## Step 5: Report (Reporting Phase)

Assemble 4c-confirmed output into the report table. **Do not re-judge severity, impact, or fix clarity** — 4c already confirmed these. Your job is to assemble, sort, and present.

Sort by severity (Critical → Low), then Fix Clarity (Actionable → Needs Discussion).

| # | Issue | Severity | Impact | Fix |
|---|-------|----------|--------|-----|
| 1 | Toast retry has no debounce | High | Network jitter causes repeated toast popups, blocking interaction 10s+ | [Actionable] Add debounce + max retry count |

Rules:

- **Issue**: Factual description of what the problem is (no cause, no fix).
- **Severity**: 4c-confirmed Critical/High/Medium/Low.
- **Impact**: 4c-confirmed Impact, explains why this severity.
- **Fix**: 4c-confirmed Fix Clarity — prefix `[Actionable]` or `[Needs Discussion]`. Do not implement unless the user asks.
- Rejected findings: list separately as "Rejected" with one-line rationale.

This closes the workflow. Do not start another full review loop over findings unless the user requests it.

## Rationalizations to Reject

| Excuse | Reality |
|--------|---------|
| "Findings look obvious" | Obvious to reviewer ≠ verified. Read the cited code. |
| "I cross-checked during synthesis" | Synthesis deduplicates; it does not confirm against source. |
| "I read the source, so verification is done" | Reading source ≠ classified + dispatched. Produce the 4a table first. |
| "Diff is small, verification is waste" | Small diffs still ship regressions. |
| "Both reviewers agreed" | Agreement proves nothing when both saw incomplete context. |
| "Skip the plan table, just verify" | The plan prevents over-dispatch and missed findings. |
| "Re-bucket findings in 4c" | 4c sanity-checks reality and reasonableness, not re-ranks. But verifier output that is clearly off must be corrected. |
| "4c only filters, no verification" | 4c is still verification — confirming Exists and checking Severity/Impact hold. Passive passthrough is a failure. |
| "Re-judge severity in the report" | The report assembles 4c-confirmed output. Do not override without reason. |
| "One small fix, re-run full review" | Patch and verify only that item, not the whole loop. |

## Red Flags

Stop and resize when:

- Review setup takes longer than the review itself.
- Reviewers have overlapping generic missions.
- Main agent does a full independent review after receiving results.
- One small fix triggers another full review loop.
- Verification proceeds without the 4a table, or Deep findings are inline-verified by main agent.
