#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import re

CRYSTAL_SECTION_ORDER = [
    "Statement",
    "Why It Matters",
    "When To Apply",
    "Provenance",
    "Notes",
]

TOPIC_SUMMARY_SECTION_ORDER = [
    "Current State",
    "Key Decisions",
    "Relevant Crystals",
    "Source Trail",
]


def today_iso() -> str:
    return str(date.today())


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "memory"


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text

    try:
        _start, remainder = text.split("---\n", 1)
        frontmatter_text, body = remainder.split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("Malformed frontmatter block") from exc

    metadata: dict[str, object] = {}
    current_key: str | None = None
    list_accumulator: list[str] = []

    for raw_line in frontmatter_text.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError("List item appeared before a list key")
            list_accumulator.append(_unquote(line[4:].strip()))
            continue

        if current_key is not None:
            metadata[current_key] = list_accumulator
            current_key = None
            list_accumulator = []

        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key = key.strip()
        value = value.strip()
        if value == "":
            current_key = key
            list_accumulator = []
        elif value == "[]":
            metadata[key] = []
        else:
            metadata[key] = _unquote(value)

    if current_key is not None:
        metadata[current_key] = list_accumulator

    return metadata, body.lstrip("\n")


def dump_frontmatter(metadata: dict[str, object], body: str) -> str:
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, list):
            lines.append(f"{key}:{yaml_list([str(item) for item in value])}")
        else:
            lines.append(f"{key}: {yaml_scalar(str(value))}")
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body.lstrip("\n")


def normalize_list(items: list[str]) -> list[str]:
    cleaned: list[str] = []
    seen: set[str] = set()
    for item in items:
        stripped = item.strip()
        if not stripped or stripped in seen:
            continue
        seen.add(stripped)
        cleaned.append(stripped)
    return cleaned


def parse_bullets(text: str) -> list[str]:
    bullets: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- ") and stripped != "- None yet.":
            bullets.append(stripped[2:])
    return normalize_list(bullets)


def metadata_list(
    metadata: dict[str, object],
    key: str,
    set_items: list[str] | None = None,
    add_items: list[str] | None = None,
) -> list[str]:
    if set_items:
        result = normalize_list(set_items)
    else:
        current = metadata.get(key, [])
        if isinstance(current, list):
            result = normalize_list([str(item) for item in current])
        elif current:
            result = normalize_list([str(current)])
        else:
            result = []
    if add_items:
        result = normalize_list(result + add_items)
    metadata[key] = result
    return result


def validate_required_metadata(
    metadata: dict[str, object], required_fields: list[str]
) -> None:
    for field in required_fields:
        value = metadata.get(field)
        if isinstance(value, list):
            if not value:
                raise ValueError(f"Required metadata field is empty: {field}")
            continue
        if value is None or not str(value).strip():
            raise ValueError(f"Required metadata field is empty: {field}")


def yaml_scalar(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def yaml_list(items: list[str]) -> str:
    cleaned = normalize_list(items)
    if not cleaned:
        return " []"
    return "\n" + "\n".join(f"  - {yaml_scalar(item)}" for item in cleaned)


def bullet_list(items: list[str], placeholder: str = "- None yet.") -> str:
    cleaned = normalize_list(items)
    if not cleaned:
        return placeholder
    return "\n".join(f"- {item}" for item in cleaned)


def resolve_path(root: Path, target: str) -> Path:
    path = Path(target)
    if path.is_absolute():
        return path
    return root / path


def split_section(
    text: str, heading: str, section_order: list[str] | None = None
) -> tuple[str, str, str]:
    marker = f"## {heading}\n"
    if marker not in text:
        if section_order and heading in section_order:
            heading_index = section_order.index(heading)
            for next_heading in section_order[heading_index + 1 :]:
                next_marker = f"\n## {next_heading}\n"
                insert_at = text.find(next_marker)
                if insert_at != -1:
                    before = text[: insert_at + 1].rstrip()
                    after = text[insert_at + 1 :]
                    return before + f"\n\n{marker}", "", after
        return text.rstrip() + f"\n\n{marker}", "", ""
    before, after = text.split(marker, 1)
    next_header = "\n## "
    split_index = after.find(next_header)
    if split_index == -1:
        return before + marker, after.strip("\n"), ""
    return before + marker, after[:split_index].strip("\n"), after[split_index:]


def update_section(
    text: str,
    heading: str,
    entries: list[str],
    mode: str,
    section_order: list[str] | None = None,
) -> str:
    if section_order is None:
        if heading in CRYSTAL_SECTION_ORDER:
            section_order = CRYSTAL_SECTION_ORDER
        elif heading in TOPIC_SUMMARY_SECTION_ORDER:
            section_order = TOPIC_SUMMARY_SECTION_ORDER

    prefix, section_body, suffix = split_section(text, heading, section_order)
    if mode == "append":
        combined = parse_bullets(section_body) + normalize_list(entries)
        new_body = bullet_list(combined)
    elif mode == "replace":
        new_body = bullet_list(entries)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    return (prefix + new_body + suffix).rstrip() + "\n"


def write_text(path: Path, content: str, force: bool = False) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Target already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _unquote(value: str) -> str:
    if len(value) >= 2 and value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value
