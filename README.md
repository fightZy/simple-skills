# Simple Skills

Reusable AI agent skills for idea validation, advanced brainstorming, closure retrospectives, code review delegation, formal change orchestration, startup research, and workspace memory.

This repository contains installable skills for the `skills.sh` ecosystem and for coding agents such as Codex, Claude Code, Cursor, Cline, OpenCode, and Goose. The current skills focus on six practical jobs:

- validating whether a product, startup, feature, or workflow idea is worth pursuing
- expanding an idea into broader, less conservative, more imaginative directions
- reflecting at task closure to decide whether reusable guidance should be codified
- deciding how to split code review across focused subagents
- orchestrating formal changes with OpenSpec artifacts, approval gates, and superpower discipline layers
- preserving durable workspace memory across repeated agent sessions inside a repository

Install from GitHub with `npx skills add fightZy/simple-skills`.

## Why This Repo Exists

Many agent workflows fail for one of six reasons:

- teams build ideas before checking whether the market is too crowded or the positioning is too weak
- teams brainstorm but still collapse too quickly into safe or conventional options
- teams finish work without converting repeated friction into reusable guidance
- teams lack a unified workflow for formal changes, letting multiple planning systems compete and create confusion
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

### Closure Retrospective

Review a task at wrap-up and decide whether any reusable lesson is worth codifying.

Use it when a non-trivial task is reaching closure and the work may justify a suggestion for an existing skill, a new skill, or `AGENTS.md` / `CLAUDE.md`.

Docs: [`CR-EN`](./docs/skills/closure-retrospective/README.md), [`CR-ZH`](./docs/skills/closure-retrospective/README_zh.md), [`CR-SKILL`](./.agents/skills/closure-retrospective/SKILL.md)

### Dispatching Code Review Subagents

Decide whether code review should use one reviewer, multiple themed reviewers, or layered review.

Use it before delegating code review to subagents, especially when a change spans independent risk areas or could benefit from focused review lenses.

Docs: [`DCR-EN`](./docs/skills/dispatching-code-review-subagents/README.md), [`DCR-ZH`](./docs/skills/dispatching-code-review-subagents/README_zh.md), [`DCR-SKILL`](./.agents/skills/dispatching-code-review-subagents/SKILL.md)

### Workspace Memory Skill

Preserve repo-local project context across repeated agent sessions.

Use it when a repository needs durable memory for decisions, conventions, rationale, summaries, and follow-ups instead of re-explaining the same context every time.

Docs: [`WMS-EN`](./docs/skills/workspace-memory-skill/README.md), [`WMS-ZH`](./docs/skills/workspace-memory-skill/README_zh.md), [`WMS-SKILL`](./.agents/skills/workspace-memory-skill/SKILL.md)

### OpenSpec Superpower Orchestration

Orchestrate formal changes using OpenSpec artifacts plus superpower skill discipline layers.

Use it when work requires formal specs (`proposal.md`, `design.md`, `spec.md`, `tasks.md`), approval gates, and coordinated implementation without creating parallel planning systems.

Docs: [`OSO-EN`](./docs/skills/openspec-superpower-orchestration/README.md), [`OSO-ZH`](./docs/skills/openspec-superpower-orchestration/README_zh.md), [`OSO-SKILL`](./.agents/skills/openspec-superpower-orchestration/SKILL.md)

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
npx skills add fightZy/simple-skills --skill closure-retrospective
npx skills add fightZy/simple-skills --skill dispatching-code-review-subagents
npx skills add fightZy/simple-skills --skill workspace-memory-skill
npx skills add fightZy/simple-skills --skill openspec-superpower-orchestration
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
- closure retrospective skill
- agent wrap-up reflection
- codify reusable workflow lessons
- code review subagents
- delegated code review
- parallel code review
- openspec orchestration skill
- formal change workflow
- spec-driven development
- approval gate workflow
- startup research skill
- competitor analysis skill
- workspace memory skill
- workspace memory benchmark
- project memory for coding agents
- reusable prompt engineering workflows

Abbreviation guide:

- `ICA` = `Idea Credibility Analyst`
- `AB` = `Advanced Brainstorming`
- `CR` = `Closure Retrospective`
- `DCR` = `Dispatching Code Review Subagents`
- `WMS` = `Workspace Memory Skill`
- `OSO` = `OpenSpec Superpower Orchestration`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
