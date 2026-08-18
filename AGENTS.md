# Repository operating instructions

These instructions apply to the whole repository.

## Purpose

- Keep reusable World of Warcraft macros and talent loadouts organized by class.
- When a conversation supplies useful macro or talent context, distill it into the relevant repository files before publishing the work.
- Store actionable game information, not full chat transcripts. Never commit credentials, account details, private identifiers, or unrelated conversation content.
- Treat Retail as the default game version unless the user names Classic or another version. Record the game version, patch, and verification date when they matter.

## Content layout

- Put class-specific content under `classes/<class>/` using lowercase kebab-case names.
- Put macros in `classes/<class>/macros/`.
- Put talent builds and import strings in `classes/<class>/talents/`.
- Put distilled cross-session material that still needs verification or localization in `classes/<class>/context/`.
- Context references must declare their source scope, game version, client locale, import date, and verification status. They do not count as published macro or talent variants.
- For macros containing localized game text, publish matching `<specialization>-<purpose>.enUS.macro`, `<specialization>-<purpose>.zhCN.macro`, and `<specialization>-<purpose>.zhTW.macro` files.
- Use an unsuffixed `<specialization>-<purpose>.macro` only when every token is client-language neutral.
- Name talent files `<specialization>-<build>.md`.
- Include English (`enUS`), Simplified Chinese (`zhCN`), and Traditional Chinese (`zhTW`) explanations in each talent file. Talent import strings normally remain shared.
- Include the specialization, intended content type, game version or patch, and verification date in talent notes.
- Keep localized macro variants behaviorally identical and verify spell, item, talent, and aura names in the corresponding client before publishing.
- Follow `LOCALIZATION.md` for bilingual content and verification requirements.
- Update the nearest README when adding, moving, or retiring content.

## Git workflow

- Make one small, focused commit for each fix or feature.
- Inspect and validate the exact diff before committing.
- Preserve unrelated user changes and never stage them silently.
- Finish completed work on `main`, merge feature branches without rewriting shared history, and push `main` to `origin`.
- Never force-push unless the user explicitly requests it and the exact impact has been checked.
