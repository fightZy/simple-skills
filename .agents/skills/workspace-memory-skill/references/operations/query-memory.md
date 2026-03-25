# Query Memory

Use this operation when the user wants prior context, norms, historical rationale, or implementation experience.

## Current State

Query retrieval is script-supported through:

- `python3 scripts/query_memory.py`

## Read Order

1. generated navigation file if present, such as `docs/memory/index.md`
2. `docs/memory/summaries/recent.md`
3. relevant `docs/memory/summaries/topics/*.md`
4. relevant `docs/memory/crystals/*.md`
5. specific `docs/memory/sessions/...md` only if needed

For deeper retrieval guidance, read [querying.md](../querying.md).

## Query Goal

Stop at the shallowest layer that gives a reliable answer. Do not open multiple session files by default when a recent summary or crystal already answers the question.

## Command Patterns

Current state:

```bash
python3 scripts/query_memory.py \
  --root <workspace> \
  --query-type current-state \
  --topic "<topic>"
```

Norms:

```bash
python3 scripts/query_memory.py \
  --root <workspace> \
  --query-type norms \
  --tag "<tag>"
```

Exact id:

```bash
python3 scripts/query_memory.py \
  --root <workspace> \
  --id "<memory:id>"
```

## Related Templates

- topic summary: [templates/topic-summary.md](../templates/topic-summary.md)
- crystal: [templates/crystal.md](../templates/crystal.md)
- session: [templates/session.md](../templates/session.md)

## Notes

- The first query script is metadata-first and returns candidate files, not synthesized answers.
- It prefers lineage-related topic summaries and crystals when their `source_ids` overlap matched session evidence.
- If memory is insufficient, say what was searched and what source should be checked next.
