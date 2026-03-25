# Initialize Memory

Use this operation when the workspace does not yet have a memory tree, or when the user wants to reseed the default structure.

## Script

`python3 scripts/init_memory.py`

## What The Script Owns

- creates the directory structure
- creates generated navigation and summary files
- writes frontmatter for generated files

## Semantic Inputs

Required:
- workspace root

Optional:
- memory directory path if the project does not use `docs/memory`
- content language for future body prose
- whether to overwrite seeded files

## Command Pattern

```bash
python3 scripts/init_memory.py --root <workspace> [--memory-dir docs/memory] [--content-language <en|zh-CN>] [--force]
```

## Resulting Files

- generated navigation file such as `docs/memory/index.md`
- `docs/memory/summaries/recent.md` seeded with empty `source_ids`
- `docs/memory/summaries/archive.md`
- `docs/memory/config.toml`
- empty directories for `sessions/`, `summaries/topics/`, and `crystals/`

## Templates

- generated index: [templates/generated-index.md](../templates/generated-index.md)
- generated recent summary: [templates/generated-recent.md](../templates/generated-recent.md)
- archive summary: [templates/archive-summary.md](../templates/archive-summary.md)

## Notes

- Do not manually recreate these generated files if the script can do it.
- If the repository already has an established memory root, preserve that convention.
- On first-time setup, infer `--content-language` from the user's conversation language and pass it explicitly.
- `content_language` controls body prose only; seeded headings remain in English.
