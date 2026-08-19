# Warlock macros

## Player profile

| Field | Value |
| --- | --- |
| Game version | WoW TBC Classic, Phase 2 raid context; exact client build not supplied |
| Class | Warlock |
| Level | Not supplied |
| Talent build | Primarily Shadow Destruction with occasional Fire Destruction; exact point allocation not supplied |
| Key talents | Source includes Shadowburn, Conflagrate, Demonic Sacrifice, and other alternative-build or utility actions |
| Role / content | Raid DPS, curses, threat, AoE, focus control, pet management, summons, consumables, and utility |
| Rotation source | Imported `zhCN` pack includes Shadow and Fire Destruction raid priorities, AoE, threat rules, and keybinds |
| Client locales | English (`enUS`), Simplified Chinese (`zhCN`) |
| Last updated | 2026-08-18 |
| Overall status | 59 `zhCN` macro blocks remain `imported-reference`; no paired macro set yet |

## Rotation and talent model

### Player rotation

- Opener: The source supplies curse and damage setup for Shadow and Fire raid variants; the active variant is not selected.
- Sustained priority: Shadow Bolt or Incinerate paths, Immolate/Conflagrate for Fire, curse assignments, AoE, and threat rules are documented.
- Cooldowns / emergencies: Trinkets, Destruction Potion, Soulshatter, health consumables, pet sacrifice, crowd control, and summons appear in the source.

### Macro opportunities

- Generate a compact set for the selected Shadow or Fire build, assigned curse, active pet, encounter role, and target preferences.
- Derive pet-control, focus control, curse, DPS, threat, consumable, and summon macros from those choices.

### Deliberately not macroed

- Damage priority, DoT refreshes, curse assignment changes, threat decisions, and pet choice remain manual.
- Alternative Shadow/Fire and pet-specific actions are not promoted as one player loadout without the active build and pet plan.

## Macro set

No paired macros yet. Select the active Destruction variant and pet plan, then add and test matching `enUS` variants.

## Imported reference backlog

> **Status:** Imported reference only — not a verified or fully localized macro release.

- Source scope: Curated TBC Warlock macro pack supplied from another session
- Game version: WoW TBC Classic, Phase 2 raid context
- Class and builds: Destruction Warlock, primarily Shadow Destruction with occasional Fire Destruction
- Use cases: Raid DPS, curses, threat, AoE, focus control, pet management, summons, consumables, and utility
- Source client locale: Simplified Chinese (`zhCN`)
- Imported: 2026-08-18
- Contents: 59 Lua macro blocks plus spell mapping, keybind, rotation, threat, and TBC compatibility notes
- Verification: Source-session claims preserved; macro behavior, localized pet conditions, ranks, and item names have not been independently revalidated
- Locale completeness: `zhCN` source only; matching `enUS` release files have not been produced
- Privacy: The source character-name line was intentionally omitted

Before marking an entry verified, test it against the intended TBC client/build, verify localized spell, item, and pet-condition names, split macros that exceed the TBC character limit, and add the matching variant required by [LOCALIZATION.md](../../../LOCALIZATION.md). The imported body is preserved after removing its outer copy fence and character identifier, nesting headings, and normalizing trailing whitespace.

## TBC Warlock Macro Pack — Chinese Client

### Context

Class: Warlock / 术士
Expansion: TBC Classic
Client language: Chinese
Main usage: Phase 2 raid Destruction Warlock, mostly Shadow Destro, sometimes Fire Destro.
Important requirements:

- Use Chinese spell names.
- Prefer mouseover when useful.
- Include focus versions for PvP / utility.
- Include pet macros for Felhunter / Succubus / Voidwalker / Imp.
- Include raid DPS macros for curses, Shadow Bolt, Incinerate, Soulshatter, Life Tap, Seed.
- Include consumable and trinket macros.
- Keep macros TBC-compatible when possible.
- If `[pet:地狱猎犬]` / `[pet:魅魔]` does not work on the Chinese client, use the fallback English pet-condition version with Chinese spell names.

---

## 1. Important Spell Name Mapping

