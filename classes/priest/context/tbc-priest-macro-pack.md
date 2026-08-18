# TBC Priest cross-session reference

> **Status:** Imported reference only — not a verified or fully localized macro release.

- Source scope: Curated TBC Priest macro pack supplied from another session
- Game version: WoW TBC Classic; specific client build was not supplied
- Class and roles: Shadow Priest PvE, dungeon, and raid; Holy/Discipline healing offspec; Discipline PvP arena
- Source macro locale: English (`enUS`)
- Localization aid: Partial Simplified Chinese (`zhCN`) spell-name glossary
- Imported: 2026-08-18
- Contents: 68 Lua macro blocks plus action-bar, targeting, rotation, mana, and dungeon notes
- Verification: Source-session claims preserved; macro behavior and localized tokens have not been independently revalidated
- Locale completeness: Complete source pack is not yet available as matching `enUS`, `zhCN`, and `zhTW` release files

Before promoting an entry into `../macros/`, test it against the intended TBC client/build, confirm features such as `@cursor` where noted, verify localized ability and item names, and create the locale set required by [LOCALIZATION.md](../../../LOCALIZATION.md). The imported body is preserved after heading nesting and trailing-whitespace normalization.

## TBC Priest Macro Pack
**Scope:** Shadow Priest PvE / dungeon / raid, Holy-Disc healing offspec, Disc PvP arena
**Client note:** These macros use **English spell names**. On a Chinese client, replace spell names by **Shift-clicking the spell from your spellbook into the macro**. Slot macros like `/use 13` and `/use 14` are language-independent.

### General Rules

- Most macros use priority: **mouseover → current target → self fallback**.
- For Shadow Priest, do **not** macro a full rotation. TBC macros cannot make smart combat decisions.
- Use WeakAuras / ClassTimer / Quartz / Plater to track **VT / SW:P / VE** timers.
- Top trinket slot = `/use 13`
- Bottom trinket slot = `/use 14`

---

## 1. Shadow Priest PvE / Dungeon Macros

### Safe Shadowform Toggle

Prevents accidentally cancelling Shadowform by pressing the button again.

```lua
#showtooltip Shadowform
/cast !Shadowform
```

---

### Vampiric Touch — Mouseover / Target

Good for boss and multi-dot dungeon pulls.

```lua
#showtooltip Vampiric Touch
/cast [@mouseover,harm,nodead][harm,nodead] Vampiric Touch
```

---

### Shadow Word: Pain — Mouseover / Target

Main multi-dot button.

```lua
#showtooltip Shadow Word: Pain
/cast [@mouseover,harm,nodead][harm,nodead] Shadow Word: Pain
```

---

### Vampiric Embrace — Mouseover / Target

Use mostly on bosses, elites, or long-lived targets.

```lua
#showtooltip Vampiric Embrace
/cast [@mouseover,harm,nodead][harm,nodead] Vampiric Embrace
```

---

### Mind Blast — Mouseover / Target

```lua
#showtooltip Mind Blast
/cast [@mouseover,harm,nodead][harm,nodead] Mind Blast
```

---

### Mind Flay — No-Clip Macro

Prevents accidentally clipping your own Mind Flay by button-spamming.

```lua
#showtooltip Mind Flay
/cast [nochanneling:Mind Flay,@mouseover,harm,nodead][nochanneling:Mind Flay,harm,nodead] Mind Flay
```

---

### Shadow Word: Death — Mouseover / Target

Use carefully. Do not kill yourself with backlash.

```lua
#showtooltip Shadow Word: Death
/cast [@mouseover,harm,nodead][harm,nodead] Shadow Word: Death
```

---

### Shadow Word: Death — Stopcasting Version

Useful for PvP or finishing a target quickly.

```lua
#showtooltip Shadow Word: Death
/stopcasting
/cast [@mouseover,harm,nodead][harm,nodead] Shadow Word: Death
```

---

### Inner Focus + Mind Blast

Useful when mana is tight or for a stronger burst Mind Blast.

```lua
#showtooltip Mind Blast
/cast Inner Focus
/cast [@mouseover,harm,nodead][harm,nodead] Mind Blast
```

---

### Shadowfiend — Mouseover / Target

```lua
#showtooltip Shadowfiend
/cast [@mouseover,harm,nodead][harm,nodead] Shadowfiend
/petattack
```

---

### Trinket + Mind Blast

Uses top trinket slot.

```lua
#showtooltip Mind Blast
/use 13
/cast [@mouseover,harm,nodead][harm,nodead] Mind Blast
```

Bottom trinket version:

```lua
#showtooltip Mind Blast
/use 14
/cast [@mouseover,harm,nodead][harm,nodead] Mind Blast
```

