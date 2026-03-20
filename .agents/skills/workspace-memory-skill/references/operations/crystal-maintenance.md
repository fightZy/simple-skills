# Crystal Maintenance

Use this operation when the task is to add or update durable rules, decisions, patterns, or insights.

## Current State

There is no dedicated crystal-creation script yet. Crystal maintenance is currently manual.

## What To Read

- [crystallization.md](../crystallization.md) for promotion rules
- [templates/crystal.md](../templates/crystal.md) for the target file shape
- [maintenance.md](../maintenance.md) when merging, deduplicating, or superseding existing crystals

## Manual Flow

1. Identify the source session or summary that justifies the crystal.
2. Check whether a matching crystal already exists.
3. Update the existing crystal if it is the same durable knowledge.
4. Create a new crystal file only when the knowledge is distinct.
5. Preserve `source_ids` so the crystal remains traceable.

## Required Semantic Inputs

- title
- summary
- knowledge type: `rule`, `decision`, `pattern`, or `insight`
- source session or summary ids

## Optional Semantic Inputs

- tags
- applies-to globs or paths when the crystal is not workspace-wide

## Notes

- Do not use `scope`; use `applies_to` when narrowing the area of relevance.
- Crystals are durable knowledge, not raw session transcripts.
