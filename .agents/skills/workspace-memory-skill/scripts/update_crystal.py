#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from memory_ops import dump_frontmatter, parse_frontmatter, resolve_path, slugify, today_iso, update_section


def main() -> int:
    parser = argparse.ArgumentParser(description="Update a workspace-memory crystal.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--path", help="Explicit crystal file path.")
    parser.add_argument("--id", help="Crystal id, for example crystal:repo-local-markdown-first.")
    parser.add_argument("--summary", help="Replace the crystal summary.")
    parser.add_argument("--append-statement", action="append", default=[], help="Statement bullet to append.")
    parser.add_argument("--replace-statement", action="append", default=[], help="Replace statement bullets.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if args.path:
        target = resolve_path(root, args.path)
    elif args.id:
        slug = slugify(args.id.split(":", 1)[-1])
        target = root / args.memory_dir / "crystals" / f"crystal-{slug}.md"
    else:
        raise SystemExit("Provide --path or --id")

    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    original_text = target.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(original_text)
    if metadata.get("memory_type") != "crystal":
        raise SystemExit(f"Expected memory_type crystal, got {metadata.get('memory_type')!r}")

    if args.summary:
        metadata["summary"] = args.summary
    metadata["updated_at"] = today_iso()

    if args.replace_statement:
        body = update_section(body, "Statement", args.replace_statement, mode="replace")
    if args.append_statement:
        body = update_section(body, "Statement", args.append_statement, mode="append")

    target.write_text(dump_frontmatter(metadata, body), encoding="utf-8")
    print(f"update {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
