# Refinement And Archiving

Use this guide when the task is to compress noisy recent memory, maintain long-term summaries, or keep the memory tree readable.

## Refinement Goal

Recent memory should stay fast to scan. Long-term memory should preserve what still matters. Session files should remain the source of traceability.

## What To Refine

Candidates for refinement:
- repeated recent entries about the same topic
- resolved follow-ups that no longer need front-page visibility
- debugging detail that mattered during execution but is no longer a top-level concern
- historical sessions that still matter, but not in full detail

Do not refine away:
- key decisions and their rationale
- active risks
- unresolved questions
- context likely to be needed for handoff or review

## When To Archive

Archive when one or more of these conditions hold:
- `summaries/recent.md` has grown large enough that fast scanning is degrading
- entries are older and no longer influence daily work
- multiple recent entries can be collapsed into one durable historical summary
- the active context and pending follow-ups no longer depend on those entries

Reasonable default heuristics:
- archive after a topic is no longer active
- archive when recent memory starts carrying mostly historical rather than current context
- archive by topic coherence before archiving by age alone

## Refinement Process

1. Read `summaries/recent.md`
2. Identify stale or repetitive entries
3. Group them by topic, milestone, or decision thread
4. Write a compressed summary into `summaries/archive.md` or a topic summary
5. Preserve links or filenames for any session files still worth revisiting
6. Remove or shorten the corresponding recent entries
7. If the compressed result yields a reusable rule, update crystallized memory too

## Compression Standard

Good archive entries keep:
- what happened
- why it mattered
- what decision or outcome resulted

Good archive entries omit:
- step-by-step debugging chatter
- repeated explanations
- temporary confusion that taught no durable lesson

## Topic Summaries

Create `summaries/topics/<topic>.md` when:
- a topic recurs often enough that `recent.md` becomes cluttered
- contributors regularly need context in that area
- several sessions point to the same subsystem or workflow

Topic summaries should be:
- shorter than the combined source sessions
- organized by subtopic or decision thread
- updated instead of duplicated

## Archive Output Style

When you refine memory, explain:
- what moved out of recent memory
- where the compressed result now lives
- whether any durable rule was crystallized from the change
