# TBC Paladin cross-session reference

> **Status:** Imported reference only — not a verified or fully localized macro release.

- Source scope: Curated `paladin_macros.md` export supplied from another session
- Game version: WoW TBC Classic / TBC Anniversary
- Class and level: Paladin, level 70
- Specializations: Retribution, Protection, Holy
- Source client locale: Simplified Chinese (`zhCN`)
- Imported: 2026-08-18
- Verification: Source-session claims preserved; macro behavior, spell ranks, and localized tokens have not been independently revalidated
- Locale completeness: `zhCN` source only; matching `enUS` and `zhTW` release files have not been produced

Before promoting any entry into `../macros/`, recheck it against the intended TBC client/build, verify localized spell and item names in the matching client, and create the locale set required by [LOCALIZATION.md](../../../LOCALIZATION.md). Exact Chinese ranks should be inserted from the spellbook with Shift-click when client formatting differs.

## TBC Paladin Macros — 中文客户端

### Context

```text
Game: WoW TBC Classic / TBC Anniversary
Client language: Chinese / 中文客户端
Class: Paladin / 圣骑士
Level: 70
Main specs discussed:
- Retribution / 惩戒骑
- Protection / 防骑
- Holy / 奶骑

Important:
- User uses Chinese client.
- Prefer Chinese spell names in all macros.
- If any spell name or rank fails, open spellbook, edit macro, then Shift-click the spell from spellbook to insert exact localized spell name.
```

---

## 0. General Notes

### 中文客户端等级格式

Some Chinese clients require exact rank formatting. Example:

```lua
命令圣印(等级 1)
```

If it fails, do not manually guess spacing. Use:

```text
Open spellbook → find Rank 1 命令圣印 → Shift-click into macro editor
```

### Useful keybind philosophy

Recommended core structure:

```text
Ret:
1  十字军打击
2  审判 + 命令圣印等级1
3  单独命令圣印等级1
4  殉难圣印
5  奉献

Prot:
1  神圣之盾
2  奉献
3  审判 + 正义圣印
4  复仇者之盾

Holy:
1  圣光闪现
2  圣光术
3  神圣震击
4  清洁术
5  神恩术 + 圣光术
```

---

## 1. Retribution Paladin / 惩戒骑 Macros

### 1.1 十字军打击

```lua
#showtooltip 十字军打击
/startattack
/cast 十字军打击
```

---

### 1.2 审判 + 命令圣印等级1

Use this as the main Ret raid Judgement key.

Purpose:

```text
当前身上是殉难圣印
→ 审判殉难圣印
→ 自动补命令圣印等级1
→ 等 swing timer 最后约0.4秒
→ 手动按殉难圣印
```

```lua
#showtooltip 审判
/startattack
/cast 审判
/cast 命令圣印(等级 1)
```

Recommended bind:

```text
2 = 审判 + 命令圣印等级1
```

Important:

```text
Only press this when GCD is available.
If you press it during GCD, 审判 may fire but 命令圣印 may fail.
```

---

### 1.3 单独命令圣印等级1

Use this when Judgement is not ready and you only want to prepare a seal twist.

```lua
#showtooltip 命令圣印(等级 1)
/cast 命令圣印(等级 1)
/startattack
```

Recommended bind:

```text
3 = 命令圣印等级1
```

---

### 1.4 殉难圣印

Use this manually in the last ~0.4s of the swing timer.

```lua
#showtooltip 殉难圣印
/startattack
/cast 殉难圣印
```

Recommended bind:

```text
4 = 殉难圣印
```

---

### 1.5 惩戒圣印五合一

Optional macro if you want several seals on one button.

```lua
#showtooltip
/cast [mod:shift,mod:ctrl] 智慧圣印; [mod:shift] 命令圣印(等级 1); [mod:ctrl] 命令圣印; [mod:alt] 复仇圣印; 殉难圣印
/startattack [nomod:shift,harm,nodead]
```

Usage:

