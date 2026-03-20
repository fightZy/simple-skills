# Workspace Memory Layout

Use this layout when creating workspace memory from scratch. If the repository already has a memory convention, adapt to it instead of forcing this exact tree.

```text
docs/memory/
  index.md
  sessions/
    YYYY/
      MM/
        YYYY-MM-DD-topic.md
  summaries/
    recent.md
    archive.md
    topics/
      architecture.md
      testing.md
      onboarding.md
  crystals/
    crystal-*.md
```

## File Roles

`index.md`
- Optional generated navigation file.
- Useful for human browsing, but should not be treated as the authoritative source of truth.
- Safe to regenerate from structured memory files.

`sessions/`
- Source memory for notable conversations or handoffs.
- Keep each file focused on one topic or one coherent work block.
- Prefer date-based filenames with a short topic suffix.

`summaries/recent.md`
- High-signal rolling summary of active work.
- Best first stop for context recovery.
- Keep this compact enough to scan quickly.

`summaries/archive.md`
- Compressed summary of older but still relevant history.
- Move stale detail here when recent memory gets noisy.

`summaries/topics/*.md`
- Topic-specific summaries when a project has recurring areas.
- Create only when the topic is reused enough to justify separate maintenance.

`crystals/`
- Durable project knowledge.
- Prefer one crystal per file.
- Use for durable rules, decisions, patterns, and insights that should influence future work.

## Default Retrieval Order

1. `index.md`
2. `summaries/recent.md`
3. relevant topic summaries
4. relevant crystallized memory files
5. only then relevant session files

## Naming Guidance

- Prefer ASCII filenames.
- Use dates in `YYYY-MM-DD` format.
- Use short, stable topic names instead of vague names like `notes.md` or `chat.md`.
- Keep one concern per file whenever possible.
