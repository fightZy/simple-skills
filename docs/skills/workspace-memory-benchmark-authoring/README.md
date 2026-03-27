# Workspace Memory Benchmark Authoring

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`workspace-memory-benchmark-authoring` is a companion skill for `workspace-memory-skill`. It teaches agents how to expand the repository's self-built benchmark fixtures without blurring fixture authoring with retrieval implementation work.

## Purpose

Use this skill when the job is to add or refine benchmark cases under:

- `tests/workspace-memory-skill/benchmark_fixtures/`

The target is realistic retrieval coverage, not synthetic test inflation.

## Design Principles

- One fixture should test one retrieval behavior.
- Fixtures should model believable layered memory trees.
- Subagents may draft fixtures, but only within the fixture directory.
- The main agent should review fixture quality and run verification locally.
- Benchmark fixtures should make regressions obvious, not easier to hide.

## Relationship To Workspace Memory

This skill depends on the benchmark harness and the runtime query behavior of `workspace-memory-skill`, but it is not part of the runtime memory workflow itself. It exists to keep benchmark authoring discoverable and disciplined.

## Verification

Typical verification commands:

- `python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q`
- `python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures`
