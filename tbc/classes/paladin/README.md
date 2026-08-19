# Paladin macros

[简体中文](README_zhCN.md)

## Player profile

| Field | Value |
| --- | --- |
| Game version | WoW TBC Classic / TBC Anniversary; exact client build not supplied |
| Class | Paladin |
| Level | 70 |
| Talent build | The source spans Retribution, Protection, and Holy; no single point allocation was supplied |
| Key talents | The source includes Crusader Strike, Avenger's Shield, Holy Shock, Divine Favor, and other build-specific actions |
| Role / content | Retribution questing and raid play, Protection tanking, Holy healing, universal utility, and engineering items |
| Rotation source | The imported `zhCN` pack covers Retribution seal-twist timing plus Protection and Holy priorities |
| Client locale | English (`enUS`) |
| Last updated | 2026-08-19 |
| Overall status | The multi-build `zhCN` source remains `imported-reference`; no paired macro set yet |

## Rotation and talent model

### Player rotation

- Opener: The source includes a Retribution raid opener using Judgement and seal setup; Protection and Holy openers have not been normalized.
- Sustained priority: Retribution seal twisting, Protection threat actions, and Holy healing choices are documented in separate source sections.
- Cooldowns / emergencies: The source includes Avenging Wrath, trinkets, Divine Favor healing, immunities, blessings, and Lay on Hands.

### Macro opportunities

- Generate one build-specific macro set after the active talent allocation and role are selected.
- Derive seal, Judgement, healing mouseover, taunt, blessing, immunity, and item macros from the chosen rotation and utility plan.

### Deliberately not macroed

- Seal-twist swing timing, Judgement decisions, tank threat priority, and healing triage remain player-controlled.
- Macros from mutually exclusive builds are not promoted together as one player loadout.

## Macro set

No paired macros yet. Select one active Paladin build, then localize and test only the relevant source macros in both clients.

## Imported reference backlog

> Status: `imported-reference`

- Source scope: Curated `paladin_macros.md` export from another session
- Source locale: Simplified Chinese (`zhCN`)
- Game version: WoW TBC Classic / TBC Anniversary
- Imported: 2026-08-18
- Contents: Retribution, Protection, Holy, universal utility, blessing, item, engineering, keybind, and WeakAura notes
- Verification: Not independently tested
- Full source: See the [Simplified Chinese source page](README_zhCN.md).

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
