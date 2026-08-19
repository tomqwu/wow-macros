# Repository operating instructions

These instructions apply to the whole repository.

## Purpose

- Keep reusable World of Warcraft macros organized by class.
- When a conversation supplies useful macro context, distill it into the relevant repository files before publishing the work.
- Store actionable game information, not full chat transcripts. Never commit credentials, account details, private identifiers, or unrelated conversation content.
- Treat TBC Classic / TBC Anniversary as the default game version unless the user names another version. Record the game version, patch, and verification date when they matter.

## Content layout

- Use [`skills/build-tbc-macros/SKILL.md`](skills/build-tbc-macros/SKILL.md) whenever creating, generating, normalizing, localizing, or importing class macros.
- Derive macros from the recorded player level, talent allocation, key talents, role, content, spell rotation, cooldown plan, pets/forms/stances, targeting preferences, and client build. Record missing inputs as `Not supplied`; never invent them.
- Put each game version in its own top-level folder. The active TBC tree is `tbc/classes/`; do not mix content from incompatible game versions.
- Put class-specific content under `<version>/classes/<class>/` using lowercase kebab-case names.
- Put the English class page in `<version>/classes/<class>/README.md` so it renders automatically. Put the Simplified Chinese page beside it as `README_zhCN.md`, and add reciprocal locale links at the top of both files. Do not create one file per macro.
- Put distilled cross-session macro material in the source locale's class page under a clearly marked imported-reference section. Summarize and link to it from the other locale page.
- Imported references must declare their source scope, game version, client locale, import date, and verification status. They do not count as verified macro variants.
- Use the skill's required localized section order and status model. Single-language or untested material stays in the source page's backlog; only macros with matching entries on both locale pages belong in the macro set.
- Give each macro its own specialization-and-purpose heading on both locale pages and reuse the same stable ID and status.
- Put `enUS` macro code and English explanations in `README.md`; put structurally matching `zhCN` macro code and Chinese explanations in `README_zhCN.md`.
- Repeat a client-neutral macro on both locale pages so their macro IDs remain complete.
- Keep localized macro variants behaviorally identical and verify spell, item, talent, and aura names in the corresponding client before publishing.
- Follow `LOCALIZATION.md` for bilingual content and verification requirements.
- Run `python3 skills/build-tbc-macros/scripts/validate_repository.py .` before committing class-page changes.
- Update the nearest README when adding, moving, or retiring content.

## Git workflow

- Make one small, focused commit for each fix or feature.
- Inspect and validate the exact diff before committing.
- Preserve unrelated user changes and never stage them silently.
- Finish completed work on `main`, merge feature branches without rewriting shared history, and push `main` to `origin`.
- Never force-push unless the user explicitly requests it and the exact impact has been checked.
