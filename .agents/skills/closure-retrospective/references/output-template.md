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
- Future trigger: [what kind of future task or situation should activate this guidance]
- Prevented failure: [what mistake, churn, or delay this guidance prevents]

### Placement

- Codification action: [Create new skill | Update existing skill | Update existing constraint | Add constraint section]
- Recommended target: [new skill name | existing skill | AGENTS.md | CLAUDE.md]
- Existing artifact to update: [file or skill name, or `none - new artifact`]
- Placement decision: [create new skill | extend existing section | add new section]
- Target section or proposed artifact: [existing heading, proposed new heading, or proposed skill name]
- Why this location: [why this is the narrowest clean fit]

### Impact

- Expected benefit: [maintainability, health, performance, speed, consistency, safety, etc.]
- Maintenance risk: [what extra burden this adds]
- Action delta: [how future agent behavior changes after this is codified]
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
- Do not bury the codification action or target file decision.
- Do not omit the placement decision inside the target artifact, or the proposed name when creating a new artifact.
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
