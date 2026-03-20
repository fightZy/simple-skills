# Memory Maintenance

Use this guide when the task is to edit existing memory, deduplicate entries, repair structure, or keep the memory index coherent over time.

## Maintenance Goal

Keep workspace memory trustworthy, compact, and easy to navigate. Maintenance should improve retrieval quality, not just add more text.

## Common Maintenance Tasks

- update an existing session file with clearer decisions or follow-up items
- merge duplicate or overlapping summary entries
- remove stale placeholders such as `None yet.`
- repair links between summaries, crystals, and session files
- rename vague files to stable topic-based names
- keep recent memory compact and topic summaries coherent

## Edit Rules

When modifying existing memory:
- preserve the original intent unless the new information clearly supersedes it
- prefer updating the most relevant existing file instead of creating a near-duplicate
- keep file names and headings stable when possible
- do not rewrite history silently when a decision changed; mark it as updated or superseded

## Handling Conflicts

If two memory files disagree:
1. prefer crystallized guidance for standing norms
2. prefer newer summaries for active state
3. open the relevant session files if the conflict affects current work
4. update the conflicting memory so the contradiction is reduced for future readers

If the conflict cannot be resolved from memory alone, say so explicitly.

## Deduplication Rules

Merge entries when they:
- describe the same decision
- refer to the same implementation thread
- repeat the same convention with different wording

Keep separate entries when they:
- reflect distinct phases of the work
- show an intentional decision change over time
- are both useful for historical context

## Shrink The Front Door

The top of the tree must stay concise:
- `index.md` should remain a navigation file, not a dump of project history
- `summaries/recent.md` should optimize for quick recovery
- crystals should hold reusable knowledge, not session chatter

If a top-level file becomes long, move detail down one layer instead of adding more headings indefinitely.

## Maintenance Output Style

When you perform maintenance, report:
- which files were updated
- whether content was merged, shortened, or superseded
- any unresolved ambiguity that still exists in memory
