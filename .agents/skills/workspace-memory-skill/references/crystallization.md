# Crystallization Guide

Use this guide when the task is to turn repeated or durable project knowledge into standing memory.

## Crystallization Goal

Crystallized memory should capture what future contributors and agents ought to reuse without rereading the original conversations.

## What Belongs In Crystals

Good crystallization candidates:
- team conventions that should guide future work
- project decisions with durable consequences
- reusable implementation patterns
- recurring pitfalls with a preferred fix
- architecture rationale that keeps resurfacing

Poor candidates:
- one-off preferences
- temporary debugging notes
- superseded implementation detail
- unresolved speculation

## Crystal Destinations

Use these destinations consistently:

`crystals/team-conventions.md`
- default team behaviors
- documentation and review expectations
- collaboration norms

`crystals/project-decisions.md`
- decision records with context, rationale, and consequences
- active and superseded decisions when history still matters

`crystals/implementation-patterns.md`
- preferred implementation shapes
- recurring anti-patterns
- stable tactics contributors should reuse

## Promotion Rules

Promote something into crystallized memory when at least one is true:
- it has been repeated across sessions
- future contributors should act on it by default
- forgetting it would likely cause drift, rework, or bad decisions
- it explains why the project is intentionally shaped a certain way

Prefer evidence over intuition. If a point appears only once and is not clearly durable, keep it in session memory for now.

## Writing Style

Crystals should be:
- directive or declarative
- shorter than the source sessions
- explicit about scope and default behavior

Avoid:
- vague slogans
- unexplained preferences
- copying whole paragraphs from sessions

## Updating Existing Crystals

Before adding a new item:
1. read the relevant crystal file
2. merge with existing guidance if it is the same rule
3. mark older guidance as superseded when necessary
4. avoid duplicating the same norm in multiple crystal files unless the cross-reference is important

## Evidence And Traceability

When possible, preserve lightweight provenance:
- mention the related session date or file
- mention whether the rule is new, reinforced, or superseded

Do not turn crystals into a raw session index. They should remain readable as standing guidance.