| English | Chinese |
|---|---|
| Shadow Bolt | 暗影箭 |
| Incinerate | 烧尽 |
| Immolate | 献祭 |
| Conflagrate | 燃烧 |
| Curse of Elements | 元素诅咒 |
| Curse of Recklessness | 鲁莽诅咒 |
| Curse of Doom | 厄运诅咒 |
| Curse of Agony | 痛苦诅咒 |
| Curse of Tongues | 语言诅咒 |
| Curse of Exhaustion | 疲劳诅咒 |
| Seed of Corruption | 腐蚀之种 |
| Rain of Fire | 火焰之雨 |
| Life Tap | 生命分流 |
| Dark Pact | 黑暗契约 |
| Soulshatter | 灵魂碎裂 |
| Shadowburn | 暗影灼烧 |
| Death Coil | 死亡缠绕 |
| Fear | 恐惧术 |
| Howl of Terror | 恐惧嚎叫 |
| Banish | 放逐术 |
| Enslave Demon | 奴役恶魔 |
| Drain Soul | 吸取灵魂 |
| Drain Life | 吸取生命 |
| Drain Mana | 吸取法力 |
| Fel Armor | 邪甲术 |
| Shadow Ward | 暗影防护结界 |
| Demonic Sacrifice | 恶魔牺牲 |
| Fel Domination | 恶魔支配 |
| Felhunter | 地狱猎犬 |
| Spell Lock | 法术封锁 |
| Succubus | 魅魔 |
| Seduction | 诱惑 |
| Voidwalker | 虚空行者 |
| Sacrifice | 牺牲 |
| Imp | 小鬼 |
| Fire Shield | 火焰之盾 |
| Summon Felhunter | 召唤地狱猎犬 |
| Summon Succubus | 召唤魅魔 |
| Summon Voidwalker | 召唤虚空行者 |
| Summon Imp | 召唤小鬼 |
| Ritual of Souls | 灵魂仪式 |
| Ritual of Summoning | 召唤仪式 |
| Create Healthstone | 制造治疗石 |
| Create Soulstone | 制造灵魂石 |
| Destruction Potion | 毁灭药水 |
| Super Mana Potion | 超级法力药水 |
| Super Healing Potion | 超级治疗药水 |

---

## 2. Core Pet Control Macros

### Felhunter Spell Lock / Succubus Seduction — Mouseover First

Chinese pet-condition version:

```lua
#showtooltip
/cast [pet:地狱猎犬,@mouseover,harm,nodead][pet:地狱猎犬,harm,nodead]法术封锁;[pet:魅魔,@mouseover,harm,nodead][pet:魅魔,harm,nodead]诱惑
```

Fallback version if Chinese pet condition fails:

```lua
#showtooltip
/cast [pet:felhunter,@mouseover,harm,nodead][pet:felhunter,harm,nodead]法术封锁;[pet:succubus,@mouseover,harm,nodead][pet:succubus,harm,nodead]诱惑
```

---

### Felhunter Spell Lock — Focus / Mouseover / Target

```lua
#showtooltip 法术封锁
/cast [@focus,harm,nodead,pet:felhunter][@mouseover,harm,nodead,pet:felhunter][harm,nodead,pet:felhunter]法术封锁
```

---

### Succubus Seduction — Focus / Mouseover / Target

```lua
#showtooltip 诱惑
/cast [@focus,harm,nodead,pet:succubus][@mouseover,harm,nodead,pet:succubus][harm,nodead,pet:succubus]诱惑
```

---

### Smart Pet Utility Macro

Function:

- Voidwalker: Sacrifice
- Imp: Fire Shield mouseover friendly, target friendly, otherwise self
- Succubus: Seduce mouseover enemy, otherwise target

Chinese pet-condition version:

```lua
#showtooltip
/cast [pet:虚空行者]牺牲;[pet:小鬼,@mouseover,help,nodead][pet:小鬼,help,nodead][pet:小鬼,@player]火焰之盾;[pet:魅魔,@mouseover,harm,nodead][pet:魅魔,harm,nodead]诱惑
```

Fallback version:

```lua
#showtooltip
/cast [pet:voidwalker]牺牲;[pet:imp,@mouseover,help,nodead][pet:imp,help,nodead][pet:imp,@player]火焰之盾;[pet:succubus,@mouseover,harm,nodead][pet:succubus,harm,nodead]诱惑
```

---

### Voidwalker Sacrifice Only

