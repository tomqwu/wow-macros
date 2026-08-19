# Warlock macros

[简体中文](README_zhCN.md)

## Player profile

| Field | Value |
| --- | --- |
| Game version | WoW TBC Classic, Phase 2 raid context; exact client build not supplied |
| Class | Warlock |
| Level | Not supplied |
| Talent build | Primarily Shadow Destruction with occasional Fire Destruction; exact point allocation not supplied |
| Key talents | The source includes Shadowburn, Conflagrate, Demonic Sacrifice, and alternative-build or utility actions |
| Role / content | Raid DPS, curses, threat, AoE, focus control, pet management, summons, consumables, and utility |
| Rotation source | The imported `zhCN` pack covers Shadow and Fire Destruction priorities, AoE, threat rules, and keybinds |
| Client locale | English (`enUS`) |
| Last updated | 2026-08-19 |
| Overall status | 59 source macro blocks remain `imported-reference` on the Chinese page; no paired macro set yet |

## Rotation and talent model

### Player rotation

- Opener: The source includes curse and damage setup for Shadow and Fire raid variants; the active variant is not selected.
- Sustained priority: Shadow Bolt or Incinerate paths, Immolate and Conflagrate for Fire, curse assignments, AoE, and threat rules are documented.
- Cooldowns / emergencies: Trinkets, Destruction Potion, Soulshatter, health consumables, pet sacrifice, crowd control, and summons appear in the source.

### Macro opportunities

- Generate a compact set after selecting the Shadow or Fire build, assigned curse, active pet, encounter role, and target preferences.
- Derive pet-control, focus-control, curse, DPS, threat, consumable, and summon macros from those choices.

### Deliberately not macroed

- Damage priority, DoT refreshes, curse-assignment changes, threat decisions, and pet choice remain manual.
- Shadow, Fire, and pet-specific actions are not promoted as one player loadout without the active build and pet plan.

## Macro set

No paired macros yet. Select the active Destruction variant and pet plan, then create and test matching locale variants.

## Imported reference backlog

> Status: `imported-reference`

- Source scope: Full TBC Warlock source pack on the [Simplified Chinese page](README_zhCN.md)
- Source locale: Simplified Chinese (`zhCN`)
- Game version: WoW TBC Classic, Phase 2 raid context; exact client build not supplied
- Imported: 2026-08-18
- Verification: Not independently tested
- Contents: 59 Lua macro blocks plus spell mapping, keybind, rotation, threat, and TBC compatibility notes

The complete source-language backlog is retained on the Chinese page. It is not duplicated here because no matching `enUS` variants have been reviewed or tested.

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
