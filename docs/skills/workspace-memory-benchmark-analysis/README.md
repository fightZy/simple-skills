# Workspace Memory Benchmark Analysis

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`workspace-memory-benchmark-analysis` is a companion skill for `workspace-memory-skill`. It teaches agents how to run benchmark commands, classify retrieval failures, and turn benchmark output into concrete optimization guidance.

## Purpose

Use this skill when the user wants to:

- run the workspace-memory benchmark suite
- understand why a benchmark case failed
- relate failures back to ranking, lineage, or fallback behavior
- decide which retrieval change to try next

## Design Principles

- Benchmark output should be read by bucket, not only by total pass rate.
- Failures should be mapped to likely causes, not reported as raw metrics only.
- `stdout` reasons from the real query script are part of the evidence.
- Recommendations should stay small and verifiable.

## Relationship To Workspace Memory

This skill depends on the benchmark harness and the runtime query behavior of `workspace-memory-skill`, but it focuses on diagnosis and optimization guidance rather than fixture creation or memory authoring.

## Verification

Typical verification commands:

- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`
- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`
