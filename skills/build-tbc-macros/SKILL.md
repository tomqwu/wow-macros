---
name: build-tbc-macros
description: Build, normalize, and maintain English (enUS) and Simplified Chinese (zhCN) World of Warcraft TBC Classic or TBC Anniversary macro collections from player context such as class, level, talent allocation, key talents, role, content, spell rotation, pets or forms, items, addons, targeting preferences, and keybinds. Use when creating or revising a class macro page, importing macro context from another chat, deriving macros from a player's build and rotation, localizing TBC macros, separating verified macros from raw source notes, or validating this repository's class README format.
---

# Build TBC macros

Turn player-specific TBC context into a maintainable class macro collection. Keep all macros for a class in that class's `README.md`; never create one file per macro.

## Workflow

1. Read the repository `AGENTS.md` and the target class `README.md`.
2. Capture the player profile defined in [references/class-schema.md](references/class-schema.md). Use `Not supplied` for missing facts; do not invent a talent build, rotation, rank, item, pet ability, or client result.
3. Read [references/tbc-macro-rules.md](references/tbc-macro-rules.md) before generating, changing, or reviewing macro behavior.
4. Model the player's opener, sustained priority, cooldown plan, emergency actions, targeting needs, and keybind constraints. Identify useful macro opportunities and actions that must remain manual.
5. Generate the smallest useful macro set. Derive each entry from a named rotation step, talent, role requirement, or utility need.
6. Keep matching `English (enUS)` and `简体中文 (zhCN)` code blocks under the same macro entry. Keep conditionals and behavior identical; localize only game tokens.
7. Apply the status rules in [references/class-schema.md](references/class-schema.md). Single-language or untested session imports belong in `Imported reference backlog`, not in `Macro set`.
8. Start new class pages from [assets/class-readme-template.md](assets/class-readme-template.md). When normalizing an existing page, preserve useful source context under its backlog rather than discarding it.
9. Update the verification log. Mark a macro `verified` only when both locale variants were tested on the named client build.
10. Run `python3 skills/build-tbc-macros/scripts/validate_repository.py <repo-root>` and fix every reported error before publishing.

## Decision rules

- Ask only for missing information that materially changes the macro: class/build, key talents, intended content, rotation, client locale, or target priority. Otherwise record the gap and continue safely.
- Treat TBC Classic and TBC Anniversary client behavior as build-sensitive. Record the exact version when available.
- Use rotation and talent context to choose macro opportunities; do not claim to automate a combat rotation or make protected combat decisions.
- Prefer several clear keypresses over a brittle all-in-one macro.
- Keep numerical item slots or other locale-neutral commands in one shared block only when every token is truly client-neutral.
- Preserve privacy. Remove character names, account details, credentials, and unrelated chat instructions from imported material.

## Repository output

For every class, maintain these sections in order:

1. `Player profile`
2. `Rotation and talent model`
3. `Macro set`
4. `Imported reference backlog`
5. `Verification log`

Use stable lowercase IDs such as `restoration-emergency-heal` or `combat-focus-kick`. Do not silently change an existing ID when revising behavior.
