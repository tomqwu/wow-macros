# TBC Combat Rogue cross-session reference

> **Status:** Imported reference only — not a verified or fully localized macro release.

- Source scope: Curated TBC Rogue Combat macro pack supplied from another session
- Game version: WoW TBC Classic; specific client build was not supplied
- Class and build: Rogue, Combat
- Use cases: Leveling, Mana-Tombs stealth farming, dungeon farming, and basic PvP
- Source client locale: Simplified Chinese (`zhCN`)
- Imported: 2026-08-18
- Contents: 26 macros plus keybind, rotation, poison, item, and farming notes
- Verification: Source-session claims preserved; macro behavior, item ranks, and localized tokens have not been independently revalidated
- Locale completeness: `zhCN` source only; matching `enUS` and `zhTW` release files have not been produced

Before promoting an entry into `../macros/`, test it against the intended TBC client/build, verify localized ability and item names, and create the locale set required by [LOCALIZATION.md](../../../../LOCALIZATION.md). Replace poison ranks and the bandage with exact bag items. The source intentionally uses `target=mouseover` syntax for TBC-era compatibility.

## TBC Rogue Combat Macro Pack

Purpose: TBC Rogue leveling / Combat Rogue / Mana-Tombs stealth farming / dungeon farming / basic PvP.

Client: Chinese WoW client skill names.
Macro condition style: uses `target=mouseover` for better TBC-era compatibility.

---

### Notes

- `16` = main-hand weapon slot.
- `17` = off-hand weapon slot.
- `13` = upper trinket slot.
- `14` = lower trinket slot.
- Replace poison ranks with the exact poison item names in your bags.
- Replace bandage name with your current bandage.
- For English client, replace Chinese skill names with English names.

---

## Core Combat Macros

### 1. Sinister Strike Auto-Attack

Recommended key: `1`

```macro
#showtooltip 邪恶攻击
/startattack
/cast 邪恶攻击
```

---

### 2. Riposte Auto-Attack

Recommended key: `R`

```macro
#showtooltip 还击
/startattack
/cast 还击
```

---

### 3. Gouge Stop-Attack

Recommended key: `E`

Important because normal auto-attacks can instantly break Gouge.

```macro
#showtooltip 凿击
/stopattack
/cast 凿击
```

---

### 4. Kick Mouseover

Recommended key: `Q`

Kicks mouseover target if available; otherwise kicks current target.

```macro
#showtooltip 脚踢
/cast [target=mouseover,harm,nodead][] 脚踢
```

---

### 5. Blind Mouseover

Recommended key: `F`

Blinds mouseover target if available; otherwise blinds current target.

```macro
#showtooltip 致盲
/cast [target=mouseover,harm,nodead][] 致盲
```

---

### 6. Vanish Stop-Attack

Recommended key: `C`

```macro
#showtooltip 消失
/stopattack
/cast 消失
```

---

### 7. Stealth No-Cancel Macro

Recommended key: Mouse Button 4 or another easy key.

`!潜行` prevents accidentally cancelling Stealth by pressing the button again.

```macro
#showtooltip 潜行
/cast !潜行
```

---

## Combat Cooldown Macros

### 8. Blade Flurry + Adrenaline Rush + Trinkets

Recommended key: `V` or `G`

Good for elites, 2-mob pulls, dangerous dungeon points, and burst windows.

```macro
#showtooltip 剑刃乱舞
/startattack
/use 13
/use 14
/cast 剑刃乱舞
/cast 冲动
```

Note: depending on client, cooldown, or GCD timing, this may need to be pressed twice.

---

### 9. Blade Flurry Only

Recommended key: `V`

Useful because you do not always want to bind Blade Flurry and Adrenaline Rush together.

```macro
#showtooltip 剑刃乱舞
/startattack
/cast 剑刃乱舞
```

---

### 10. Adrenaline Rush Only

Recommended key: `G`

```macro
#showtooltip 冲动
/startattack
/cast 冲动
```

---

## Stealth / Dungeon Farming Macros

### 11. Cheap Shot + Pick Pocket

Recommended stealth bar key: `1`

Use with auto-loot enabled.
For humanoid targets, this attempts Pick Pocket first, then Cheap Shot.

```macro
#showtooltip 偷袭
/cast 搜索
/cast 偷袭
```

---

### 12. Sap Mouseover

Recommended stealth bar key: `4`

Useful for Mana-Tombs, dungeon skips, patrol control, and PvP.

```macro
#showtooltip 闷棍
/cast [target=mouseover,harm,nodead][] 闷棍
```

---

### 13. Garrote Auto-Attack

Recommended stealth bar key: `2`

Good versus casters or targets where opener silence matters.

```macro
#showtooltip 绞喉
/startattack
/cast 绞喉
```

---

### 14. Cheap Shot Auto-Attack Only

Use this version when you do not want to Pick Pocket.

```macro
#showtooltip 偷袭
/startattack
/cast 偷袭
```

---

### 15. Distract Mouseover

Useful for dungeon stealth pathing and turning patrols.

