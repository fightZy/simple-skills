#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from memory_ops import (
    CRYSTAL_SECTION_ORDER,
    dump_frontmatter,
    metadata_list,
    parse_frontmatter,
    resolve_path,
    slugify,
    today_iso,
    update_section,
    validate_required_metadata,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update a workspace-memory crystal.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--memory-dir", default="docs/memory", help="Memory directory relative to the workspace root.")
    parser.add_argument("--path", help="Explicit crystal file path.")
    parser.add_argument("--id", help="Crystal id, for example crystal:repo-local-markdown-first.")
    parser.add_argument("--summary", help="Replace the crystal summary.")
    parser.add_argument("--add-tag", action="append", default=[], help="Tag to add.")
    parser.add_argument("--set-tag", action="append", default=[], help="Replace tags with the provided values.")
    parser.add_argument("--add-source-id", action="append", default=[], help="Source id to add.")
    parser.add_argument("--set-source-id", action="append", default=[], help="Replace source ids with the provided values.")
    parser.add_argument("--add-applies-to", action="append", default=[], help="Path or glob to add to applies_to.")
    parser.add_argument("--set-applies-to", action="append", default=[], help="Replace applies_to values.")
    parser.add_argument("--append-statement", action="append", default=[], help="Statement bullet to append.")
    parser.add_argument("--replace-statement", action="append", default=[], help="Replace statement bullets.")
    parser.add_argument("--append-why-it-matters", action="append", default=[], help="Why-it-matters bullet to append.")
    parser.add_argument("--replace-why-it-matters", action="append", default=[], help="Replace why-it-matters bullets.")
    parser.add_argument("--append-when-to-apply", action="append", default=[], help="When-to-apply bullet to append.")
    parser.add_argument("--replace-when-to-apply", action="append", default=[], help="Replace when-to-apply bullets.")
    parser.add_argument("--append-note", action="append", default=[], help="Note bullet to append.")
    parser.add_argument("--replace-note", action="append", default=[], help="Replace note bullets.")
    parser.add_argument("--append-provenance", action="append", default=[], help="Provenance bullet to append.")
    parser.add_argument("--replace-provenance", action="append", default=[], help="Replace provenance bullets.")
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
    metadata_list(metadata, "tags", set_items=args.set_tag, add_items=args.add_tag)
    metadata_list(
        metadata,
        "source_ids",
        set_items=args.set_source_id,
        add_items=args.add_source_id,
    )
    metadata_list(
        metadata,
        "applies_to",
        set_items=args.set_applies_to,
        add_items=args.add_applies_to,
    )
    metadata["updated_at"] = today_iso()
    try:
        validate_required_metadata(
            metadata,
            [
                "id",
                "memory_type",
                "title",
                "summary",
                "created_at",
                "updated_at",
                "knowledge_type",
                "source_ids",
            ],
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    if args.replace_statement:
        body = update_section(body, "Statement", args.replace_statement, mode="replace", section_order=CRYSTAL_SECTION_ORDER)
    if args.append_statement:
        body = update_section(body, "Statement", args.append_statement, mode="append", section_order=CRYSTAL_SECTION_ORDER)
    if args.replace_why_it_matters:
        body = update_section(body, "Why It Matters", args.replace_why_it_matters, mode="replace", section_order=CRYSTAL_SECTION_ORDER)
    if args.append_why_it_matters:
        body = update_section(body, "Why It Matters", args.append_why_it_matters, mode="append", section_order=CRYSTAL_SECTION_ORDER)
    if args.replace_when_to_apply:
        body = update_section(body, "When To Apply", args.replace_when_to_apply, mode="replace", section_order=CRYSTAL_SECTION_ORDER)
    if args.append_when_to_apply:
        body = update_section(body, "When To Apply", args.append_when_to_apply, mode="append", section_order=CRYSTAL_SECTION_ORDER)
    if args.replace_note:
        body = update_section(body, "Notes", args.replace_note, mode="replace", section_order=CRYSTAL_SECTION_ORDER)
    if args.append_note:
        body = update_section(body, "Notes", args.append_note, mode="append", section_order=CRYSTAL_SECTION_ORDER)
    if args.replace_provenance:
        body = update_section(body, "Provenance", args.replace_provenance, mode="replace", section_order=CRYSTAL_SECTION_ORDER)
    if args.append_provenance:
        body = update_section(body, "Provenance", args.append_provenance, mode="append", section_order=CRYSTAL_SECTION_ORDER)

    target.write_text(dump_frontmatter(metadata, body), encoding="utf-8")
    print(f"update {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