```text
No modifier:        殉难圣印
Shift:             命令圣印等级1
Ctrl:              最高等级命令圣印
Alt:               复仇圣印
Shift+Ctrl:        智慧圣印
```

Recommended bind:

```text
4 = this macro
```

If using this macro, still keep a separate `3 = 命令圣印等级1` if you want cleaner twisting.

---

### 1.6 最高等级命令圣印 for questing

Use for solo questing, not raid seal twisting.

```lua
#showtooltip 命令圣印
/cast 命令圣印
/startattack
```

Recommended bind:

```text
Shift+3 = 最高等级命令圣印
```

---

### 1.7 复仇圣印

Useful for high-health solo elite targets or special cases. Not part of normal Ret raid seal twisting.

```lua
#showtooltip 复仇圣印
/cast 复仇圣印
/startattack
```

Recommended bind:

```text
Shift+4 = 复仇圣印
```

---

### 1.8 十字军圣印 / 开场挂强化十字军审判

```lua
#showtooltip 十字军圣印
/cast 十字军圣印
/startattack
```

Open with:

```text
十字军圣印
→ 审判
→ 命令圣印等级1
→ 最后0.4秒殉难圣印
```

---

### 1.9 驱邪术

```lua
#showtooltip 驱邪术
/cast 驱邪术
```

Use only on:

```text
恶魔
亡灵
```

---

### 1.10 奉献

Highest rank:

```lua
#showtooltip 奉献
/cast 奉献
```

Optional downrank macro. Use Shift-click from spellbook to insert the exact rank.

```lua
#showtooltip 奉献(等级 3)
/cast 奉献(等级 3)
```

Recommended:

```text
5        奉献等级3/4 for single target
Shift+5  满级奉献 for AoE
```

---

### 1.11 复仇之怒 + 饰品

```lua
#showtooltip 复仇之怒
/use 13
/use 14
/cast 复仇之怒
```

Warning:

```text
复仇之怒会造成自律。
自律期间不能使用圣盾术、圣佑术、保护祝福。
Do not use before mechanics where you may need bubble.
```

---

## 2. Ret Rotation Reference

### Raid single target, Alliance

Core seal twist:

```text
命令圣印（等级1）
→ swing timer 最后约0.4秒
→ 殉难圣印
```

Judgement timing:

```text
身上是殉难圣印
→ 审判
→ 命令圣印等级1
→ 最后0.4秒殉难圣印
```

Key pattern:

```text
审判 ready:
2 → wait swing timer → 4

Judgement not ready:
3 → wait swing timer → 4
```

Do not:

```text
Do not judge 命令圣印等级1.
Do not press 十字军打击 in the last twist window.
Do not use 愤怒之锤 in normal PvE rotation; it can reset swing timer.
```

---

## 3. Protection Paladin / 防骑 Macros

### 3.1 神圣之盾

```lua
#showtooltip 神圣之盾
/cast 神圣之盾
```

Recommended bind:

```text
1 = 神圣之盾
```

---

### 3.2 奉献

```lua
#showtooltip 奉献
/cast 奉献
```

Recommended bind:

```text
2 = 奉献
```

---

### 3.3 审判 + 正义圣印

Use this as the default Prot threat macro.

```lua
#showtooltip 审判
/startattack
/cast 审判
/cast 正义圣印
```

Recommended bind:

```text
3 = 审判 + 正义圣印
```

Note:

```text
If target is out of Judgement range, macro may still recast 正义圣印.
```

---

### 3.4 防骑圣印选择

```lua
#showtooltip
/cast [mod:shift] 智慧圣印; [mod:alt] 复仇圣印; 正义圣印
/startattack [harm,nodead]
```

Usage:

```text
No modifier:  正义圣印
Shift:        智慧圣印
Alt:          复仇圣印
```

---

### 3.5 复仇者之盾

```lua
#showtooltip 复仇者之盾
/cast 复仇者之盾
/startattack
```

Recommended bind:

```text
4 = 复仇者之盾
```

Important:

```text
Do not cast while raid boss is actively hitting you unless timing is safe.
Casting means you cannot dodge/parry/block during the cast.
```