---

### Fade

```lua
#showtooltip Fade
/cast Fade
```

---

### Emergency Flash Heal Out of Shadowform

For Shadow spec emergency healing.

```lua
#showtooltip Flash Heal
/cancelaura Shadowform
/cast [@mouseover,help,nodead][help,nodead][@player] Flash Heal
```

---

### Emergency Prayer of Mending Out of Shadowform

```lua
#showtooltip Prayer of Mending
/cancelaura Shadowform
/cast [@mouseover,help,nodead][help,nodead][@player] Prayer of Mending
```

---

### Emergency Renew Out of Shadowform

```lua
#showtooltip Renew
/cancelaura Shadowform
/cast [@mouseover,help,nodead][help,nodead][@player] Renew
```

---

## 2. Holy / Discipline Healing Macros

### Power Word: Shield — Mouseover / Target / Self

```lua
#showtooltip Power Word: Shield
/cast [@mouseover,help,nodead][help,nodead][@player] Power Word: Shield
```

---

### Flash Heal — Mouseover / Target / Self

```lua
#showtooltip Flash Heal
/cast [@mouseover,help,nodead][help,nodead][@player] Flash Heal
```

---

### Greater Heal — Mouseover / Target / Self

```lua
#showtooltip Greater Heal
/cast [@mouseover,help,nodead][help,nodead][@player] Greater Heal
```

---

### Renew — Mouseover / Target / Self

```lua
#showtooltip Renew
/cast [@mouseover,help,nodead][help,nodead][@player] Renew
```

---

### Prayer of Mending — Mouseover / Target / Self

```lua
#showtooltip Prayer of Mending
/cast [@mouseover,help,nodead][help,nodead][@player] Prayer of Mending
```

---

### Binding Heal — Mouseover / Target / Self

```lua
#showtooltip Binding Heal
/cast [@mouseover,help,nodead][help,nodead][@player] Binding Heal
```

---

### Circle of Healing — Mouseover / Target / Self

Only works if you are Holy with Circle of Healing.

```lua
#showtooltip Circle of Healing
/cast [@mouseover,help,nodead][help,nodead][@player] Circle of Healing
```

---

### Prayer of Healing

```lua
#showtooltip Prayer of Healing
/cast Prayer of Healing
```

---

### Inner Focus + Greater Heal

Use for big free single-target heal.

```lua
#showtooltip Greater Heal
/cast Inner Focus
/cast [@mouseover,help,nodead][help,nodead][@player] Greater Heal
```

---

### Inner Focus + Circle of Healing

Use for free AoE healing if several people are injured.

```lua
#showtooltip Circle of Healing
/cast Inner Focus
/cast [@mouseover,help,nodead][help,nodead][@player] Circle of Healing
```

---

### Pain Suppression — Mouseover / Target / Self

```lua
#showtooltip Pain Suppression
/stopcasting
/cast [@mouseover,help,nodead][help,nodead][@player] Pain Suppression
```

---

### Power Infusion — Mouseover / Target / Self

```lua
#showtooltip Power Infusion
/cast [@mouseover,help,nodead][help,nodead][@player] Power Infusion
```

---

### Fear Ward — Mouseover / Target / Self

```lua
#showtooltip Fear Ward
/cast [@mouseover,help,nodead][help,nodead][@player] Fear Ward
```

---

### Abolish Disease — Mouseover / Target / Self

```lua
#showtooltip Abolish Disease
/cast [@mouseover,help,nodead][help,nodead][@player] Abolish Disease
```

---

### Friendly Dispel Only

Use this when you do not want to accidentally offensively dispel an enemy.

```lua
#showtooltip Dispel Magic
/cast [@mouseover,help,nodead][help,nodead][@player] Dispel Magic
```

---

### Enemy Dispel Only

Use this to purge enemy buffs.

```lua
#showtooltip Dispel Magic
/cast [@mouseover,harm,nodead][harm,nodead] Dispel Magic
```

---

### All-Purpose Dispel

Mouseover friendly/enemy first, then current target, then self.

```lua
#showtooltip Dispel Magic
/cast [@mouseover,help,nodead][@mouseover,harm,nodead][help,nodead][harm,nodead][@player] Dispel Magic
```

---

### Mass Dispel — Cursor Version

Use if your TBC client supports `@cursor`.

```lua
#showtooltip Mass Dispel
/cast [@cursor] Mass Dispel
```

Manual targeting version:

```lua
#showtooltip Mass Dispel
/cast Mass Dispel
```

---

### Resurrection — Mouseover / Target

```lua
#showtooltip Resurrection
/cast [@mouseover,help,dead][help,dead] Resurrection
```

---

## 3. PvP / Arena Macros

