# 潜行者宏

[English](README.md)

## 玩家配置

| 字段 | 内容 |
| --- | --- |
| 游戏版本 | WoW TBC Classic；具体客户端版本未提供 |
| 职业 | 潜行者 |
| 等级 | 未提供 |
| 天赋配置 | 战斗；具体点数分配未提供 |
| 关键天赋 | 来源包含还击、剑刃乱舞和冲动 |
| 职责 / 玩法 | 练级、法力陵墓潜行采集、副本采集和基础 PvP |
| 循环来源 | 导入的 `zhCN` 宏包包含常规战斗与潜行采集优先级、毒药、物品和按键设置 |
| 客户端语言 | 简体中文（`zhCN`） |
| 最后更新 | 2026-08-19 |
| 总体状态 | 26 个 `zhCN` 宏仍为 `imported-reference`；尚无双语宏组合 |

## 技能循环与天赋模型

### 玩家循环

- 起手：来源包含搜索加偷袭等潜行起手，以及绕过副本目标所需的控制方式。
- 持续优先级：来源概述了邪恶攻击攒连击点、触发还击、终结技、打断和冷却技能的使用。
- 冷却 / 应急：来源包含剑刃乱舞、冲动、消失、闪避、疾跑、暗影斗篷和绷带。

### 宏设计机会

- 可从战斗计划中提炼自动攻击、停止攻击、鼠标指向打断、潜行保护、冷却、毒药和焦点宏。
- 应先明确练级、采集或 PvP 场景，再从原始资料中选择最小可用宏组合。

### 明确保留手动操作

- 连击点消费、能量时机、站位选择和脱离决定保持手动。
- 在玩家提供实际背包物品和客户端名称前，不发布特定毒药等级或绷带物品。

## 宏组合

尚无双语宏。需要先确定战斗专精的具体玩法，补齐对应 `enUS` 版本并完成测试。

## 导入参考资料

> 状态：`imported-reference`

- 来源范围：另一会话提供的 TBC 战斗潜行者宏包
- 来源语言：简体中文（`zhCN`）
- 游戏版本：WoW TBC Classic；具体客户端版本未提供
- 导入日期：2026-08-18
- 内容：26 个宏，以及按键、循环、毒药、物品和采集说明
- 验证状态：保留来源会话中的说法；尚未独立复核宏行为、物品等级和本地化名称
- 语言完整性：目前仅有 `zhCN` 来源；尚未生成配套 `enUS` 发布版本

发布前必须在目标 TBC 客户端中测试本地化技能和物品名称，并按照 [本地化规范](../../../LOCALIZATION.md) 添加匹配版本。毒药等级和绷带必须替换为背包中的准确物品。原始资料为了兼容 TBC 时代客户端而使用 `target=mouseover` 语法。

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

## 验证记录

| 宏 ID | 状态 | enUS | zhCN | 客户端版本 | 日期 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
