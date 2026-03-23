# Crystal Maintenance

Use this operation when the task is to add or update durable rules, decisions, patterns, or insights.

## Current State

Crystal maintenance is script-supported for creation and update.

Available scripts:
- `python3 scripts/create_crystal.py`
- `python3 scripts/update_crystal.py`

## What To Read

- [crystallization.md](../crystallization.md) for promotion rules
- [templates/crystal.md](../templates/crystal.md) for the target file shape
- [maintenance.md](../maintenance.md) when merging, deduplicating, or superseding existing crystals

## Scripted Flow

1. Identify the source session or summary that justifies the crystal.
2. Check whether a matching crystal already exists.
3. Use `create_crystal.py` when the knowledge is distinct and needs a new file.
4. Use `update_crystal.py` when the durable knowledge already has a matching crystal.
5. Preserve `source_ids` so the crystal remains traceable.

## Required Semantic Inputs

- title
- summary
- knowledge type: `rule`, `decision`, `pattern`, or `insight`
- source session or summary ids

## Optional Semantic Inputs

- tags
- applies-to globs or paths when the crystal is not workspace-wide

## Command Patterns

Create:

```bash
python3 scripts/create_crystal.py \
  --root <workspace> \
  --title "<title>" \
  --summary "<summary>" \
  --knowledge-type <rule|decision|pattern|insight> \
  --source-id "<source id>"
```

Update:

```bash
python3 scripts/update_crystal.py \
  [--path <file>] \
  [--id <crystal:id>] \
  [--summary "<summary>"] \
  [--append-statement "<bullet>"]
```

## Notes

- Do not use `scope`; use `applies_to` when narrowing the area of relevance.
- Crystals are durable knowledge, not raw session transcripts.
- Update scripts operate at metadata and section granularity, not as free-form text patchers.
