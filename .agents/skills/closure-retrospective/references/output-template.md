# Output Template

Use this structure when at least one codifiable suggestion survives the rubric.

## Recommended shape

```markdown
Worth codifying: yes

1. [Short recommendation title]
Observation: [what happened in this task]
Evidence from this task: [specific repeated correction, friction, or improvement]
Why reusable: [why it is likely to recur]
Recommended target: [existing skill | new skill | AGENTS.md | CLAUDE.md]
Expected benefit: [maintainability, health, performance, speed, consistency, safety, etc.]
Maintenance risk: [what extra burden this adds]
Proposed change summary: [one concise sentence]

2. [Optional second recommendation]
...

If you approve, I will apply the suggested edits.
```

## Limits

- Suggest at most 3 items.
- Keep each item specific and evidence-backed.
- Do not bury the target file decision.
- Do not include patch text unless the user asks for it.
- Do not imply edits already happened.

## No-Change Case

If the user explicitly asked for a retrospective and nothing qualifies:

```markdown
Worth codifying: no

No candidate from this task cleared the bar for durable guidance.
```

If the user did not explicitly ask for a retrospective, surface nothing and finish normally.