---

### 3.6 正义防御 Mouseover

```lua
#showtooltip 正义防御
/cast [@mouseover,help,nodead] 正义防御; [help,nodead] 正义防御; [@targettarget,help,nodead] 正义防御
```

Priority:

```text
Mouseover friendly target
→ current friendly target
→ target's target
```

Recommended bind:

```text
E = 正义防御
```

---

### 3.7 正义之怒 toggle

```lua
#showtooltip 正义之怒
/cancelaura [mod:alt] 正义之怒
/cast [nomod] 正义之怒
```

Usage:

```text
Press:      开启正义之怒
Alt+Press: 取消正义之怒
```

---

### 3.8 神圣愤怒

```lua
#showtooltip 神圣愤怒
/cast 神圣愤怒
```

Use on:

```text
亡灵
恶魔
```

---

### 3.9 防骑圣盾术 / 取消圣盾

```lua
#showtooltip 圣盾术
/cancelaura [mod:alt] 圣盾术
/cast [nomod] 圣盾术
```

Usage:

```text
Press:      圣盾术
Alt+Press: 取消圣盾术
```

Tank note:

```text
Using 圣盾术 can make mobs leave you.
If using it only to clear debuff, cancel quickly.
```

---

## 4. Holy Paladin / 奶骑 Macros

### 4.1 圣光闪现 Mouseover

```lua
#showtooltip 圣光闪现
/cast [@mouseover,help,nodead] 圣光闪现; [help,nodead] 圣光闪现; [@player] 圣光闪现
```

Recommended bind:

```text
1 = 圣光闪现
```

---

### 4.2 圣光术 Mouseover

```lua
#showtooltip 圣光术
/cast [@mouseover,help,nodead] 圣光术; [help,nodead] 圣光术; [@player] 圣光术
```

Recommended bind:

```text
2 = 圣光术
```

---

### 4.3 低等级圣光术 Mouseover

Use for Light’s Grace / mana control. Insert exact rank from spellbook.

```lua
#showtooltip 圣光术(等级 5)
/cast [@mouseover,help,nodead] 圣光术(等级 5); [help,nodead] 圣光术(等级 5); [@player] 圣光术(等级 5)
```

Recommended bind:

```text
Shift+2 = 低等级圣光术
```

---

### 4.4 神圣震击 Mouseover

```lua
#showtooltip 神圣震击
/cast [@mouseover,help,nodead] 神圣震击; [help,nodead] 神圣震击; [@player] 神圣震击
```

Recommended bind:

```text
3 = 神圣震击
```

---

### 4.5 清洁术 Mouseover

```lua
#showtooltip 清洁术
/cast [@mouseover,help,nodead] 清洁术; [help,nodead] 清洁术; [@player] 清洁术
```

Recommended bind:

```text
4 = 清洁术
```

---

### 4.6 神恩术 + 圣光术 Emergency Heal

```lua
#showtooltip 神恩术
/cast 神恩术
/cast [@mouseover,help,nodead] 圣光术; [help,nodead] 圣光术; [@player] 圣光术
```

Recommended bind:

```text
5 or Shift+2 = 神恩术 + 圣光术
```

---

### 4.7 神启

```lua
#showtooltip 神启
/cast 神启
```

Recommended bind:

```text
T = 神启
```

If Chinese client does not recognize `神启`, Shift-click the spell from spellbook.

---

### 4.8 圣疗术 Mouseover

```lua
#showtooltip 圣疗术
/cast [@mouseover,help,nodead] 圣疗术; [help,nodead] 圣疗术; [@player] 圣疗术
```

Recommended bind:

```text
G = 圣疗术
```

---

### 4.9 圣光术 with Alt Stopcasting

Use only if you want an emergency override.

```lua
#showtooltip 圣光术
/stopcasting [mod:alt]
/cast [@mouseover,help,nodead] 圣光术; [help,nodead] 圣光术; [@player] 圣光术
```

Usage:

