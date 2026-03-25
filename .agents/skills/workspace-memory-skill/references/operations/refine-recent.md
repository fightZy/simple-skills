# Refine Recent Memory

Use this operation when `summaries/recent.md` has become noisy and older recent entries should move into archive memory.

## Script

`python3 scripts/refine_memory.py`

## What The Script Owns

- reading the current recent summary
- moving older recent entries into archive history
- shrinking pending follow-ups to match the retained recent entries
- rebuilding `source_ids` for recent and archive summaries
- refreshing `updated_at` on rewritten derived summaries

## Semantic Inputs

Required:
- workspace root

Optional:
- how many recent entries to keep
- minimum recent-entry count before archiving starts

## Command Pattern

```bash
python3 scripts/refine_memory.py \
  --root <workspace> \
  [--memory-dir docs/memory] \
  [--keep 5] \
  [--min-archive 7]
```

## Related Templates

- generated recent summary: [templates/generated-recent.md](../templates/generated-recent.md)
- archive summary: [templates/archive-summary.md](../templates/archive-summary.md)

## Notes

- This is structural compression, not semantic crystal extraction.
- If the refined result suggests durable knowledge, update crystals separately.
- Archive and recent lineage are derived mechanically from the retained summary entries.
- Use `python3 scripts/refine_memory.py --help` as the final parameter contract.
