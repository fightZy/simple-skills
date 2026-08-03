# Output Template

Read this file only after at least one candidate survives the decision rubric.

Default to a two-layer response: make the recommendation and its reason immediately visible, then separate any decision-useful analysis. Keep internal qualification fields out of the main result.

```markdown
# [conclusion-led title]

**Recommendation**

[State what should change, including the target and action, in one short paragraph.]

**Why**

[Explain the decisive evidence, problem, or expected benefit in one or two sentences.]

## Supporting analysis

[Include only details that help the user evaluate or apply the recommendation. Organize them around the content rather than a fixed field list. Omit this section when the recommendation and reason are sufficient.]

If you approve, I will apply only the named intervention and target.
```

Use a title that states the recommended direction; do not use a generic retrospective title. Match headings and labels to the user's language.

For one candidate, use the conclusion-led title directly without a wrapper. For several independent candidates, use one shared theme as the top-level title and give each candidate a numbered conclusion-led heading. Include at most three.

Keep the main layer limited to `Recommendation` and `Why`. When supporting analysis is needed, select only the relevant evidence and mechanism, scope and boundary, delivery and verification, or follow-up and lifecycle information. Use natural prose or content-specific subheadings; do not emit empty fields, `Not applicable`, or internal rubric labels.

Do not include patch text, claim later effect is already proven, or imply edits happened during the read-only retrospective.
