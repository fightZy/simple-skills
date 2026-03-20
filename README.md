# Simple Skills

This repository contains two reusable skills for agent workflows.

## Skills

### Idea Credibility Analyst

A skill for evaluating whether a product, startup, feature, or workflow idea is worth pursuing.

It focuses on idea clarification, competitive research, market crowdedness assessment, and a final `continue` / `pivot` / `stop` recommendation.

- English: [`.agents/skills/idea-credibility-analyst/README.md`](./.agents/skills/idea-credibility-analyst/README.md)
- 中文: [`.agents/skills/idea-credibility-analyst/README_zh.md`](./.agents/skills/idea-credibility-analyst/README_zh.md)
- Runtime entry: [`.agents/skills/idea-credibility-analyst/SKILL.md`](./.agents/skills/idea-credibility-analyst/SKILL.md)

### Workspace Memory Skill

A skill for maintaining repo-local workspace memory across agent sessions.

It focuses on structured session capture, layered summaries, archive refinement, and durable project knowledge inside a single repository.

- English: [`.agents/skills/workspace-memory-skill/README.md`](./.agents/skills/workspace-memory-skill/README.md)
- 中文: [`.agents/skills/workspace-memory-skill/README_zh.md`](./.agents/skills/workspace-memory-skill/README_zh.md)
- Runtime entry: [`.agents/skills/workspace-memory-skill/SKILL.md`](./.agents/skills/workspace-memory-skill/SKILL.md)

## Install

List available skills in the repo:

```bash
npx skills add <owner>/<repo> --list
```

Install a specific skill:

```bash
npx skills add <owner>/<repo> --skill idea-credibility-analyst
npx skills add <owner>/<repo> --skill workspace-memory-skill
```

## Usage

After installation, the runtime behavior is defined by each skill's [`SKILL.md`](./.agents/skills/idea-credibility-analyst/SKILL.md).

Use the linked README files above for a human-readable overview of purpose, capabilities, and usage scenarios.

## License

This repository is licensed under the [MIT License](./LICENSE).
