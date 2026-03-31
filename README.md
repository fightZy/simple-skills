# Simple Skills

Reusable AI agent skills for idea validation, advanced brainstorming, startup research, and workspace memory.

This repository contains installable skills for the `skills.sh` ecosystem and for coding agents such as Codex, Claude Code, Cursor, Cline, OpenCode, and Goose. The current skills focus on three practical jobs:

- validating whether a product, startup, feature, or workflow idea is worth pursuing
- expanding an idea into broader, less conservative, more imaginative directions
- preserving durable workspace memory across repeated agent sessions inside a repository

Install from GitHub with `npx skills add fightZy/simple-skills`.

## Why This Repo Exists

Many agent workflows fail for one of three reasons:

- teams build ideas before checking whether the market is too crowded or the positioning is too weak
- teams brainstorm but still collapse too quickly into safe or conventional options
- teams lose project context between sessions and keep re-explaining the same decisions, conventions, and follow-ups

This repo packages these workflows as reusable agent skills so they can be installed, shared, and reused across projects.

## Skills

### Idea Credibility Analyst

Evaluate whether an idea is worth pursuing before building.

Use it when you want a sharper answer than brainstorming alone, especially for differentiation, alternatives, market crowdedness, or a `continue` / `pivot` / `stop` call.

Docs: [`ICA-EN`](./docs/skills/idea-credibility-analyst/README.md), [`ICA-ZH`](./docs/skills/idea-credibility-analyst/README_zh.md), [`ICA-SKILL`](./.agents/skills/idea-credibility-analyst/SKILL.md)

### Advanced Brainstorming

Expand a proposal into broader, less conservative, more imaginative directions.

Use it when the user wants higher-order ideation instead of the safest recommendation, a shallow idea list, or an early MVP plan.

Docs: [`AB-EN`](./docs/skills/advanced-brainstorming/README.md), [`AB-ZH`](./docs/skills/advanced-brainstorming/README_zh.md), [`AB-SKILL`](./.agents/skills/advanced-brainstorming/SKILL.md)

### Workspace Memory Skill

Preserve repo-local project context across repeated agent sessions.

Use it when a repository needs durable memory for decisions, conventions, rationale, summaries, and follow-ups instead of re-explaining the same context every time.

Docs: [`WMS-EN`](./docs/skills/workspace-memory-skill/README.md), [`WMS-ZH`](./docs/skills/workspace-memory-skill/README_zh.md), [`WMS-SKILL`](./.agents/skills/workspace-memory-skill/SKILL.md)

### Workspace Memory Benchmark Authoring

Add or refine workspace-memory benchmark fixtures safely.

Use it when expanding retrieval benchmark coverage under the benchmark fixture directory without mixing fixture authoring with runtime retrieval changes.

Docs: [`WMBA-EN`](./docs/skills/workspace-memory-benchmark-authoring/README.md), [`WMBA-ZH`](./docs/skills/workspace-memory-benchmark-authoring/README_zh.md), [`WMBA-SKILL`](./.agents/skills/workspace-memory-benchmark-authoring/SKILL.md)

### Workspace Memory Benchmark Analysis

Run workspace-memory benchmarks and interpret failures.

Use it when you need bucket-level retrieval diagnosis and the smallest next optimization step, rather than a flat pass/fail summary.

Docs: [`WMAN-EN`](./docs/skills/workspace-memory-benchmark-analysis/README.md), [`WMAN-ZH`](./docs/skills/workspace-memory-benchmark-analysis/README_zh.md), [`WMAN-SKILL`](./.agents/skills/workspace-memory-benchmark-analysis/SKILL.md)

## Install

List the installable skills available in this GitHub repository:

```bash
npx skills add fightZy/simple-skills --list
```

Install the full repository:

```bash
npx skills add fightZy/simple-skills
```

Install a specific skill from the repo:

```bash
npx skills add fightZy/simple-skills --skill idea-credibility-analyst
npx skills add fightZy/simple-skills --skill advanced-brainstorming
npx skills add fightZy/simple-skills --skill workspace-memory-skill
npx skills add fightZy/simple-skills --skill workspace-memory-benchmark-authoring
npx skills add fightZy/simple-skills --skill workspace-memory-benchmark-analysis
```

Repository-level tests live under `tests/`. Installable skill payloads stay under `.agents/skills/` and should not include development-only test files.

These commands work with the `skills` CLI and are intended for skill-compatible agents and editors.

## Usage

After installation, each skill runs according to its own `SKILL.md`. Use the doc links above to understand scope, capabilities, and scenarios before installing or invoking a skill.

## Benchmarking Workspace Memory

The workspace-memory skill now includes a repository-level benchmark harness for retrieval evaluation. This harness lives outside the installable skill payload and exercises the real runtime query script through subprocess calls.

Repo-owned benchmark fixtures live in `tests/workspace-memory-skill/benchmark_fixtures/`. They cover:

- current-state layered retrieval
- experience retrieval with lineage promotion
- norms queries that should prefer crystals
- exact-id lookup
- sparse or negative retrieval behavior

Run the retrieval benchmark suite:

```bash
python -m scripts.benchmarks.workspace_memory.runner tests/workspace-memory-skill/benchmark_fixtures
```

Run the focused benchmark tests:

```bash
python -m pytest tests/workspace-memory-skill/test_workspace_memory_benchmark.py -q
```

The benchmark harness also includes:

- an optional fixed-LLM QA adapter boundary for end-to-end evaluation
- a `LoCoMo` adapter that converts external records into the repository's internal benchmark case schema

Current boundary:

- retrieval benchmarking is implemented and covered by tests
- fixed-LLM QA is scaffolded but only runs when model configuration is supplied
- `LoCoMo` support is adapter-based and intended for staged integration, not leaderboard-compatible claims in this first batch

## Keywords

Useful search terms for this repository:

- AI agent skills
- skills.sh repository
- Codex skills
- Claude Code skills
- Cursor skills
- Cline skills
- idea validation skill
- advanced brainstorming skill
- ideation skill
- frame-breaking brainstorming
- startup research skill
- competitor analysis skill
- workspace memory skill
- workspace memory benchmark
- retrieval benchmark authoring
- retrieval benchmark analysis
- project memory for coding agents
- reusable prompt engineering workflows

Abbreviation guide:

- `ICA` = `Idea Credibility Analyst`
- `AB` = `Advanced Brainstorming`
- `WMS` = `Workspace Memory Skill`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