```text
Press:      normal Holy Light
Alt+Press: stop current cast and start Holy Light immediately
```

---

## 5. Universal Paladin Utility Macros

### 5.1 圣盾术 / 圣佑术 / 取消免疫

Recommended bind:

```text
Z
```

```lua
#showtooltip [mod:shift] 圣佑术; 圣盾术
/stopcasting
/cancelaura [mod:alt] 圣盾术
/cancelaura [mod:alt] 圣佑术
/cast [mod:shift] 圣佑术; [nomod] 圣盾术
```

Usage:

```text
Z        圣盾术
Shift+Z 圣佑术
Alt+Z   取消圣盾术/圣佑术
```

---

### 5.2 简单圣盾术

```lua
#showtooltip 圣盾术
/cast 圣盾术
```

---

### 5.3 Bubble Hearth

```lua
#showtooltip 炉石
/cancelaura 圣盾术
/cast 圣盾术
/use 炉石
```

Optional safer version without cancel first:

```lua
#showtooltip 炉石
/cast 圣盾术
/use 炉石
```

Recommended bind:

```text
Shift+Z or side bar only
```

Do not put this on the main emergency bubble key.

---

### 5.4 保护祝福 Mouseover

```lua
#showtooltip 保护祝福
/cast [@mouseover,help,nodead] 保护祝福; [help,nodead] 保护祝福
```

Recommended bind:

```text
G or Shift+G = 保护祝福
```

Tank warning:

```text
Do not accidentally BoP yourself as tank.
```

---

### 5.5 取消自身保护祝福

```lua
/cancelaura 保护祝福
```

---

### 5.6 自由祝福 Mouseover

```lua
#showtooltip 自由祝福
/cast [@mouseover,help,nodead] 自由祝福; [help,nodead] 自由祝福; [@player] 自由祝福
```

Recommended bind:

```text
T or Mouse4 = 自由祝福
```

---

### 5.7 牺牲祝福 Mouseover

```lua
#showtooltip 牺牲祝福
/cast [@mouseover,help,nodead] 牺牲祝福; [help,nodead] 牺牲祝福
```

Use cases:

```text
Break crowd-control effects
Maiden of Virtue repentance tech
Help tank absorb damage
```

---

### 5.8 制裁之锤 Mouseover Enemy

```lua
#showtooltip 制裁之锤
/cast [@mouseover,harm,nodead] 制裁之锤; 制裁之锤
```

Recommended bind:

```text
R = 制裁之锤
```

---

### 5.9 忏悔 Mouseover Enemy

```lua
#showtooltip 忏悔
/cast [@mouseover,harm,nodead] 忏悔; 忏悔
```

Recommended bind:

```text
T = 忏悔 for Ret
```

---

### 5.10 清洁术 Universal Mouseover

```lua
#showtooltip 清洁术
/cast [@mouseover,help,nodead] 清洁术; [help,nodead] 清洁术; [@player] 清洁术
```

Recommended bind:

```text
F or 4 = 清洁术
```

---

## 6. Blessing Macros

### 6.1 力量祝福

```lua
#showtooltip 力量祝福
/cast [@mouseover,help,nodead] 力量祝福; [help,nodead] 力量祝福; [@player] 力量祝福
```

---

### 6.2 智慧祝福

```lua
#showtooltip 智慧祝福
/cast [@mouseover,help,nodead] 智慧祝福; [help,nodead] 智慧祝福; [@player] 智慧祝福
```

---

### 6.3 王者祝福

```lua
#showtooltip 王者祝福
/cast [@mouseover,help,nodead] 王者祝福; [help,nodead] 王者祝福; [@player] 王者祝福
```

---

### 6.4 拯救祝福

```lua
#showtooltip 拯救祝福
/cast [@mouseover,help,nodead] 拯救祝福; [help,nodead] 拯救祝福; [@player] 拯救祝福
```

---

### 6.5 庇护祝福

```lua
#showtooltip 庇护祝福
/cast [@mouseover,help,nodead] 庇护祝福; [help,nodead] 庇护祝福; [@player] 庇护祝福
```

