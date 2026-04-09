# Output Template

Use this structure when at least one codifiable suggestion survives the rubric.

## Recommended shape

```markdown
# Closure Retrospective

## Result

- Worth codifying: yes
- Recommendation count: [1-3]

## Recommendation 1: [Short recommendation title]

### Why this surfaced

- Observation: [what happened in this task]
- Evidence from this task: [specific repeated correction, friction, or improvement]

### Generalized guidance

- Durable guidance: [the reusable rule, rubric, or heuristic]
- Why this generalizes: [why it is likely to recur]

### Placement

- Recommended target: [existing skill | new skill | AGENTS.md | CLAUDE.md]
- Existing artifact to update: [file or skill name]
- Placement decision: [extend existing section | add new section]
- Target section: [existing heading name, or proposed new heading]
- Why this location: [why this is the narrowest clean fit]

### Impact

- Expected benefit: [maintainability, health, performance, speed, consistency, safety, etc.]
- Maintenance risk: [what extra burden this adds]
- Proposed change summary: [one concise sentence]

## Recommendation 2: [Optional short recommendation title]

[Repeat the same section structure only if needed]

## Next Step

If you approve, I will apply the suggested edits.
```

## Limits

- Suggest at most 3 items.
- Keep each item specific and evidence-backed.
- Rewrite every item into guidance that can stand outside the current task.
- Match the user's language preference; if none is stated, default to the language used in the user's request.
- Do not bury the target file decision.
- Do not omit the placement decision inside the target artifact.
- Do not include patch text unless the user asks for it.
- Do not imply edits already happened.

## No-Change Case

If the user explicitly asked for a retrospective and nothing qualifies:

```markdown
# Closure Retrospective

## Result

- Worth codifying: no

## Reason

No candidate from this task cleared the bar for durable guidance.
```

If the user did not explicitly ask for a retrospective, surface nothing and finish normally.
