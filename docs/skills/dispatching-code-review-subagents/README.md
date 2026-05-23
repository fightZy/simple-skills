# Dispatching Code Review Subagents

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`dispatching-code-review-subagents` is a lightweight review-routing skill for deciding how to delegate code review to subagents.

It is designed to make an agent:

- judge whether a review needs one reviewer, multiple themed reviewers, or layered review
- split review by risk area instead of by mechanical file count
- give each reviewer a bounded mission and output shape
- synthesize reviewer results without performing a second full review

## Purpose

Use this skill before assigning code review to subagents, especially after implementation milestones or before merging complex changes.

This skill is not for:

- implementing review fixes
- replacing the normal code-review output format
- forcing multiple subagents for small localized diffs

## Design Principles

- Cost-aware dispatch: split only when extra reviewers increase signal.
- Theme-first review: assign independent risk lenses such as contracts, data, security, tests, UI, or maintainability.
- Parallel by default: run independent review themes concurrently.
- Layer only when useful: stage review passes only when first-pass findings affect the second pass.
- Main agent as synthesizer: collect, deduplicate, rank, and call out gaps without re-reviewing every line.

## Verification

Good verification scenarios should check that the skill:

- chooses one reviewer for small localized diffs
- chooses parallel themed reviewers for broad multi-domain changes
- uses layered review only when later review depends on earlier findings
- keeps the main agent focused on routing and synthesis
