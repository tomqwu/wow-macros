# WoW Macros

[简体中文](README_zhCN.md)

A versioned library of World of Warcraft macros distilled from working conversations.

## Active version

| Version | Status | Browse |
| --- | --- | --- |
| TBC Classic / TBC Anniversary | Active | [Classes and macros](tbc/) |

Content is currently organized for TBC only. Future game versions should use sibling top-level folders so incompatible macros are never mixed.

## Generation workflow

Use the repository's [TBC Macro Builder skill](skills/build-tbc-macros/SKILL.md) to turn a player's level, talent build, key talents, rotation, role, content, targeting preferences, and client details into a compact macro set.

Every class uses two reciprocal pages:

- `README.md`: default English page with `enUS` macros.
- `README_zhCN.md`: Simplified Chinese page with matching `zhCN` macros.

Both pages share the same player model, stable macro IDs, statuses, command structure, and verification record. Single-language source material remains backlog on its source-locale page until a matching macro is created and tested.

## File conventions

- Default English class page: `<version>/classes/<class>/README.md`
- Simplified Chinese class page: `<version>/classes/<class>/README_zhCN.md`
- Put reciprocal locale links at the top of both files.
- Keep cross-session references awaiting verification in the source locale's backlog with an explicit status.
- Record the game version or patch and verification date when behavior can change.
- Give each macro a specialization-and-purpose heading and stable ID on both pages.
- Keep matching `enUS` and `zhCN` macros behaviorally and structurally identical.
- Do not create a separate file for each macro.

See [LOCALIZATION.md](LOCALIZATION.md) for client-language and verification rules.
