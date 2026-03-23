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

- [`ICA-EN`](./.agents/skills/idea-credibility-analyst/README.md): English overview
- [`ICA-ZH`](./.agents/skills/idea-credibility-analyst/README_zh.md): 中文说明
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

- [`WMS-EN`](./.agents/skills/workspace-memory-skill/README.md): English overview
- [`WMS-ZH`](./.agents/skills/workspace-memory-skill/README_zh.md): 中文说明
- [`WMS-SKILL`](./.agents/skills/workspace-memory-skill/SKILL.md): runtime instructions

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
```

These commands work with the `skills` CLI and are intended for skill-compatible agents and editors.

## Usage

After installation, each skill runs according to its own `SKILL.md`. Use the doc links above to understand scope, capabilities, and scenarios before installing or invoking a skill.

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
- project memory for coding agents
- reusable prompt engineering workflows

Abbreviation guide:

- `ICA` = `Idea Credibility Analyst`
- `WMS` = `Workspace Memory Skill`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
