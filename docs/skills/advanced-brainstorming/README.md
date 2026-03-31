# Advanced Brainstorming

This document is for maintainers of the skill, not for runtime routing. The runtime entrypoint remains `SKILL.md`.

## What This Skill Is

`advanced-brainstorming` is a standalone ideation skill for moments when the user wants a proposal pushed beyond cautious defaults.

It is designed to make an agent:

- surface hidden assumptions instead of accepting the first framing
- expand the current direction before replacing it
- generate frame-breaking alternatives and wildcards
- end with light prioritization instead of implementation planning

## Purpose

Use this skill when the user wants:

- richer brainstorming
- less conservative idea exploration
- more imaginative but still intelligible directions
- expansion of an existing proposal into multiple stronger possibilities

This skill is not for validation, research, or execution.

## Design Principles

- The user's initial framing is a starting point, not a fixed boundary.
- A strong answer should widen the possibility space before converging.
- Novelty should come from changed axes, not random decoration.
- Wild ideas are useful only if they stay interpretable.
- The skill should stop at light prioritization, not implementation.

## Output Style

The runtime skill defaults to a structured response:

1. hidden assumptions
2. expanded directions
3. frame-breaking alternatives
4. wildcards
5. most worth exploring next

This structure exists because baseline brainstorming often produced interesting ideas but did so inconsistently. The skill makes the stronger pattern repeatable.

## Relationship To Other Skills

This skill is intentionally standalone. It does not depend on other repository skills and should remain usable on its own.

## Verification

Typical verification should include prompt-pressure checks such as:

- a plausible idea that tempts the agent into optimization instead of divergence
- a vague concept that tempts the agent into filler
- a prompt that explicitly rejects the safest answer

Good outputs should show:

- visible assumption surfacing
- at least one meaningful reframing
- layered idea groups instead of one flat list
- light convergence without execution planning
