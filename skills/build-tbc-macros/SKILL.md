---
name: build-tbc-macros
description: Build, normalize, and maintain World of Warcraft TBC Classic or TBC Anniversary macro collections from player context such as class, level, talent allocation, key talents, role, content, spell rotation, pets or forms, items, addons, targeting preferences, and keybinds. Use when creating or revising class macro pages, importing macro context from another chat, deriving macros from a player's build and rotation, splitting English (enUS) and Simplified Chinese (zhCN) documentation, localizing TBC macros, separating verified macros from raw source notes, or validating this repository's paired README.md and README_zhCN.md format.
---

# Build TBC macros

Turn player-specific TBC context into a maintainable class macro collection. Keep the English view in the class `README.md` and the Simplified Chinese view in `README_zhCN.md`; never create one file per macro.

## Workflow

1. Read the repository `AGENTS.md` and both locale pages for the target class.
2. Capture the player profile defined in [references/class-schema.md](references/class-schema.md). Use `Not supplied` or `未提供` for missing facts; do not invent a build, rotation, rank, item, pet ability, or client result.
3. Read [references/tbc-macro-rules.md](references/tbc-macro-rules.md) before generating, changing, or reviewing macro behavior.
4. Model the player's opener, sustained priority, cooldown plan, emergency actions, targeting needs, and keybind constraints. Identify useful macro opportunities and actions that must remain manual.
5. Generate the smallest useful macro set. Derive each entry from a named rotation step, talent, role requirement, or utility need.
6. Put the `enUS` macro and English explanation in `README.md`. Put the matching `zhCN` macro and Chinese explanation in `README_zhCN.md`. Reuse the same stable ID, status, targeting order, modifiers, and command structure.
7. Apply the status rules in [references/class-schema.md](references/class-schema.md). Single-language or untested imports stay in the source locale's backlog; add a link from the other locale page instead of duplicating untranslated material.
8. Start new pages from [assets/class-readme-template.en.md](assets/class-readme-template.en.md) and [assets/class-readme-template.zhCN.md](assets/class-readme-template.zhCN.md). Preserve useful source context under backlog when normalizing existing pages.
9. Update matching verification logs. Mark a macro `verified` only when both locale variants were tested on the named client build.
10. Run `python3 skills/build-tbc-macros/scripts/validate_repository.py <repo-root>` and fix every reported error before publishing.

## Decision rules

- Ask only for missing information that materially changes the macro: class/build, key talents, intended content, rotation, client locale, or target priority. Otherwise record the gap and continue safely.
- Treat TBC Classic and TBC Anniversary behavior as build-sensitive. Record the exact version when available.
- Use rotation and talent context to choose macro opportunities; do not claim to automate a combat rotation or make protected combat decisions.
- Prefer several clear keypresses over a brittle all-in-one macro.
- Keep numerical item slots or other locale-neutral behavior structurally identical on both locale pages.
- Preserve privacy. Remove character names, account details, credentials, and unrelated chat instructions from imported material.

## Repository output

Maintain two reciprocal pages per class:

- `README.md`: default English page with a top link to `README_zhCN.md`.
- `README_zhCN.md`: Simplified Chinese page with a top link back to `README.md`.

Both pages contain the same five sections in their locale: player profile, rotation/talent model, macro set, imported-reference backlog, and verification log. Use stable lowercase IDs such as `restoration-emergency-heal` or `combat-focus-kick`; never silently change an ID when revising behavior.