```macro
#showtooltip 扰乱
/cast [target=mouseover,harm,nodead][] 扰乱
```

---

## Defensive / Survival Macros

### 16. Evasion

Recommended key: `Z`

```macro
#showtooltip 闪避
/cast 闪避
```

---

### 17. Sprint

Recommended key: `X`

```macro
#showtooltip 疾跑
/cast 疾跑
```

---

### 18. Self-Bandage

Recommended key: `Shift+X`

Replace `厚灵纹布绷带` with your current bandage.

Classic use:

```text
凿击 → 后退一点 → 绷带
```

Macro:

```macro
#showtooltip 厚灵纹布绷带
/stopattack
/use [target=player] 厚灵纹布绷带
```

---

### 19. Cloak of Shadows

Available at level 66 in TBC.

```macro
#showtooltip 暗影斗篷
/cast 暗影斗篷
```

---

## Poison Application Macros

### 20. Main-Hand Instant Poison

Replace `速效毒药 VII` with your current rank.

```macro
#showtooltip 速效毒药
/use 速效毒药 VII
/use 16
```

---

### 21. Off-Hand Crippling Poison

```macro
#showtooltip 致残毒药
/use 致残毒药 II
/use 17
```

---

### 22. Off-Hand Deadly Poison

Use for longer boss fights or elite mobs.

Replace `致命毒药 VII` with your current rank.

```macro
#showtooltip 致命毒药
/use 致命毒药 VII
/use 17
```

---

## PvP / Focus Control Macros

### 23. Set Focus

Sets mouseover enemy as focus.
If no mouseover exists, sets current hostile target as focus.

```macro
/focus [target=mouseover,harm,nodead][harm,nodead]
```

---

### 24. Focus Kick

Kicks focus target if available; otherwise kicks current target.

```macro
#showtooltip 脚踢
/cast [target=focus,harm,nodead][] 脚踢
```

---

### 25. Focus Blind

Blinds focus target if available; otherwise blinds current target.

```macro
#showtooltip 致盲
/cast [target=focus,harm,nodead][] 致盲
```

---

### 26. Focus Sap

Saps focus target if available; otherwise saps current target.

```macro
#showtooltip 闷棍
/cast [target=focus,harm,nodead][] 闷棍
```

---

## Recommended Keybinding Layout

### Main Combat Bar

| Key | Ability / Macro |
|---|---|
| `1` | 邪恶攻击 auto-attack macro |
| `2` | 切割 |
| `3` | 剔骨 |
| `4` | 割裂 |
| `5` | 肾击 |
| `Q` | 脚踢 mouseover macro |
| `E` | 凿击 stop-attack macro |
| `R` | 还击 auto-attack macro |
| `F` | 致盲 mouseover macro |
| `Z` | 闪避 |
| `X` | 疾跑 |
| `C` | 消失 stop-attack macro |
| `V` | 剑刃乱舞 |
| `G` | 冲动 |
| `Shift+X` | Self-bandage |
| Mouse Button 4 | 潜行 no-cancel macro |

---

### Stealth Bar

| Key | Ability / Macro |
|---|---|
| `1` | 偷袭 + 搜索 |
| `2` | 绞喉 |
| `3` | 伏击, if using dagger |
| `4` | 闷棍 mouseover macro |
| `R` | 扰乱 mouseover macro |
| `F` | 致盲 mouseover macro |
| `C` | 消失 stop-attack macro |

---

## Minimal Must-Have Macro Set

If you do not want to create all macros, make these first.

### Must-Have 1: Sinister Strike

```macro
#showtooltip 邪恶攻击
/startattack
/cast 邪恶攻击
```

### Must-Have 2: Gouge Stop-Attack

```macro
#showtooltip 凿击
/stopattack
/cast 凿击
```

### Must-Have 3: Kick Mouseover

```macro
#showtooltip 脚踢
/cast [target=mouseover,harm,nodead][] 脚踢
```

### Must-Have 4: Stealth No-Cancel

```macro
#showtooltip 潜行
/cast !潜行
```

### Must-Have 5: Vanish Stop-Attack

```macro
#showtooltip 消失
/stopattack
/cast 消失
```

### Must-Have 6: Cheap Shot + Pick Pocket

```macro
#showtooltip 偷袭
/cast 搜索
/cast 偷袭
```

---

## Usage Priorities

### Normal Combat Rogue Leveling

```text
邪恶攻击 → 切割 → 邪恶攻击到 4-5 星 → 剔骨
```

Use:

```text
还击 whenever it procs
脚踢 against casters
凿击 → 绷带 when low HP
剑刃乱舞 / 冲动 on dangerous pulls
```

---

### Mana-Tombs / Dungeon Stealth Farming

Basic pattern:

```text
潜行 → 闷棍 / 扰乱 to bypass → 开箱 / 挖矿 / 采草 → 消失 or reset
```

For humanoid targets:

```text
潜行 → 搜索 + 偷袭 → kill or escape
```

---

## End of TBC Rogue Combat Macro Pack
