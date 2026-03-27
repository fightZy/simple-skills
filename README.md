# Simple Skills

Reusable AI agent skills for idea validation, startup research, and workspace memory.

This repository contains installable skills for the `skills.sh` ecosystem and for coding agents such as Codex, Claude Code, Cursor, Cline, OpenCode, and Goose. The current skills focus on two practical jobs:

- validating whether a product, startup, feature, or workflow idea is worth pursuing
- preserving durable workspace memory across repeated agent sessions inside a repository

Install from GitHub with `npx skills add fightZy/simple-skills`.

## Why This Repo Exists

Many agent workflows fail for one of two reasons:

- teams build ideas before checking whether the market is too crowded or the positioning is too weak
- teams lose project context between sessions and keep re-explaining the same decisions, conventions, and follow-ups

This repo packages both workflows as reusable agent skills so they can be installed, shared, and reused across projects.

## Skills

### Idea Credibility Analyst

A reusable AI agent skill for idea validation, startup research, competitor analysis, and market crowdedness assessment.

It helps an agent move from vague discussion to structured judgment. The skill is designed for cases where the user does not just want brainstorming, but wants a sharper answer about differentiation, demand, alternatives, and whether there is enough room to continue.

Core capabilities:

- focused clarification instead of broad questionnaires
- competitor research and alternative analysis
- market crowdedness assessment
- structured comparison of positioning, maturity, and gaps
- final `continue` / `pivot` / `stop` recommendation

Typical use cases:

- validating a startup, SaaS, or AI product concept
- pressure-testing a feature before building it
- checking whether a workflow automation idea has a real wedge
- understanding whether a market is too crowded or still has room

Docs:

- [`ICA-EN`](./docs/skills/idea-credibility-analyst/README.md): English overview
- [`ICA-ZH`](./docs/skills/idea-credibility-analyst/README_zh.md): 中文说明
- [`ICA-SKILL`](./.agents/skills/idea-credibility-analyst/SKILL.md): runtime instructions

### Workspace Memory Skill

A reusable AI agent skill for repo-local workspace memory, project context preservation, and long-lived team knowledge.

It is designed for small teams or solo builders who work repeatedly in the same repository and want project context to persist across conversations. Instead of relying on scattered chat history, this skill keeps memory inside the workspace with structured files, summaries, and durable knowledge artifacts.

Core capabilities:

- initialize workspace memory structure
- record structured work sessions
- keep recent context small and archive older material
- separate source sessions from derived summaries
- support durable knowledge such as rules, decisions, patterns, and insights

Typical use cases:

- preserving rationale and follow-ups between agent sessions
- reducing repeated explanation in an active repo
- maintaining recent summaries and archived history
- building lightweight long-term project memory without external infrastructure
- keeping coding agents aligned on decisions, conventions, and prior work

Docs:

- [`WMS-EN`](./docs/skills/workspace-memory-skill/README.md): English overview
- [`WMS-ZH`](./docs/skills/workspace-memory-skill/README_zh.md): 中文说明
- [`WMS-SKILL`](./.agents/skills/workspace-memory-skill/SKILL.md): runtime instructions

### Workspace Memory Benchmark Authoring

A companion skill for `workspace-memory-skill` that teaches agents how to expand self-built benchmark fixtures safely, including subagent-assisted drafting constrained to the benchmark fixture directory.

Docs:

- [`WMBA-EN`](./docs/skills/workspace-memory-benchmark-authoring/README.md): English overview
- [`WMBA-ZH`](./docs/skills/workspace-memory-benchmark-authoring/README_zh.md): 中文说明
- [`WMBA-SKILL`](./.agents/skills/workspace-memory-benchmark-authoring/SKILL.md): runtime instructions

### Workspace Memory Benchmark Analysis

A companion skill for `workspace-memory-skill` that teaches agents how to run benchmark commands, interpret retrieval failures by bucket, and turn those results into targeted optimization guidance.

Docs:

- [`WMAN-EN`](./docs/skills/workspace-memory-benchmark-analysis/README.md): English overview
- [`WMAN-ZH`](./docs/skills/workspace-memory-benchmark-analysis/README_zh.md): 中文说明
- [`WMAN-SKILL`](./.agents/skills/workspace-memory-benchmark-analysis/SKILL.md): runtime instructions

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
- `WMS` = `Workspace Memory Skill`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
