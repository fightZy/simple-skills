# Workspace Memory Maintenance Scripts Design

**Date:** 2026-03-23

## Goal

Add the first complete automation layer for workspace-memory content maintenance without over-expanding the skill surface. This batch should make `crystal` and `topic-summary` files script-maintained for creation and update, while keeping the existing repo-local Markdown model and the current narrow CLI style.

## Problem Statement

The skill already automates:

- memory tree initialization
- session capture
- recent-to-archive refinement

But it still leaves durable knowledge maintenance and topic aggregation as manual workflows. That creates three practical problems:

1. metadata discipline stops at `session` and generated summaries
2. repeated crystal/topic edits are error-prone and inconsistent
3. future query automation has no stable write path to depend on

The gap is not just "missing scripts". The missing piece is a shared maintenance layer that can update typed Markdown memory files safely and predictably.

## Scope

This design covers one implementation batch:

- add shared Markdown memory maintenance helpers
- add `create_crystal.py`
- add `update_crystal.py`
- add `create_topic_summary.py`
- add `update_topic_summary.py`
- add automated tests for the new scripts
- update runtime docs and operation cards to describe the new automation boundary

## Non-Goals

This batch does not include:

- a query script
- automated migration from arbitrary legacy notes
- full derived-file `source_ids` repair across all memory types
- generic free-form patching of Markdown bodies
- a universal "maintain anything" CLI

Those would expand the problem from "safe content maintenance" into retrieval and repair infrastructure. The current skill is not mature enough for that in one batch.

## Current Constraints

The design must preserve these existing properties:

- repo-local, Markdown-first files remain the source of truth
- metadata should stay script-owned where possible
- bodies must remain readable and manually inspectable
- updates should prefer existing files over near-duplicate creation
- CLIs should stay narrow and explicit, consistent with current scripts

The repository is intentionally light: there is no existing project-wide Python packaging, no test harness under this skill, and no shared parsing module. The new design should stay minimal and local to the skill.

## Options Considered

### Option 1: Independent scripts with duplicated logic

Each new script would parse frontmatter, find sections, and update files on its own.

Pros:

- fastest to start
- easy to understand per script

Cons:

- duplicates merge logic immediately
- high regression risk when update rules change
- harder to extend into future query or repair work

### Option 2: Single large `maintain_memory.py` with subcommands

One CLI would expose `create-crystal`, `update-crystal`, `create-topic-summary`, and more.

Pros:

- central implementation
- less file sprawl

Cons:

- larger first change set
- deviates from the current script shape
- forces docs and operation cards to change more aggressively

### Option 3: Shared maintenance core plus narrow scripts

Introduce a shared helper module and keep small dedicated CLIs for each operation.

Pros:

- consistent with existing scripts
- shared logic for metadata and section updates
- easy to test
- good base for later automation

Cons:

- more script files than a single CLI
- requires a small internal API design upfront

## Chosen Approach

Choose Option 3.

It is the smallest change that still creates a durable foundation. The skill needs predictable typed-file maintenance more than it needs a generic CLI abstraction. Narrow CLIs also align with the current operation-card model: each task maps cleanly to one script.

## Architecture

### New Shared Module

Add a local helper module:

- `.agents/skills/workspace-memory-skill/scripts/memory_ops.py`

Responsibilities:

- parse and serialize simple YAML frontmatter used by this skill
- read typed Markdown files safely
- validate `memory_type`
- normalize list metadata fields
- update `updated_at`
- locate and rewrite known `##` sections
- merge list-style section entries with de-duplication and stable order
- clear or restore placeholder lines such as `- None yet.`
- generate stable slugs and default file paths

This module is intentionally not a generic Markdown AST system. It only supports the narrow file shapes defined by this skill.

### New Scripts

Add:

- `.agents/skills/workspace-memory-skill/scripts/create_crystal.py`
- `.agents/skills/workspace-memory-skill/scripts/update_crystal.py`
- `.agents/skills/workspace-memory-skill/scripts/create_topic_summary.py`
- `.agents/skills/workspace-memory-skill/scripts/update_topic_summary.py`

Each script should:

1. parse CLI arguments
2. resolve workspace and target path
3. validate semantic inputs
4. call `memory_ops.py`
5. print a simple file action result, matching existing script style

### Existing Scripts

Do not refactor existing scripts aggressively in the same batch.

Allowed:

- small reuse of helper functions if it is trivial and low-risk

Avoid in this batch:

- rewriting `record_session.py`
- rewriting `refine_memory.py`

Reason: the main goal is to add new maintenance capability, not to expand the blast radius. Existing scripts can be migrated to the shared module later after the new path is proven by tests.

## File Mapping Rules

### Crystal

Default location:

- `docs/memory/crystals/crystal-<slug>.md`

Default file id:

- `crystal:<slug>`

Required metadata:

- `id`
- `memory_type: crystal`
- `title`
- `summary`
- `created_at`
- `updated_at`
- `knowledge_type`
- `source_ids`

Optional metadata:

- `tags`
- `applies_to`

Body sections:

- `Statement`
- `Why It Matters`
- `When To Apply`
- `Provenance`
- `Notes`

### Topic Summary

Default location:

- `docs/memory/summaries/topics/<topic-slug>.md`

Default file id:

- `topic-summary:<topic-slug>`

Required metadata:

- `id`
- `memory_type: topic-summary`
- `title`
- `summary`
- `created_at`
- `updated_at`
- `topic`
- `source_ids`

Optional metadata:

- `tags`

Body sections:

- `Current State`
- `Key Decisions`
- `Relevant Crystals`
- `Source Trail`

## CLI Design

### `create_crystal.py`

Required:

- `--root`
- `--title`
- `--summary`
- `--knowledge-type`
- at least one `--source-id`

Optional:

- `--memory-dir`
- `--path`
- `--tag` repeatable
- `--applies-to` repeatable
- `--statement`
- `--why-it-matters`
- `--when-to-apply`
- `--note`
- `--force`

Behavior:

- creates a new crystal file
- fails if the target exists unless `--force` is used
- fills missing body inputs with stable placeholders

### `update_crystal.py`

Target selection:

- `--path` or `--id`

Metadata updates:

- `--summary`
- `--add-tag`
- `--set-tag`
- `--add-source-id`
- `--set-source-id`
- `--add-applies-to`
- `--set-applies-to`

Body updates:

- `--append-statement`
- `--replace-statement`
- `--append-why-it-matters`
- `--replace-why-it-matters`
- `--append-when-to-apply`
- `--replace-when-to-apply`
- `--append-note`
- `--replace-note`
- `--append-provenance`
- `--replace-provenance`

Behavior:

- updates only known metadata fields and known sections
- refreshes `updated_at`
- preserves `created_at`
- de-duplicates list-like content where the section is list-based

### `create_topic_summary.py`

Required:

- `--root`
- `--topic`
- `--title`
- `--summary`
- at least one `--source-id`

Optional:

- `--memory-dir`
- `--path`
- `--tag` repeatable
- `--current-state`
- `--key-decision`
- `--relevant-crystal`
- `--source-trail`
- `--force`

Behavior:

- creates a topic summary at the default topic path unless `--path` is provided

### `update_topic_summary.py`

Target selection:

- `--path` or `--topic`

Metadata updates:

- `--summary`
- `--add-tag`
- `--set-tag`
- `--add-source-id`
- `--set-source-id`

Body updates:

- `--append-current-state`
- `--replace-current-state`
- `--append-key-decision`
- `--replace-key-decision`
- `--append-relevant-crystal`
- `--replace-relevant-crystal`
- `--append-source-trail`
- `--replace-source-trail`

## Update Semantics

This is the most important design choice in the batch.

### Narrow Update Model

Updates operate only at the metadata-field and section level.

Not supported:

- arbitrary in-place text patching
- heading renames
- section insertion outside the known schema
- fuzzy matching against partial titles

This restriction is intentional. It keeps the scripts deterministic and testable.

### Metadata Rules

- `created_at` is set only at file creation
- `updated_at` is refreshed on every successful update
- list metadata fields are normalized, stripped, de-duplicated, and preserved in first-seen order
- `memory_type` must match the target script or the script fails
- required fields remain required after update

### Section Rules

- section updates only target known `##` headings
- `append` mode adds items to the end of the section
- `replace` mode replaces the section body entirely
- placeholder bullets are removed when real content exists
- if a list-style section becomes empty, it falls back to `- None yet.`
- sections absent from the file are inserted in the canonical order

### Overwrite Policy

Creation scripts should not overwrite existing files by default.

Update scripts should not create new files implicitly. If the target is missing, they fail with a precise error.

## Error Handling

Scripts should fail fast for:

- missing required arguments
- missing target files on update
- invalid `memory_type`
- unsupported `knowledge_type`
- empty `source_ids`
- malformed frontmatter in target files

Errors should explain:

- what failed
- which file or argument caused it
- what the caller should provide instead

## Testing Strategy

Add local tests under:

- `.agents/skills/workspace-memory-skill/tests/`

Preferred test style:

- black-box CLI tests using temporary directories
- light unit coverage for `memory_ops.py` where parsing or merge behavior is tricky

Required coverage:

- create crystal with required fields
- update crystal metadata without clobbering unrelated fields
- append and replace section behavior
- create topic summary with canonical layout
- update topic summary with list de-duplication
- placeholder cleanup and restoration
- `created_at` preservation and `updated_at` refresh
- error on `memory_type` mismatch
- error on missing update target

## Documentation Changes

After the scripts exist, update:

- `.agents/skills/workspace-memory-skill/SKILL.md`
- `.agents/skills/workspace-memory-skill/references/operations/crystal-maintenance.md`
- `.agents/skills/workspace-memory-skill/references/templates.md`
- maintainers docs if they describe the automation boundary

The runtime docs should clearly distinguish:

- now-scripted flows
- still-manual flows

## Risks

### Risk 1: Over-generalizing the helper layer

If `memory_ops.py` becomes a pseudo framework, the batch slows down and the API becomes harder to trust.

Mitigation:

- support only the file shapes needed by crystal and topic-summary
- use explicit helper functions, not plugin-style abstractions

### Risk 2: Markdown parsing fragility

If parsing assumes too much, it may break on manually edited files.

Mitigation:

- support the narrow frontmatter format already used by the skill
- fail clearly when the structure is malformed
- cover manual-edit edge cases in tests

### Risk 3: Accidental rewrite of human-authored bodies

Update scripts can become destructive if they rewrite whole documents.

Mitigation:

- update at section granularity only
- preserve untouched sections verbatim
- avoid whole-document regeneration for updates

## Self-Review

I reviewed the design against the skill goals and repository constraints.

What changed during self-review:

- removed any attempt to include `query` in this batch
- removed aggressive refactoring of existing scripts from the critical path
- narrowed update behavior to section-level append or replace only
- made tests part of the batch instead of a follow-up item

What still remains intentionally deferred:

- generalized repair and dedup across arbitrary memory files
- broader lineage automation across generated summaries
- metadata-first retrieval automation

## Approval Boundary

If this design is accepted, the next implementation batch should produce:

- four new maintenance CLIs
- one shared helper module
- local automated tests
- synced docs for the new automation boundary

No implementation should start beyond that boundary until this batch is stable.