---

## 7. Trinkets / Items / Engineering

### 7.1 Trinket macro

```lua
#showtooltip
/use 13
/use 14
```

---

### 7.2 Use upper trinket only

```lua
#showtooltip 13
/use 13
```

---

### 7.3 Use lower trinket only

```lua
#showtooltip 14
/use 14
```

---

### 7.4 地精火箭发射器

```lua
#showtooltip 地精火箭发射器
/use 地精火箭发射器
```

---

### 7.5 超级神风炸药

```lua
#showtooltip 超级神风炸药
/use 超级神风炸药
```

---

### 7.6 地精工兵炸药

```lua
#showtooltip 地精工兵炸药
/use 地精工兵炸药
```

---

### 7.7 Mana Potion

Use the exact potion name you carry. Example placeholder:

```lua
#showtooltip
/use 法力药水
```

For raid consumables, Shift-click the exact item from bags into the macro.

---

## 8. Suggested Keybind Layout

### 8.1 Ret / 惩戒

```text
1        十字军打击
2        审判 + 命令圣印等级1
3        命令圣印等级1
4        殉难圣印
5        奉献

Q        驱邪术
E        复仇之怒 + 饰品
R        制裁之锤
F        清洁术
T        忏悔

Z        圣盾术 / 圣佑术 / 取消
X        法力药水 / 糖 / 血瓶
C        饰品
V        工程炸弹

Shift+3  最高等级命令圣印
Shift+4  复仇圣印
Shift+5  满级奉献
```

---

### 8.2 Prot / 防护

```text
1        神圣之盾
2        奉献
3        审判 + 正义圣印
4        复仇者之盾

Q        驱邪术
E        正义防御
R        制裁之锤
F        清洁术
T        自由祝福
G        保护祝福

Z        圣盾术 / 取消圣盾
X        圣疗术
C        饰品 / 药水
V        工程炸弹

Shift+1  智慧圣印
Shift+2  低等级奉献
Shift+3  复仇圣印
```

---

### 8.3 Holy / 神圣

```text
1        圣光闪现
2        圣光术
3        神圣震击
4        清洁术
5        神恩术 + 圣光术

Q        保护祝福
E        自由祝福
R        制裁之锤
F        自我治疗 / 清洁术
T        神启
G        圣疗术

Z        圣盾术
X        法力药水 / 糖
C        饰品
V        工程手雷

Shift+1  低等级圣光术
Shift+2  大圣光急救
Shift+E  牺牲祝福
```

---

## 9. WA / Spell ID Notes

These are not macros, but useful for WeakAuras.

```text
正义之怒 spell ID: 25780
神圣之盾 spell ID: 27179
```

### 正义之怒 missing WA

Trigger:

```text
类型: 光环
单位: 玩家
光环类型: 增益效果
精确法术ID: 25780
显示: 光环缺失
```

### 神圣之盾 cooldown WA

Use cooldown trigger, not aura trigger.

```text
类型: 法术
事件: 冷却/充能/次数
法术: 神圣之盾 / 27179
显示: 总是
忽略公共冷却: 开启
```

Display logic:

```text
默认透明度: 100%
条件:
如果冷却中 / 剩余时间 > 0
→ 透明度 35%
→ 褪色 开启
```

---

## 10. Important Ret Timing Summary

### Correct TBC Ret seal twisting

```text
命令圣印（等级1）
→ final ~0.4s before swing lands
→ 殉难圣印
```

### Judgement timing

```text
Only judge while 殉难圣印 is active.
Then immediately prepare 命令圣印等级1.
```

Correct:

```text
2 审判 + 命令等级1
→ wait swing timer
→ 4 殉难圣印
```

If Judgement is not ready:

```text
3 命令等级1
→ wait swing timer
→ 4 殉难圣印
```

Do not:

```text
Do not judge 命令圣印等级1.
Do not press 十字军打击 in final twist window.
Do not use 愤怒之锤 in normal raid rotation.
```
