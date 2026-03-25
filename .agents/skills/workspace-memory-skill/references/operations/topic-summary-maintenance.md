# Topic Summary Maintenance

Use this operation when the task is to create or update topic-level summaries under `summaries/topics/`.

## Current State

Topic-summary maintenance is script-supported for creation and update.

Available scripts:
- `python3 scripts/create_topic_summary.py`
- `python3 scripts/update_topic_summary.py`

## What To Read

- [templates/topic-summary.md](../templates/topic-summary.md) for the target file shape
- [maintenance.md](../maintenance.md) when merging, deduplicating, or superseding existing summaries

## Scripted Flow

1. Identify the topic that needs aggregation.
2. Check whether a matching topic summary already exists.
3. Use `create_topic_summary.py` when the topic needs a new summary file.
4. Use `update_topic_summary.py` when the topic summary already exists and only its content needs maintenance.
5. Preserve `source_ids` so the summary remains traceable.

## Required Semantic Inputs

- topic
- title
- summary
- source session or summary ids

## Optional Semantic Inputs

- tags
- current-state bullets
- key-decision bullets
- relevant-crystal ids or links
- source-trail bullets

## Command Patterns

Create:

```bash
python3 scripts/create_topic_summary.py \
  --root <workspace> \
  --topic "<topic>" \
  --title "<title>" \
  --summary "<summary>" \
  --source-id "<source id>"
```

Update:

```bash
python3 scripts/update_topic_summary.py \
  [--path <file>] \
  [--topic <topic>] \
  [--summary "<summary>"] \
  [--append-current-state "<bullet>"]
```

## Notes

- Topic summaries are aggregated views, not first-party session records.
- Update scripts operate at metadata and section granularity, not as free-form text patchers.
- Keep the scripted English headings unchanged. Write body prose in the configured `content_language`, or English if the config is missing.
