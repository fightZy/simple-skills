# Workspace Memory Config

Workspace memory can carry a repo-local config file at `docs/memory/config.toml`.

Current supported field:

```toml
content_language = "en"
```

## Rules

- `content_language` controls body prose only.
- Headings remain in their scripted English form.
- Filenames remain ASCII-friendly.
- If the config is missing, treat body language as English.

## Initialization

During first-time initialization, infer the user's preferred language from the current conversation and pass it to `init_memory.py --content-language ...`.

Use:

```bash
python3 scripts/init_memory.py --root <workspace> --content-language <en|zh-CN>
```

Validate:

```bash
python3 scripts/check_memory_language.py --root <workspace>
```