```lua
#showtooltip 牺牲
/cast [pet:虚空行者]牺牲
```

Fallback:

```lua
#showtooltip 牺牲
/cast [pet:voidwalker]牺牲
```

---

### Imp Fire Shield — Mouseover / Target / Self

```lua
#showtooltip 火焰之盾
/cast [@mouseover,help,nodead][help,nodead][@player]火焰之盾
```

---

### Pet Attack / Pet Follow

Alt = pet follow
No modifier = pet attack mouseover or target

```lua
#showtooltip
/petfollow [mod:alt]
/petattack [nomod,@mouseover,harm,nodead][nomod,harm,nodead]
```

---

### Pet Passive / Defensive / Aggressive

```lua
#showtooltip
/petpassive [mod:alt]
/petdefensive [nomod]
```

Use Alt if pet is about to break CC or run into danger.

---

## 3. Focus Macros

### Set Focus / Clear Focus

Alt = clear focus
No modifier = set mouseover or target as focus

```lua
#showtooltip
/clearfocus [mod:alt]
/focus [nomod,@mouseover,harm,nodead][nomod,harm,nodead]
```

---

### Fear — Focus with Shift, Otherwise Mouseover / Target

```lua
#showtooltip 恐惧术
/cast [mod:shift,@focus,harm,nodead][@mouseover,harm,nodead][harm,nodead]恐惧术
```

---

### Banish — Focus with Shift, Otherwise Mouseover / Target

```lua
#showtooltip 放逐术
/cast [mod:shift,@focus,harm,nodead][@mouseover,harm,nodead][harm,nodead]放逐术
```

---

### Enslave Demon — Mouseover / Target

```lua
#showtooltip 奴役恶魔
/cast [@mouseover,harm,nodead][harm,nodead]奴役恶魔
```

---

## 4. Raid DPS Macros

### Shadow Bolt — Mouseover / Target

```lua
#showtooltip 暗影箭
/cast [@mouseover,harm,nodead][harm,nodead]暗影箭
```

---

### Incinerate — Mouseover / Target

```lua
#showtooltip 烧尽
/cast [@mouseover,harm,nodead][harm,nodead]烧尽
```

---

### Immolate — Mouseover / Target

```lua
#showtooltip 献祭
/cast [@mouseover,harm,nodead][harm,nodead]献祭
```

---

### Conflagrate — Mouseover / Target

```lua
#showtooltip 燃烧
/cast [@mouseover,harm,nodead][harm,nodead]燃烧
```

Note: Do not use Conflagrate as normal raid rotation unless Fire Destro movement / specific situation. It consumes Immolate.

---

### Shadowburn — Mouseover / Target

```lua
#showtooltip 暗影灼烧
/cast [@mouseover,harm,nodead][harm,nodead]暗影灼烧
```

---

### Death Coil — Mouseover / Target

```lua
#showtooltip 死亡缠绕
/cast [@mouseover,harm,nodead][harm,nodead]死亡缠绕
```

---

## 5. Curse Macros

### Curse of Elements

```lua
#showtooltip 元素诅咒
/cast [@mouseover,harm,nodead][harm,nodead]元素诅咒
```

---

### Curse of Recklessness

```lua
#showtooltip 鲁莽诅咒
/cast [@mouseover,harm,nodead][harm,nodead]鲁莽诅咒
```

---

### Curse of Doom

```lua
#showtooltip 厄运诅咒
/cast [@mouseover,harm,nodead][harm,nodead]厄运诅咒
```

---

### Curse of Agony

```lua
#showtooltip 痛苦诅咒
/cast [@mouseover,harm,nodead][harm,nodead]痛苦诅咒
```

---

### Curse of Tongues

```lua
#showtooltip 语言诅咒
/cast [@mouseover,harm,nodead][harm,nodead]语言诅咒
```

---

### Curse of Exhaustion

```lua
#showtooltip 疲劳诅咒
/cast [@mouseover,harm,nodead][harm,nodead]疲劳诅咒
```

---

### Compact Curse Modifier Macro

Default = Curse of Doom
Shift = Curse of Elements
Ctrl = Curse of Recklessness
Alt = Curse of Agony

```lua
#showtooltip
/cast [mod:shift]元素诅咒;[mod:ctrl]鲁莽诅咒;[mod:alt]痛苦诅咒;厄运诅咒
```

