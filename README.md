# Simple Skills

This repository contains two reusable skills for agent workflows. It is a small public skills repo focused on two practical problems: evaluating whether an idea is worth pursuing, and preserving durable workspace memory across agent sessions.

## Skills

### Idea Credibility Analyst

A skill for evaluating whether a product, startup, feature, or workflow idea is worth pursuing.

It helps an agent move from vague discussion to structured judgment. The skill is designed for situations where the user does not just want brainstorming, but wants a sharper answer to whether an idea has enough differentiation, demand, and room to justify further work.

Core capabilities:

- focused clarification instead of broad questionnaires
- competitor and alternative research
- market crowdedness assessment
- structured comparison of positioning, maturity, and gaps
- final `continue` / `pivot` / `stop` recommendation

Typical use cases:

- validating a startup or SaaS concept
- pressure-testing a feature before building it
- checking whether a workflow automation idea has a real wedge
- understanding whether a space is too crowded or still has room

Docs:

- [`ICA-EN`](./.agents/skills/idea-credibility-analyst/README.md): English overview
- [`ICA-ZH`](./.agents/skills/idea-credibility-analyst/README_zh.md): 中文说明
- [`ICA-SKILL`](./.agents/skills/idea-credibility-analyst/SKILL.md): runtime instructions

### Workspace Memory Skill

A skill for maintaining repo-local workspace memory across agent sessions.

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

Docs:

- [`WMS-EN`](./.agents/skills/workspace-memory-skill/README.md): English overview
- [`WMS-ZH`](./.agents/skills/workspace-memory-skill/README_zh.md): 中文说明
- [`WMS-SKILL`](./.agents/skills/workspace-memory-skill/SKILL.md): runtime instructions

## Install

List the skills available in this repository:

```bash
npx skills add fightZy/simple-skills --list
```

Install a specific skill from the repo:

```bash
npx skills add fightZy/simple-skills --skill idea-credibility-analyst
npx skills add fightZy/simple-skills --skill workspace-memory-skill
```

## Usage

After installation, each skill runs according to its own `SKILL.md`. Use the doc links above to understand scope, capabilities, and scenarios before installing or invoking a skill.

Abbreviation guide:

- `ICA` = `Idea Credibility Analyst`
- `WMS` = `Workspace Memory Skill`
- `EN` = English README
- `ZH` = Chinese README

## License

This repository is licensed under the [MIT License](./LICENSE).
