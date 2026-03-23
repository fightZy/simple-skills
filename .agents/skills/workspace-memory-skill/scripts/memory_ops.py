#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import re


def today_iso() -> str:
    return str(date.today())


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "memory"


def yaml_scalar(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def yaml_list(items: list[str]) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return " []"
    return "\n" + "\n".join(f"  - {yaml_scalar(item)}" for item in cleaned)


def bullet_list(items: list[str], placeholder: str = "- None yet.") -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return placeholder
    return "\n".join(f"- {item}" for item in cleaned)


def write_text(path: Path, content: str, force: bool = False) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Target already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