---

## 6. AoE Macros

### Seed of Corruption — Mouseover / Target

```lua
#showtooltip 腐蚀之种
/cast [@mouseover,harm,nodead][harm,nodead]腐蚀之种
```

Important raid usage:

- Do not Seed instantly on pull.
- Wait 2-4 seconds for tank threat.
- Especially wait if tank is Warrior or Bear.
- Paladin tank is safer, but still do not open instantly.

---

### Rain of Fire

```lua
#showtooltip 火焰之雨
/cast 火焰之雨
```

---

### Howl of Terror

```lua
#showtooltip 恐惧嚎叫
/cast 恐惧嚎叫
```

---

## 7. Threat / Survival Macros

### Soulshatter Emergency

```lua
#showtooltip 灵魂碎裂
/stopcasting
/cast 灵魂碎裂
```

Usage rule:

- Use around 75%-85% of tank threat.
- Do not wait until already OT.
- Treat Soulshatter as permission to keep DPSing, not only as panic button.

---

### Life Tap

```lua
#showtooltip 生命分流
/cast 生命分流
```

---

### Low Rank Life Tap Option

Use Shift for Rank 1 Life Tap, normal press for max rank.

```lua
#showtooltip 生命分流
/cast [mod:shift]生命分流(等级 1);生命分流
```

If rank syntax does not work on the client, use the simple Life Tap macro above.

---

### Dark Pact

```lua
#showtooltip 黑暗契约
/cast 黑暗契约
```

---

### Drain Life — Mouseover / Target

```lua
#showtooltip 吸取生命
/cast [@mouseover,harm,nodead][harm,nodead]吸取生命
```

---

### Drain Mana — Mouseover / Target

```lua
#showtooltip 吸取法力
/cast [@mouseover,harm,nodead][harm,nodead]吸取法力
```

---

### Drain Soul — Mouseover / Target

```lua
#showtooltip 吸取灵魂
/cast [@mouseover,harm,nodead][harm,nodead]吸取灵魂
```

---

### Use Healthstone

```lua
#showtooltip 治疗石
/use 极效治疗石
/use 特效治疗石
/use 治疗石
```

---

### Use Health Potion

```lua
#showtooltip 超级治疗药水
/use 超级治疗药水
```

---

### Shadow Ward

```lua
#showtooltip 暗影防护结界
/cast 暗影防护结界
```

---

## 8. Raid Burst / Consumable Macros

### Trinkets Only

```lua
#showtooltip
/use 13
/use 14
```

---

### Destruction Potion Only

```lua
#showtooltip 毁灭药水
/use 毁灭药水
```

---

### Shadow Destro Burst

Uses trinkets + Destruction Potion, then casts Shadow Bolt.

```lua
#showtooltip 暗影箭
/use 13
/use 14
/use 毁灭药水
/cast 暗影箭
```

Usage warning:

- Do not spam this if saving potion.
- Use after tank has threat.
- Ideally use after Soulshatter if threat is high.
- Best during Bloodlust / Heroism window.

---

### Fire Destro Burst

Uses trinkets + Destruction Potion, then casts Incinerate.

```lua
#showtooltip 烧尽
/use 13
/use 14
/use 毁灭药水
/cast 烧尽
```

---

### Mana Potion

```lua
#showtooltip 超级法力药水
/use 超级法力药水
```

---

## 9. Buff / Utility Macros

### Fel Armor

```lua
#showtooltip 邪甲术
/cast 邪甲术
```

---

### Detect Invisibility — Mouseover / Target / Self

```lua
#showtooltip 侦测隐形
/cast [@mouseover,help,nodead][help,nodead][@player]侦测隐形
```

---

### Create Healthstone

```lua
#showtooltip 制造治疗石
/cast 制造治疗石
```

---

### Create Soulstone

```lua
#showtooltip 制造灵魂石
/cast 制造灵魂石
```

---

### Use Soulstone on Mouseover / Target / Self

Try higher-rank soulstone names first.

```lua
#showtooltip 灵魂石
/use [@mouseover,help,nodead][help,nodead][@player]极效灵魂石
/use [@mouseover,help,nodead][help,nodead][@player]特效灵魂石
/use [@mouseover,help,nodead][help,nodead][@player]灵魂石
```

