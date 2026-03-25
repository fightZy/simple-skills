# Session Capture

Use this operation when the user wants to record a new first-party session memory.

## Script

`python3 scripts/record_session.py`

## What The Script Owns

- session filename and path
- session frontmatter
- session id generation
- updates to `summaries/recent.md`

## What The Agent Owns

- the actual session content
- the semantic inputs passed to the script
- any cleanup or refinement of the generated body afterward

## Required Semantic Inputs

- `topic`

Usually provide at least one of:
- `decision`
- `goal`

## Optional Semantic Inputs

- `date`
- `tag`
- `rationale`
- `change`
- `open-question`
- `follow-up`
- `crystal`
- `related-file`
- `related-ref`

## Command Pattern

```bash
python3 scripts/record_session.py \
  --root <workspace> \
  --date <YYYY-MM-DD> \
  --topic "<topic>" \
  [--goal "<goal>"] \
  [--tag "<tag>"] \
  [--decision "<decision>"] \
  [--rationale "<rationale>"] \
  [--change "<change>"] \
  [--open-question "<question>"] \
  [--follow-up "<next step>"] \
  [--crystal "<candidate>"] \
  [--related-file "<path>"] \
  [--related-ref "<ref>"]
```

## Body Template

See [templates/session.md](../templates/session.md).

The body sections are:
- Goal
- Key Decisions
- Rationale
- Changes
- Open Questions
- Follow-up
- Crystallization Candidates

## Notes

- The script generates metadata. Do not hand-write session frontmatter unless fixing a broken file.
- Session files do not carry `source_ids` by default because they are primary sources.
- The script refreshes `summaries/recent.md` lineage metadata so the generated summary stays traceable to its session entries.
- Use `python3 scripts/record_session.py --help` as the final parameter contract.
