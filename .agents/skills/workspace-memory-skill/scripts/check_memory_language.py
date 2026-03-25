#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re

from memory_ops import parse_frontmatter


ALLOWED_HEADING_PATTERNS = [
    re.compile(r"^# Workspace Memory$"),
    re.compile(r"^# Recent Memory$"),
    re.compile(r"^# Archived Memory$"),
    re.compile(r"^# Session: .+$"),
    re.compile(r"^# Crystal: .+$"),
    re.compile(r"^# Topic Summary: .+$"),
    re.compile(r"^## Purpose$"),
    re.compile(r"^## Suggested Entry Points$"),
    re.compile(r"^## Key Files$"),
    re.compile(r"^## Active Context$"),
    re.compile(r"^## Recent Sessions$"),
    re.compile(r"^## Pending Follow-ups$"),
    re.compile(r"^## Important History$"),
    re.compile(r"^## Reusable Context$"),
    re.compile(r"^## Goal$"),
    re.compile(r"^## Key Decisions$"),
    re.compile(r"^## Rationale$"),
    re.compile(r"^## Changes$"),
    re.compile(r"^## Open Questions$"),
    re.compile(r"^## Follow-up$"),
    re.compile(r"^## Crystallization Candidates$"),
    re.compile(r"^## Related Files$"),
    re.compile(r"^## Related References$"),
    re.compile(r"^## Statement$"),
    re.compile(r"^## Why It Matters$"),
    re.compile(r"^## When To Apply$"),
    re.compile(r"^## Provenance$"),
    re.compile(r"^## Notes$"),
    re.compile(r"^## Current State$"),
    re.compile(r"^## Relevant Crystals$"),
    re.compile(r"^## Source Trail$"),
]

AUTHORING_MEMORY_TYPES = {"session", "crystal", "topic-summary"}
ENGLISH_PLACEHOLDERS = {
    "What this session tried to resolve.",
    "- Decision",
    "- Why the decision was made",
    "- What changed in code, docs, or plans",
    "- What remains unresolved",
    "- Next actions",
    "- Rules, patterns, decisions, or insights worth promoting",
    "- The durable rule, decision, pattern, or insight.",
    "- Why future contributors should care.",
    "- Situations where this knowledge should guide actions.",
    "- Source session or summary ids",
    "- Caveats, exceptions, or supersession notes",
    "- What is currently true",
    "- Important decisions to remember",
    "- Crystal ids or links worth reading first",
    "- Source ids or filenames",
}
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def read_content_language(memory_dir: Path) -> str:
    config_path = memory_dir / "config.toml"
    if not config_path.exists():
        return "en"

    for line in config_path.read_text(encoding="utf-8").splitlines():
        key, _sep, value = line.partition("=")
        if key.strip() != "content_language":
            continue
        cleaned = value.strip().strip('"').strip("'")
        if cleaned:
            return cleaned
    return "en"


def is_allowed_heading(line: str) -> bool:
    return any(pattern.fullmatch(line) for pattern in ALLOWED_HEADING_PATTERNS)


def body_lines(body: str) -> list[str]:
    return [line.rstrip() for line in body.splitlines()]


def validate_headings(path: Path, body: str) -> list[str]:
    errors: list[str] = []
    for line in body_lines(body):
        stripped = line.strip()
        if not stripped.startswith("#"):
            continue
        if not is_allowed_heading(stripped):
            errors.append(f"Unexpected heading in {path}: {stripped}")
    return errors


def validate_authored_body(path: Path, body: str, content_language: str) -> list[str]:
    errors: list[str] = []
    for line in body_lines(body):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if content_language == "zh-CN" and stripped in ENGLISH_PLACEHOLDERS:
            errors.append(
                f"Expected zh-CN body content in {path}, found English placeholder: {stripped}"
            )
        if content_language == "en" and CJK_RE.search(stripped):
            errors.append(
                f"Expected English body content in {path}, found Chinese text: {stripped}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate workspace-memory language rules.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument(
        "--memory-dir",
        default="docs/memory",
        help="Memory directory relative to the workspace root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    memory_dir = root / args.memory_dir
    content_language = read_content_language(memory_dir)
    errors: list[str] = []

    for path in sorted(memory_dir.rglob("*.md")):
        metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        errors.extend(validate_headings(path, body))
        if metadata.get("memory_type") in AUTHORING_MEMORY_TYPES:
            errors.extend(validate_authored_body(path, body, content_language))

    if errors:
        print("\n".join(errors))
        return 1

    print(
        f"Workspace memory language check passed for {memory_dir} "
        f"(content_language={content_language})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
