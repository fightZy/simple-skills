# Workspace Memory Templates

Use these templates as starting points. Keep body templates separate from metadata rules so the agent can focus on content structure while scripts own frontmatter generation.

## Metadata Schema

Read [schema.md](schema.md) for shared fields, type-specific fields, and which values should be script-generated.

## Template Files

- Session memory: [templates/session.md](templates/session.md)
- Crystal memory: [templates/crystal.md](templates/crystal.md)
- Topic summary: [templates/topic-summary.md](templates/topic-summary.md)
- Archive summary: [templates/archive-summary.md](templates/archive-summary.md)
- Generated recent summary: [templates/generated-recent.md](templates/generated-recent.md)
- Optional generated navigation index: [templates/generated-index.md](templates/generated-index.md)

## Design Notes

- Template files below are body-first. Do not treat the example bodies as instructions to hand-write metadata.
- `session` files are first-party records and should not carry `source_ids` by default.
- `crystal` files use `knowledge_type`, not `crystal_type`.
- `crystal` and `topic-summary` files now have script-supported create/update flows; prefer those scripts over hand-writing frontmatter.
- If a crystal applies only to part of the workspace, use `applies_to` with file globs or concrete paths.
- Generated summary or index files may include generator metadata, but they are not authoritative sources.
