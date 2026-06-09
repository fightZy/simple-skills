---
name: openspec-discovery
description: Use when scope is unstable or requirements are unclear, before creating OpenSpec artifacts. Covers codebase investigation, requirement clarification, option comparison, and decision convergence.
---

# OpenSpec Discovery

## Overview

Discovery is the thinking phase before artifact creation. Investigate the codebase, clarify requirements with the user, compare approaches, and converge on stable scope — all without writing code or creating artifacts.

**Iron law: Discovery is for thinking, not implementing.** You may read files, search code, and investigate the codebase, but NEVER write application code. You MAY create OpenSpec artifacts if the user asks — that's capturing decisions, not implementing.

## Questioning Discipline

### One Question at a Time

Ask ONE question per message. Do not batch multiple questions. If a topic needs multiple questions, break them into separate turns.

### Multiple Choice Preferred

When possible, offer choices rather than open-ended questions. Easier for the user to answer, reduces ambiguity.

### Propose Options with Recommendation

When the user faces a decision:

1. Propose 2-3 approaches with trade-offs
2. Lead with your recommended option and explain why
3. Let the user choose or override

```
Option A (recommended): [approach] — [why]
Option B: [approach] — [trade-off]
Option C: [approach] — [trade-off]
```

### Challenge Assumptions

Don't accept requirements at face value. If something seems over-engineered, under-specified, or misaligned with existing patterns, say so.

## Investigation

### Explore the Codebase

Ground discussions in reality. Before proposing anything:

- Map existing architecture relevant to the discussion
- Find integration points and patterns already in use
- Surface hidden complexity
- Check for existing implementations that could be reused

### Visualize

Use ASCII diagrams liberally when they clarify thinking:

```
┌────────────┐     ┌────────────┐     ┌────────────┐
│   Input    │────▶│  Process   │────▶│   Output   │
└────────────┘     └────────────┘     └────────────┘
```

System diagrams, state machines, data flows, architecture sketches, dependency graphs, comparison tables — all fair game.

### Surface Risks and Unknowns

- Identify what could go wrong
- Find gaps in understanding
- Suggest spikes or investigations for uncertain areas

## OpenSpec Awareness

### Check for Context

At the start, check what exists:

```bash
openspec list --json
```

This tells you active changes, their names, schemas, and status.

### When No Change Exists

Think freely. When insights crystallize, offer:

- "This feels solid enough to start a change. Want me to create a proposal?"
- Or keep exploring — no pressure to formalize

### When a Change Exists

1. **Read existing artifacts** for context (`proposal.md`, `design.md`, `tasks.md`, etc.)
2. **Reference them naturally**: "Your design mentions Redis, but we just realized SQLite fits better..."
3. **Offer to capture** when decisions are made:

   | Insight Type        | Where to Capture             |
   | ------------------- | ---------------------------- |
   | New requirement     | `specs/<capability>/spec.md` |
   | Requirement changed | `specs/<capability>/spec.md` |
   | Design decision     | `design.md`                  |
   | Scope changed       | `proposal.md`                |
   | New work identified | `tasks.md`                   |

4. **The user decides** — offer and move on, don't auto-capture

## Ending Discovery

When scope crystallizes, summarize:

```
## What We Figured Out

**The problem**: [crystallized understanding]
**The approach**: [if one emerged]
**Open questions**: [if any remain]
**Next steps**: Create a change proposal (via openspec-propose)
```

If open questions remain that would materially change artifacts, do NOT proceed — return to discovery.

## Guardrails

- **Don't implement** — never write application code
- **Don't fake understanding** — if unclear, dig deeper
- **Don't rush** — discovery is thinking time, not task time
- **Don't batch questions** — one at a time, always
- **Don't skip recommendations** — when comparing options, always state your pick and why
- **Do visualize** — a good diagram is worth many paragraphs
- **Do explore the codebase** — ground discussions in reality
- **Do question assumptions** — including the user's and your own
