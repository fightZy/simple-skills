---
name: workspace-memory-benchmark-analysis
description: Use when the user wants to run workspace-memory benchmarks, interpret retrieval results, or map benchmark failures to likely ranking, lineage, or fallback defects before optimizing the system.
---

# Workspace Memory Benchmark Analysis

Use this companion skill when the job is to run the workspace-memory benchmark suite and turn results into concrete optimization guidance.

## Scope

This skill analyzes benchmark output for `workspace-memory-skill`.

Primary paths:

- `scripts/benchmarks/workspace_memory/runner.py`
- `scripts/benchmarks/workspace_memory/scoring.py`
- `tests/workspace-memory-skill/benchmark_fixtures/`
- `.agents/skills/workspace-memory-skill/scripts/query_memory.py`

## Workflow

1. Run the benchmark suite and any focused pytest checks needed for the task.
2. Read suite output at both total and bucket levels.
3. Inspect failed cases and their `stdout` reasons.
4. Classify the problem before proposing code changes.
5. Recommend the smallest next retrieval change and the exact verification to rerun.

## Interpretation Guide

- low `recall_at_k`: retrieval did not find the right candidate set
- low `mrr` or `top_hit`: ranking is wrong even if recall is acceptable
- low `layer_hit`: derived layers are losing to raw sessions
- `forbidden_hit`: sparse or constrained queries are leaking irrelevant results
- `false_positive`: no-match handling is too permissive

Use bucket names to separate failure families such as:

- `current-state`
- `lineage`
- `norms-ordering`
- `negative`
- `exact-id`

## Output

For each failure group, report:

- affected cases
- observed retrieval order
- likely cause
- smallest recommended change
- verification command

Do not stop at aggregate pass/fail counts.

## Verification

Run:

- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`
- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`

If optimization work is requested, use these findings to justify the next retrieval edit and rerun the same commands after the change.
