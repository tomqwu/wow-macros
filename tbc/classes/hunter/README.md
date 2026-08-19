# Hunter macros

[简体中文](README_zhCN.md)

## Player profile

| Field | Value |
| --- | --- |
| Game version | WoW TBC Classic / Anniversary-style TBC; exact client build not supplied |
| Class | Hunter |
| Level | 70 |
| Talent build | No single allocation supplied; the source spans Beast Mastery, Marksmanship, and Survival-only abilities |
| Key talents | The source mentions Bestial Wrath, Intimidation, Silencing Shot, and Wyvern Sting across alternative builds |
| Role / content | PvE rotation, raids, Misdirection, pet control, traps, Tempest Keep skips, and PvP focus control |
| Rotation source | The imported `zhCN` pack covers Steady Shot timing, Auto Shot, Kill Command, cooldowns, and keybind notes |
| Client locale | English (`enUS`) |
| Last updated | 2026-08-19 |
| Overall status | The `zhCN` source remains `imported-reference`; no paired macro set yet |

## Rotation and talent model

### Player rotation

- Opener: Hunter's Mark and pet attack are supplied as opener utility; an encounter-specific opener has not been normalized.
- Sustained priority: The source discusses timing Steady Shot around Auto Shot and using Kill Command, but no single talent-specific priority is confirmed.
- Cooldowns / emergencies: The source includes Bestial Wrath with trinkets, Feign Death, traps, pet recall, and Misdirection.

### Macro opportunities

- Derive shot, Misdirection, pet-control, trap, aspect, and focus macros after selecting one actual talent build and rotation.
- Preserve the supplied Ravager and Wind Serpent context when generating pet-specific controls.

### Deliberately not macroed

- Auto Shot weaving and the full damage priority remain manual because a macro cannot intelligently select their timing.
- Talent-only abilities are not promoted until the player's active build is identified.

## Macro set

No paired macros yet. The source pack must be reduced to the player's actual build, localized for `enUS`, and tested in both clients.

## Imported reference backlog

> Status: `imported-reference`

- Source scope: Curated TBC Hunter macro pack and Phase 2 pet handoff from another session
- Source locale: Simplified Chinese (`zhCN`)
- Game version: WoW TBC Classic / Anniversary-style TBC
- Imported: 2026-08-18
- Contents: 44 named macro blocks plus action-bar, limitations, pet training, resistance, and raid-role notes
- Verification: Not independently tested
- Full source: See the [Simplified Chinese source page](README_zhCN.md).

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
