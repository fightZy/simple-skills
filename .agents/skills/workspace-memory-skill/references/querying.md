# Querying Workspace Memory

Use this guide when the user wants to recover context, inspect prior decisions, find norms, or answer "what do we already know about this?"

## Retrieval Goal

Optimize for the smallest useful read:
- start with the highest-signal summary
- stop as soon as the answer is reliable
- only open session files when summaries or crystals are insufficient

## Default Read Order

1. `docs/memory/index.md`
2. `docs/memory/summaries/recent.md`
3. relevant `docs/memory/summaries/topics/*.md`
4. relevant `docs/memory/crystals/*.md`
5. specific `docs/memory/sessions/...md`

If the repository uses a different root, adapt the same order to that layout.

## Query Types

### Experience or prior implementation

Goal:
- find how similar work was done before
- recover rationale, pitfalls, or follow-up context

Read order:
1. `summaries/recent.md`
2. topic summaries related to the area
3. `crystals/implementation-patterns.md`
4. specific session files linked from those summaries

Stop when:
- a pattern and its tradeoff are already clear

Go deeper when:
- the summary mentions disagreement, unresolved tradeoffs, or a superseded approach

### Summary or current state

Goal:
- understand what is active now
- recover recent priorities and unresolved work

Read order:
1. `summaries/recent.md`
2. the newest session files only if needed

Stop when:
- you can state current priorities, recent changes, and pending follow-ups confidently

### Norms, conventions, or project rules

Goal:
- find what contributors should do by default

Read order:
1. `crystals/team-conventions.md`
2. `crystals/project-decisions.md`
3. supporting sessions only if the rule seems ambiguous or contested

Do not treat a single session preference as a standing norm unless it has been crystallized or clearly repeated.

### Preferences

Goal:
- infer stable team preferences, not one-off opinions

Preferred sources:
1. `crystals/team-conventions.md`
2. `crystals/implementation-patterns.md`
3. repeated signals across multiple recent sessions

Do not promote isolated comments to "team preference" without corroboration.

## When To Open Session Files

Open a session file only when one of these is true:
- a summary is too compressed to answer the question
- you need the rationale behind a decision
- a convention appears to conflict with another source
- you need exact related files, open questions, or follow-up details

Avoid opening multiple session files in parallel unless the user explicitly asks for a broad review.

## Query Output Style

When responding after a memory query:
- state the answer first
- distinguish between crystallized knowledge and inference from session history
- cite the specific memory files used
- mention uncertainty if the memory appears stale or conflicting

## Escalation

If memory is insufficient:
- say what was searched
- say what was missing
- then recommend whether to inspect code, docs, issue history, or additional session files
