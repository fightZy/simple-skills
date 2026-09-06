# Simple Skills

Reusable AI agent skills for idea validation, advanced brainstorming, closure retrospectives, code review delegation, formal change orchestration, and startup research.

This repository contains installable skills for the `skills.sh` ecosystem and for coding agents such as Codex, Claude Code, Cursor, Cline, OpenCode, and Goose. The current skills focus on five practical jobs:

- validating whether a product, startup, feature, or workflow idea is worth pursuing
- expanding an idea into broader, less conservative, more imaginative directions
- using task evidence to improve durable guidance, its scope, and when it is loaded
- deciding how to split code review across focused subagents
- orchestrating formal changes with OpenSpec artifacts, approval gates, and superpower discipline layers

Install from GitHub with `npx skills add fightZy/simple-skills`.

## Why This Repo Exists

Many agent workflows fail for recurring reasons:

- teams build ideas before checking whether the market is too crowded or the positioning is too weak
- teams brainstorm but still collapse too quickly into safe or conventional options
- teams accumulate guidance without checking whether it improves later decisions or adds unnecessary context
- teams lack a unified workflow for formal changes, letting multiple planning systems compete and create confusion

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

Use existing work evidence to decide whether durable guidance should be retained, cleaned up, clarified, relocated, or supplemented.

Use it at non-trivial task closure, or when explicitly reviewing reusable context from a stable work unit. Determine scope and loading time before choosing the smallest change to skills or applicable project guidance; propose edits before applying them.

Docs: [`CR-EN`](./docs/skills/closure-retrospective/README.md), [`CR-ZH`](./docs/skills/closure-retrospective/README_zh.md), [`CR-SKILL`](./.agents/skills/closure-retrospective/SKILL.md)

### Dispatching Code Review Subagents

Decide whether code review should use one reviewer, multiple themed reviewers, or layered review.

Use it before delegating code review to subagents, especially when a change spans independent risk areas or could benefit from focused review lenses.

Docs: [`DCR-EN`](./docs/skills/dispatching-code-review-subagents/README.md), [`DCR-ZH`](./docs/skills/dispatching-code-review-subagents/README_zh.md), [`DCR-SKILL`](./.agents/skills/dispatching-code-review-subagents/SKILL.md)

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
npx skills add fightZy/simple-skills --skill openspec-superpower-orchestration
```

Repository-level tests and other development-only assets live outside `.agents/skills/`. Installable skill directories contain only the runtime files that agents need to read or execute.

These commands work with the `skills` CLI and are intended for skill-compatible agents and editors.

## Usage

After installation, each skill runs according to its own `SKILL.md`. Use the doc links above to understand scope, capabilities, and scenarios before installing or invoking a skill.

## Repository Documentation

Keep durable project knowledge in its authoritative artifact instead of maintaining a parallel memory hierarchy:

- requirements and behavior in project specs
- architecture and technical rationale in `docs/` or ADRs
- repository-wide agent and engineering rules in `AGENTS.md` or `CLAUDE.md`
- active work and follow-ups in the project issue tracker or task artifacts

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
- durable context optimization
- code review subagents
- delegated code review
- parallel code review
- openspec orchestration skill
- formal change workflow
- spec-driven development
- approval gate workflow
- startup research skill
- competitor analysis skill
- reusable prompt engineering workflows

Abbreviation guide:

- `ICA` = `Idea Credibility Analyst`
- `AB` = `Advanced Brainstorming`
- `CR` = `Closure Retrospective`
- `DCR` = `Dispatching Code Review Subagents`
- `OSO` = `OpenSpec Superpower Orchestration`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
