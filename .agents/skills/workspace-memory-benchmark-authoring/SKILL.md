---
name: workspace-memory-benchmark-authoring
description: Use when the user wants to add or expand workspace-memory benchmark fixture coverage, especially for complex retrieval cases that can be drafted safely by subagents under the benchmark fixture directory.
---

# Workspace Memory Benchmark Authoring

Use this companion skill when the job is to add or refine self-built benchmark fixtures for `workspace-memory-skill`.

## Scope

This skill is for repository benchmark authoring, not for runtime memory operations.

Primary paths:

- `tests/workspace-memory-skill/benchmark_fixtures/`
- `tests/workspace-memory-skill/test_workspace_memory_benchmark.py`
- `scripts/benchmarks/workspace_memory/`

## Workflow

1. Inspect existing fixture coverage before adding new cases.
2. Identify missing buckets or edge conditions.
3. Keep each fixture focused on one retrieval behavior.
4. If fixture drafting is independent, use a subagent restricted to `benchmark_fixtures/` only.
5. Review fixture realism locally before accepting it.
6. Run benchmark verification after fixture changes.

## Fixture Rules

Each fixture should define:

- `case_id`
- `query`
- `memory_files`
- `expected_candidate_ids`
- `bucket`

Add these when they help:

- `expected_top_id`
- `expected_layers`
- `forbidden_candidate_ids`
- `gold_answer`
- `qa_enabled`

Keep fixture files realistic:

- use frontmatter-rich Markdown
- use stable ids and tags
- keep memory trees small but believable
- avoid testing multiple ranking ideas in one case

## Subagent Boundary

If you delegate fixture drafting:

- the subagent owns only `tests/workspace-memory-skill/benchmark_fixtures/`
- do not let the subagent edit runner, scorer, or runtime scripts
- review every drafted case locally before verification

## Verification

Run:

- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`
- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`

If a fixture exposes a real retrieval bug, report that separately instead of silently weakening the case.
