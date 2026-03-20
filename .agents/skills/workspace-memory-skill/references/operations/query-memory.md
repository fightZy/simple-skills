# Query Memory

Use this operation when the user wants prior context, norms, historical rationale, or implementation experience.

## Current State

There is no dedicated query script yet. Retrieval is currently reference-driven.

## Read Order

1. generated navigation file if present, such as `docs/memory/index.md`
2. `docs/memory/summaries/recent.md`
3. relevant `docs/memory/summaries/topics/*.md`
4. relevant `docs/memory/crystals/*.md`
5. specific `docs/memory/sessions/...md` only if needed

For deeper retrieval guidance, read [querying.md](../querying.md).

## Query Goal

Stop at the shallowest layer that gives a reliable answer. Do not open multiple session files by default when a recent summary or crystal already answers the question.

## Related Templates

- topic summary: [templates/topic-summary.md](../templates/topic-summary.md)
- crystal: [templates/crystal.md](../templates/crystal.md)
- session: [templates/session.md](../templates/session.md)

## Notes

- Do not invent a `query_memory.py` flow until the script exists.
- If memory is insufficient, say what was searched and what source should be checked next.