### Set Focus — Mouseover / Target

```lua
/focus [@mouseover,harm,nodead][harm,nodead]
```

---

### Clear Focus

```lua
/clearfocus
```

---

### Mana Burn — Mouseover / Target

This is the one you asked for directly.

```lua
#showtooltip Mana Burn
/cast [@mouseover,harm,nodead][harm,nodead] Mana Burn
```

---

### Mana Burn — Stopcasting Mouseover / Target

Better for arena when you want instant reaction.

```lua
#showtooltip Mana Burn
/stopcasting
/cast [@mouseover,harm,nodead][harm,nodead] Mana Burn
```

---

### Mana Burn — Focus

```lua
#showtooltip Mana Burn
/stopcasting
/cast [@focus,harm,nodead][harm,nodead] Mana Burn
```

---

### Mana Burn — Arena 1

```lua
#showtooltip Mana Burn
/stopcasting
/cast [@arena1] Mana Burn
```

---

### Mana Burn — Arena 2

```lua
#showtooltip Mana Burn
/stopcasting
/cast [@arena2] Mana Burn
```

---

### Mana Burn — Arena 3

```lua
#showtooltip Mana Burn
/stopcasting
/cast [@arena3] Mana Burn
```

---

### Focus Enemy Dispel

```lua
#showtooltip Dispel Magic
/cast [@focus,harm,nodead][harm,nodead] Dispel Magic
```

---

### Arena 1 Dispel

```lua
#showtooltip Dispel Magic
/cast [@arena1] Dispel Magic
```

---

### Arena 2 Dispel

```lua
#showtooltip Dispel Magic
/cast [@arena2] Dispel Magic
```

---

### Arena 3 Dispel

```lua
#showtooltip Dispel Magic
/cast [@arena3] Dispel Magic
```

---

### Psychic Scream — Stopcasting

```lua
#showtooltip Psychic Scream
/stopcasting
/cast Psychic Scream
```

---

### Shadow Word: Death — Focus Anti-CC

Use to break incoming Polymorph/Blind-style CC by timing the backlash.

```lua
#showtooltip Shadow Word: Death
/stopcasting
/cast [@focus,harm,nodead][harm,nodead] Shadow Word: Death
```

---

### Mind Control — Focus / Mouseover / Target

```lua
#showtooltip Mind Control
/cast [@focus,harm,nodead][@mouseover,harm,nodead][harm,nodead] Mind Control
```

---

### Shackle Undead — Mouseover / Target

Useful in dungeons and certain PvP situations.

```lua
#showtooltip Shackle Undead
/cast [@mouseover,harm,nodead][harm,nodead] Shackle Undead
```

---

### Mind Soothe — Mouseover / Target

Useful for skips in dungeons.

```lua
#showtooltip Mind Soothe
/cast [@mouseover,harm,nodead][harm,nodead] Mind Soothe
```

---

## 4. Direct Party Arena Macros

These are optional but strong for arena because they avoid mouseover mistakes.

### Shield Self

```lua
#showtooltip Power Word: Shield
/cast [@player] Power Word: Shield
```

---

### Shield Party 1

```lua
#showtooltip Power Word: Shield
/cast [@party1] Power Word: Shield
```

---

### Shield Party 2

```lua
#showtooltip Power Word: Shield
/cast [@party2] Power Word: Shield
```

---

### Dispel Self

```lua
#showtooltip Dispel Magic
/cast [@player] Dispel Magic
```

---

### Dispel Party 1

```lua
#showtooltip Dispel Magic
/cast [@party1] Dispel Magic
```

---

### Dispel Party 2

```lua
#showtooltip Dispel Magic
/cast [@party2] Dispel Magic
```

---

### Pain Suppression Self

```lua
#showtooltip Pain Suppression
/stopcasting
/cast [@player] Pain Suppression
```

---

### Pain Suppression Party 1

```lua
#showtooltip Pain Suppression
/stopcasting
/cast [@party1] Pain Suppression
```

---

### Pain Suppression Party 2

```lua
#showtooltip Pain Suppression
/stopcasting
/cast [@party2] Pain Suppression
```

---

### Fear Ward Self

```lua
#showtooltip Fear Ward
/cast [@player] Fear Ward
```

---

### Fear Ward Party 1

```lua
#showtooltip Fear Ward
/cast [@party1] Fear Ward
```

---

### Fear Ward Party 2

```lua
#showtooltip Fear Ward
/cast [@party2] Fear Ward
```

---

## 5. Consumable / Mana Macros

### Super Mana Potion

Replace the item name if your client is not English.

```lua
#showtooltip Super Mana Potion
/use Super Mana Potion
```

---

### Demonic Rune

