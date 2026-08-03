# Output Template

Read this file only after at least one candidate survives the decision rubric.

Default to a two-layer response: make the recommendation and its reason immediately visible, then separate any decision-useful analysis. Keep internal qualification fields out of the main result.

```markdown
# [conclusion-led title]

**Recommendation**

[State the recurring decision point, desired context state, smallest durable change, and owning target in one short paragraph. Keep task-specific evidence out of this paragraph unless it defines a real scope boundary.]

**Why**

[Explain how the current context influenced the observed decision and why the desired context would improve or preserve later behavior in one or two sentences.]

## Supporting analysis

[Include only details that help the user evaluate or apply the recommendation. Organize them around the content rather than a fixed field list. Omit this section when the recommendation and reason are sufficient.]

If you approve, I will apply only the named context change and target.
```

Use a title that states the recommended direction; do not use a generic retrospective title. Match headings and labels to the user's language.

Generalize around the recurring decision and context effect, not the incident's nouns or a closed list of observed symptoms. Keep concrete task details in `Why` or supporting analysis as evidence. Stop abstracting when removing a term would erase a real scope boundary or actionable instruction.

For one candidate, use the conclusion-led title directly without a wrapper. For several independent candidates, use one shared theme as the top-level title and give each candidate a numbered conclusion-led heading. Include at most three.

Keep the main layer limited to `Recommendation` and `Why`. When supporting analysis is needed, select only the relevant evidence and context effect, scope and boundary, delivery and verification, or follow-up and lifecycle information. Use natural prose or content-specific subheadings; do not emit empty fields, `Not applicable`, or internal rubric labels.

Do not include patch text, claim later effect is already proven, or imply edits happened during the read-only retrospective.
