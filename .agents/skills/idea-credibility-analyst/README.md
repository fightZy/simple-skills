# Idea Credibility Analyst

`Idea Credibility Analyst` is a reusable skill for evaluating whether a product, startup, feature, or workflow idea is worth pursuing.

## What It Does

This skill helps an agent turn a vague idea discussion into a structured credibility assessment.

It is designed to:

- clarify the idea through focused dialogue
- research competing products, open-source projects, and community discussion
- compare alternatives by positioning, maturity, strengths, and gaps
- assess how crowded the market is
- recommend `continue`, `pivot`, or `stop`

## Capabilities

The skill is built to keep idea evaluation disciplined and evidence-driven.

- Focused clarification
  Ask one high-value question at a time instead of dumping a long questionnaire.
- Research with current evidence
  Prefer official sites, docs, code, release history, and recent community discussion.
- Competitive comparison
  Build a compact view of serious alternatives, not superficial name lists.
- Crowdedness assessment
  Judge whether the space is uncrowded, moderately crowded, crowded, or hyper-competitive.
- Clear decision output
  End with an explicit recommendation and rationale.

## When To Use

Use this skill when the user wants a rigorous go or no-go assessment instead of loose brainstorming.

Typical use cases:

- evaluating a startup or SaaS concept
- checking whether a feature idea is differentiated enough
- validating a workflow automation idea before building
- understanding whether an idea has a clear wedge or is too crowded

Typical questions it helps answer:

- Is this idea already saturated?
- Who else is solving this problem?
- What is the most realistic wedge?
- Should this continue, pivot, or stop?

## Skill Contents

- [`SKILL.md`](./SKILL.md): main runtime instructions
- [`README_zh.md`](./README_zh.md): Chinese introduction
- [`agents/openai.yaml`](./agents/openai.yaml): agent-facing metadata
- [`references/interview-playbook.md`](./references/interview-playbook.md): stronger discovery flow
- [`references/rubric.md`](./references/rubric.md): evaluation criteria
- [`references/report-template.md`](./references/report-template.md): response structure

## Notes

This README is a high-level introduction. The actual operating instructions live in [`SKILL.md`](./SKILL.md).