```lua
#showtooltip Demonic Rune
/use Demonic Rune
```

---

### Dark Rune

```lua
#showtooltip Dark Rune
/use Dark Rune
```

---

## 6. Suggested Action Bar / Keybind Layout

### Shadow PvE / Dungeon

| Key | Spell / Macro |
|---|---|
| 1 | Vampiric Touch |
| 2 | Shadow Word: Pain |
| 3 | Mind Blast |
| 4 | Mind Flay no-clip |
| 5 | Shadow Word: Death |
| Q | Vampiric Embrace |
| E | Shadowfiend |
| R | Trinket + Mind Blast |
| F | Fade |
| C | Dispel Magic |
| V | Shackle Undead / Mind Soothe |
| Shift+1 | Emergency Flash Heal out of Shadowform |
| Shift+2 | Emergency Prayer of Mending out of Shadowform |
| Shift+3 | Emergency Renew out of Shadowform |

### Disc / Holy Healing

| Key | Spell / Macro |
|---|---|
| 1 | Power Word: Shield |
| 2 | Flash Heal |
| 3 | Dispel Magic |
| 4 | Prayer of Mending |
| 5 | Renew |
| Q | Psychic Scream |
| E | Mana Burn |
| R | Pain Suppression |
| F | Power Infusion |
| C | Mass Dispel |
| V | Shadowfiend |
| Shift+1 | Binding Heal |
| Shift+2 | Greater Heal |
| Shift+3 | Abolish Disease |
| Shift+4 | Inner Focus + Greater Heal |
| Shift+5 | Drink / Mana Potion |

### Arena Targeting

| Key | Target |
|---|---|
| Mousewheel Up | Party 1 |
| Mousewheel Down | Party 2 |
| Mouse Button 3 | Self |
| F1 | Arena Enemy 1 |
| F2 | Arena Enemy 2 |
| F3 | Arena Enemy 3 |
| T | Set Focus |
| G | Target Focus |

---

## 7. Important Chinese Client Spell Name Note

For Chinese client, do not manually type spell names unless confirmed. Best method:

1. Open macro window.
2. Put cursor after `/cast`.
3. Open spellbook.
4. **Shift-click the spell**.
5. WoW inserts the correct localized spell name.

Common Chinese spell names you will probably need:

| English | Chinese |
|---|---|
| Power Word: Shield | 真言术：盾 |
| Flash Heal | 快速治疗 |
| Greater Heal | 强效治疗术 |
| Renew | 恢复 |
| Prayer of Mending | 愈合祷言 |
| Binding Heal | 联结治疗 |
| Prayer of Healing | 治疗祷言 |
| Circle of Healing | 治疗之环 |
| Dispel Magic | 驱散魔法 |
| Mass Dispel | 群体驱散 |
| Mana Burn | 法力燃烧 |
| Psychic Scream | 心灵尖啸 |
| Pain Suppression | 痛苦压制 |
| Power Infusion | 能量灌注 |
| Inner Focus | 心灵专注 |
| Shadowform | 暗影形态 |
| Shadow Word: Pain | 暗言术：痛 |
| Shadow Word: Death | 暗言术：灭 |
| Vampiric Touch | 吸血鬼之触 |
| Vampiric Embrace | 吸血鬼的拥抱 |
| Mind Blast | 心灵震爆 |
| Mind Flay | 精神鞭笞 |
| Shadowfiend | 暗影魔 |
| Fear Ward | 防护恐惧结界 |
| Shackle Undead | 束缚亡灵 |
| Mind Soothe | 安抚心灵 |
| Mind Control | 精神控制 |
| Fade | 渐隐术 |
| Resurrection | 复活 |

---

## 8. Shadow Rotation Reminder

### Boss / Raid

```text
Vampiric Embrace if long fight
Vampiric Touch
Shadow Word: Pain
Mind Blast on cooldown
Shadow Word: Death only if safe and mana is okay
Mind Flay filler
```

### P2 Mana-Safe Raid Mode

```text
Keep Vampiric Touch up
Keep Shadow Word: Pain up
Use Mind Flay as main filler
Use Mind Blast only if mana allows
Skip Shadow Word: Death if mana is tight
Use Shadowfiend early
Use Mana Potion early
Use Dark Rune / Demonic Rune
```

### Dungeon 2–4 Mob Pulls

```text
2 mobs:
VT + SW:P on skull
SW:P on second mob
Mind Blast / Mind Flay skull

3 mobs:
VT + SW:P on skull
SW:P on second mob
SW:P third only if it will live long enough
Mind Blast / Mind Flay skull

4 mobs:
Do not greed full DoTs on everything
VT + SW:P skull
SW:P 1–2 extra mobs only if pull lives long enough
Focus skull
```