---

### Ritual of Souls / Soulwell

```lua
#showtooltip 灵魂仪式
/cast 灵魂仪式
```

---

### Ritual of Summoning

```lua
#showtooltip 召唤仪式
/cast 召唤仪式
```

---

## 10. Summon / Sacrifice Macros

### Demonic Sacrifice

For Shadow Destro, usually sacrifice Succubus.
For Fire Destro, usually sacrifice Imp.

```lua
#showtooltip 恶魔牺牲
/cast 恶魔牺牲
```

---

### Fast Summon Felhunter

```lua
#showtooltip 召唤地狱猎犬
/cast 恶魔支配
/cast 召唤地狱猎犬
```

---

### Fast Summon Succubus

```lua
#showtooltip 召唤魅魔
/cast 恶魔支配
/cast 召唤魅魔
```

---

### Fast Summon Voidwalker

```lua
#showtooltip 召唤虚空行者
/cast 恶魔支配
/cast 召唤虚空行者
```

---

### Fast Summon Imp

```lua
#showtooltip 召唤小鬼
/cast 恶魔支配
/cast 召唤小鬼
```

---

### Modifier Summon Pet Macro

Default = Imp
Shift = Felhunter
Ctrl = Succubus
Alt = Voidwalker

```lua
#showtooltip
/cast [mod:shift]召唤地狱猎犬;[mod:ctrl]召唤魅魔;[mod:alt]召唤虚空行者;召唤小鬼
```

---

## 11. Recommended Keybind Layout

### Main DPS Bar

1. 暗影箭
2. 烧尽
3. 献祭
4. 腐蚀之种
5. 生命分流
6. 灵魂碎裂
7. 毁灭药水 / Burst macro
8. 暗影灼烧
9. 死亡缠绕
10. 恐惧术

### Curse Bar

- 元素诅咒
- 鲁莽诅咒
- 厄运诅咒
- 痛苦诅咒
- 语言诅咒
- 疲劳诅咒

### Pet / Control Bar

- 法术封锁 / 诱惑 smart macro
- Focus Spell Lock
- Focus Seduction
- Pet Attack / Follow
- 虚空行者牺牲
- 小鬼火焰之盾

---

## 12. Raid Rotation Reference

### Shadow Destro P2 Raid

```text
Before pull:
邪甲术
召唤魅魔
恶魔牺牲
确认拯救祝福
准备灵魂石 / 糖 / 灵魂井

Pull:
Wait 2-3 sec if tank threat is weak
Assigned Curse:
- 元素诅咒 if assigned
- 鲁莽诅咒 if assigned
- 厄运诅咒 if free DPS curse and boss lives 60+ sec

Main:
暗影箭 spam
Refresh assigned curse
生命分流 during movement
75%-85% tank threat: 灵魂碎裂
Burst after threat is safe:
饰品 + 毁灭药水 + 暗影箭
```

### Fire Destro P2 Raid

```text
Before pull:
邪甲术
召唤小鬼
恶魔牺牲

Pull:
Assigned Curse
献祭
烧尽 spam
Refresh 献祭 before/when it drops
Do not use 燃烧 as normal rotation unless movement/special case
```

### AoE Trash

```text
Wait for tank threat
腐蚀之种
腐蚀之种
腐蚀之种
Stop if threat is dangerous
Use 灵魂碎裂 before you rip aggro
```

---

## 13. Threat Rules

Warlock threat priority:

1. Always have 拯救祝福 if Alliance raid.
2. Do not open with trinket + potion instantly.
3. Use 灵魂碎裂 at 75%-85% of tank threat.
4. On AoE, wait 2-4 seconds before Seed.
5. If threat is high, stop one Shadow Bolt instead of dying.
6. Destruction Potion should be used when tank threat is stable.
7. Soulshatter is not just an emergency button; it is a second DPS window.

---

## 14. Notes for TBC Macro Compatibility

- TBC macros may have a 255-character limit.
- If a macro is too long, split it into separate macros.
- If localized pet condition fails, use English pet family in the condition:
  - `[pet:felhunter]`
  - `[pet:succubus]`
  - `[pet:voidwalker]`
  - `[pet:imp]`
- Keep Chinese spell names for `/cast`.
- Test every pet macro outside raid first.

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
