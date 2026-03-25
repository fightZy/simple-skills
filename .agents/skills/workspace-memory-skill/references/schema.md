# Workspace Memory Schema

Use this file for metadata rules. Template files under `references/templates/` are body-first and should not be the primary place the agent learns frontmatter.

## Shared Fields

Required for all memory files:
- `id`: stable unique identifier
- `memory_type`: file category such as `session`, `crystal`, `topic-summary`, `archive-summary`, `generated-summary`, or `generated-index`
- `title`: human-readable title
- `summary`: one-line retrieval preview
- `created_at`: creation date
- `updated_at`: last update date

Recommended:
- `tags`: compact retrieval tags

Do not add fields such as `participants` or `scope` by default.

## Script-Owned Metadata

Prefer scripts to generate or update these fields:
- `id`
- `memory_type`
- `created_at`
- `updated_at`
- generated-file metadata such as `generator`

The agent should provide semantic inputs, not hand-write these values unless repairing a broken file.

## Type-Specific Fields

### `session`

Additional fields:
- `session_date`: required
- `tags`: recommended

Do not include `source_ids` by default. A session is normally the source.

### `crystal`

Additional fields:
- `knowledge_type`: required, one of `rule`, `decision`, `pattern`, `insight`
- `source_ids`: required
- `applies_to`: optional paths or globs when the crystal is not workspace-wide

### `topic-summary`

Additional fields:
- `topic`: required
- `source_ids`: required

### `archive-summary`

Additional fields:
- `source_ids`: required

### `generated-summary`

Additional fields:
- `generator`: optional but recommended
- `source_ids`: recommended when the summary is derived from explicit session entries

### `generated-index`

Additional fields:
- `generator`: optional but recommended

## Usage Notes

- Use body templates to structure content.
- Use scripts and operation cards to determine how metadata gets produced.
- When schema and a template example disagree, follow this schema document.
