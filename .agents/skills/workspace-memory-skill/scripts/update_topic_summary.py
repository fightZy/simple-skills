#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from memory_ops import dump_frontmatter, parse_frontmatter, resolve_path, slugify, today_iso, update_section


def main() -> int:
    parser = argparse.ArgumentParser(description="Update a workspace-memory topic summary.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--path", help="Explicit topic-summary file path.")
    parser.add_argument("--topic", help="Topic name used to resolve the default summary path.")
    parser.add_argument("--summary", help="Replace the topic summary one-line summary.")
    parser.add_argument("--append-current-state", action="append", default=[], help="Current-state bullet to append.")
    parser.add_argument("--replace-current-state", action="append", default=[], help="Replace current-state bullets.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if args.path:
        target = resolve_path(root, args.path)
    elif args.topic:
        target = root / args.memory_dir / "summaries" / "topics" / f"{slugify(args.topic)}.md"
    else:
        raise SystemExit("Provide --path or --topic")

    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    original_text = target.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(original_text)
    if metadata.get("memory_type") != "topic-summary":
        raise SystemExit(f"Expected memory_type topic-summary, got {metadata.get('memory_type')!r}")

    if args.summary:
        metadata["summary"] = args.summary
    metadata["updated_at"] = today_iso()

    if args.replace_current_state:
        body = update_section(body, "Current State", args.replace_current_state, mode="replace")
    if args.append_current_state:
        body = update_section(body, "Current State", args.append_current_state, mode="append")

    target.write_text(dump_frontmatter(metadata, body), encoding="utf-8")
    print(f"update {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
