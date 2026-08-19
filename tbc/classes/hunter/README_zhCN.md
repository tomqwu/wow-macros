# 猎人宏

[English](README.md)

## 玩家配置

| 字段 | 内容 |
| --- | --- |
| 游戏版本 | WoW TBC Classic / TBC Anniversary 风格；未提供准确客户端版本 |
| 职业 | 猎人 |
| 等级 | 70 |
| 天赋配置 | 未提供单一天赋点法；源资料涉及野兽控制、射击和生存天赋专属技能 |
| 关键天赋 | 源资料在不同备选天赋中提到狂野怒火、胁迫、沉默射击和翼龙钉刺 |
| 职责 / 玩法 | PvE 循环、团队副本、误导、宠物控制、陷阱、风暴要塞跳怪和 PvP 焦点控制 |
| 循环来源 | 导入的 `zhCN` 宏包包含稳固射击时机、自动射击、杀戮命令、冷却和按键说明 |
| 客户端语言 | 简体中文（`zhCN`） |
| 最后更新 | 2026-08-19 |
| 总体状态 | 44 个具名 `zhCN` 宏块仍为 `imported-reference`；尚无双语配对宏组合 |

## 技能循环与天赋模型

### 玩家循环

- 起手：资料提供了猎人印记加宠物攻击的起手工具；尚未整理出具体首领战起手。
- 持续优先级：资料讨论了围绕自动射击安排稳固射击并使用杀戮命令，但尚未确认单一天赋对应的优先级。
- 冷却 / 应急：资料包含狂野怒火加饰品、假死、陷阱、召回宠物和误导。

### 宏设计机会

- 确定实际天赋和循环后，再从资料中整理射击、误导、宠物控制、陷阱、守护和焦点宏。
- 生成宠物专用控制宏时，保留已提供的掠食者和风蛇背景。

### 明确保留手动操作

- 自动射击穿插和完整伤害优先级必须手动执行，因为宏不能智能判断时机。
- 在确认玩家当前天赋前，不把天赋专属技能提升为正式宏。

## 宏组合

目前没有双语配对宏。必须先根据玩家实际天赋筛选导入的 `zhCN` 宏包，再补齐并测试对应的 `enUS` 版本。

## 导入参考资料

> 状态：`imported-reference`

- 来源范围：另一会话提供的 TBC 猎人宏包和第二阶段宠物交接资料
- 来源语言：简体中文（`zhCN`）
- 游戏版本：WoW TBC Classic / TBC Anniversary 风格
- 职业与等级：70 级猎人
- 宠物背景：70 级、忠诚度 6 的掠食者及其核心技能与毒蛇神殿抗性计划；风蛇用于风暴要塞跳怪
- 用途：PvE 循环、误导、宠物控制与照料、守护、陷阱、风暴要塞跳怪和 PvP 焦点控制
- 导入日期：2026-08-18
- 内容：44 个具名宏块，以及动作条、限制、宠物训练、抗性和团队职责说明
- 验证状态：保留源会话中的说法；尚未独立复核宏行为、本地化名称、宠物训练点数或客户端兼容性
- 语言完整度：仅有 `zhCN` 源资料；尚未生成配对的 `enUS` 正式版本
- 隐私与范围：已按原记录省略宠物名称、回复语言偏好和下一会话控制指令

源格式在每个代码块首行放置了便于阅读的宏名称；该行不是可执行命令，复制到 WoW 时必须删除。在标记为已验证前，应在目标 TBC 客户端版本中测试，并核对准确的本地化法术和宠物技能名称，再按 [LOCALIZATION.md](../../../LOCALIZATION.md) 添加配对版本。以下导入正文在既有隐私与范围删减的基础上完整保留。

## TBC Hunter — Complete Macro Pack and P2 Pet Handoff

### Imported gameplay context

- Game version: **World of Warcraft TBC Classic / Anniversary-style TBC**
- Client language: **Simplified Chinese**
- Hunter level: **70**
- Pet family: **掠食者**
- Pet level and loyalty: **70级，忠诚度6**
- Core pet skills already completed:
  - **撕咬9**
  - **角刺9**
  - **突进3**
  - **毒蛇反射**
  - **躲避2**
- Current resistance investment:
  - **自然抗性5**
  - Screenshot showed **122 training points remaining**
- Planned SSC finishing allocation:
  - **冰霜抗性5**: 105 points
  - **暗影抗性2**: 15 points
  - 2 points remain
  - Optional **自然护甲1**: 1 point
- P2 pet usage:
  - **Five-man dungeons and general PvE:** Ravager first
  - **SSC:** Ravager with Nature/Frost resistance
  - **TK trash skips and Eyes of the Beast pulling:** Wind Serpent is the utility choice
  - Wind Serpent ranged utility comes from **闪电吐息**; it is not a fully ranged pet
- In normal groups and raids:
  - Keep **低吼** autocast off
  - Keep the pet behind targets
  - Use **突进/俯冲** manually for opening and target switching
- For all future macros:
  1. Put each macro in its own code block.
  2. Put the macro name on the first line of the code block.
  3. Start the actual macro on the second line.
  4. Use only English half-width punctuation in macro bodies.
  5. Use the exact Simplified Chinese spell names recognized by the game client.
  6. Clearly label alternate versions and their different purposes.
  7. Prefer short, directly usable macros.

---

## 1. PvE rotation macros

### Safe Steady Shot macro

This does not automate shot timing. Use a shot timer and press it during the Steady Shot window so Auto Shot is not clipped.

```text
稳固射击+自动射击+杀戮命令
#showtooltip 稳固射击
/cast 杀戮命令
/cast !自动射击
/cast 稳固射击
```

### Auto Shot without accidentally toggling it off

```text
只开自动射击
#showtooltip 自动射击
/cast !自动射击
```

### Kill Command by itself

Useful when Kill Command is bound separately and should not be coupled to Steady Shot.

```text
单独杀戮命令
#showtooltip 杀戮命令
/cast 杀戮命令
```

### Hunter's Mark plus pet attack

Uses a hostile mouseover first; otherwise uses the current hostile target.

```text
猎人印记+宠物攻击
#showtooltip 猎人印记
/cast [@mouseover,harm,nodead][harm,nodead] 猎人印记
/petattack [@mouseover,harm,nodead][harm,nodead]
```

### Mouseover Tranquilizing Shot

```text
鼠标指向宁神射击
#showtooltip 宁神射击
/cast [@mouseover,harm,nodead][] 宁神射击
```

### Mouseover Distracting Shot

```text
鼠标指向扰乱射击
#showtooltip 扰乱射击
/cast [@mouseover,harm,nodead][] 扰乱射击
```

### Bestial Wrath with usable trinkets

This attempts the upper trinket first and then the lower trinket. Shared cooldown rules still apply.

```text
狂野怒火+饰品
#showtooltip 狂野怒火
/use 13
/use 14
/cast 狂野怒火
```

---

## 2. Misdirection macros

### Priority: focus, mouseover, then pet

- Friendly living focus has first priority.
- Friendly living mouseover has second priority.
- Living pet is the fallback.

```text
误导焦点/鼠标指向/宠物
#showtooltip 误导
/cast [@focus,help,nodead][@mouseover,help,nodead][@pet,exists,nodead] 误导
```

### Set a friendly mouseover as focus and cast Misdirection

With no valid friendly mouseover, it uses the existing friendly focus; if none exists, it uses the pet.

```text
设置焦点并误导
#showtooltip 误导
/focus [@mouseover,help,nodead]
/cast [@focus,help,nodead][@pet,exists,nodead] 误导
```

### Pet-only Misdirection

```text
误导宠物
#showtooltip 误导
/cast [@pet,exists,nodead] 误导
```

---

## 3. Core pet-control macros

### Normal press attacks; Shift recalls and sets passive

```text
宠物攻击/Shift召回
#showtooltip
/petattack [nomod,@mouseover,harm,nodead][nomod,harm,nodead]
/petpassive [mod:shift]
/petfollow [mod:shift]
```

### Emergency pet recall

```text
宠物紧急召回
#showtooltip
/petpassive
/petfollow
```

### Toggle Growl autocast

```text
切换低吼自动施放
#showtooltip 低吼
/petautocasttoggle 低吼
```

### Five-man and raid pet mode

For the Ravager. Pet stays passive until manually ordered to attack.

```text
副本宠物模式
#showtooltip
/petpassive
/petfollow
/petautocastoff 低吼
/petautocaston 撕咬
/petautocaston 角刺
```

### Solo and questing pet mode

```text
单刷宠物模式
#showtooltip
/petdefensive
/petautocaston 低吼
/petautocaston 撕咬
/petautocaston 角刺
```

### Dash or Dive on one key

Only the movement skill known by the active pet will cast.

```text
宠物加速
#showtooltip
/cast 突进
/cast 俯冲
```

### Family special attack on one key

- Ravager: 角刺
- Wind Serpent: 闪电吐息
- Scorpid: 蝎毒

```text
宠物家族技能
#showtooltip
/cast 角刺
/cast 闪电吐息
/cast 蝎毒
```

### Ravager Gore manually

```text
手动角刺
#showtooltip 角刺
/cast 角刺
```

### Wind Serpent Lightning Breath manually

Uses a hostile mouseover first and otherwise the current target.

```text
手动闪电吐息
#showtooltip 闪电吐息
/cast [@mouseover,harm,nodead][] 闪电吐息
```

### Scorpid Poison manually

```text
手动蝎毒
#showtooltip 蝎毒
/cast [@mouseover,harm,nodead][] 蝎毒
```

---

## 4. Pet care macros

### Call, revive, or mend the pet

- Dead pet: Revive Pet
- No active pet: Call Pet
- Living active pet: Mend Pet

```text
召唤/复活/治疗宠物
#showtooltip
/cast [@pet,dead] 复活宠物; [nopet] 召唤宠物; [@pet,nodead] 治疗宠物
```

### Safe Dismiss Pet

```text
安全解散野兽
#showtooltip 解散野兽
/petpassive
/petfollow
/cast 解散野兽
```

### Feign Death with pet recall

This is the safer dungeon and raid version when both hunter and pet should disengage.

```text
假死+宠物召回
#showtooltip 假死
/stopcasting
/stopattack
/petpassive
/petfollow
/cast 假死
```

### Personal Feign Death without changing pet behavior

Use this when the pet must continue attacking.

```text
单独假死
#showtooltip 假死
/stopcasting
/stopattack
/cast 假死
```

---

## 5. Aspect macros

### Hawk normally, Viper with Shift, Cheetah with Ctrl

```text
守护整合
#showtooltip
/cast [mod:shift] 蝰蛇守护; [mod:ctrl] 猎豹守护; 雄鹰守护
```

### Cancel Aspect of the Cheetah immediately

```text
取消猎豹守护
/cancelaura 猎豹守护
```

---

## 6. Trap macros

### Feign Death plus Freezing Trap

In combat this normally requires two presses:

1. First press: stop attacks, recall pet, Feign Death.
2. Second press: place Freezing Trap.

Out of combat it places the trap directly.

```text
假死冰冻陷阱
#showtooltip 冰冻陷阱
/stopcasting
/stopattack
/petpassive
/petfollow
/cast [combat] 假死
/cast 冰冻陷阱
```

### Feign Death plus Frost Trap

```text
假死冰霜陷阱
#showtooltip 冰霜陷阱
/stopcasting
/stopattack
/petpassive
/petfollow
/cast [combat] 假死
/cast 冰霜陷阱
```

### Feign Death plus Explosive Trap

```text
假死爆炸陷阱
#showtooltip 爆炸陷阱
/stopcasting
/stopattack
/petpassive
/petfollow
/cast [combat] 假死
/cast 爆炸陷阱
```

### Feign Death plus Snake Trap

```text
假死毒蛇陷阱
#showtooltip 毒蛇陷阱
/stopcasting
/stopattack
/petpassive
/petfollow
/cast [combat] 假死
/cast 毒蛇陷阱
```

---

## 7. Tempest Keep pet-skip macros

### Prepare Wind Serpent and enter Eyes of the Beast

This disables pet attacks before taking direct control. Lightning Breath should be used manually only when needed.

```text
风暴跳怪准备+野兽之眼
#showtooltip 野兽之眼
/petpassive
/petfollow
/petautocastoff 低吼
/petautocastoff 撕咬
/petautocastoff 闪电吐息
/cast 野兽之眼
```

### Wind Serpent skip pull

Uses Lightning Breath on a hostile mouseover first, otherwise the current target.

```text
风蛇远程补拉
#showtooltip 闪电吐息
/cast [@mouseover,harm,nodead][] 闪电吐息
```

### Wind Serpent emergency recall after a skip attempt

```text
风蛇跳怪后召回
#showtooltip
/petpassive
/petfollow
```

### Restore Wind Serpent combat autocasts

```text
风蛇恢复战斗模式
#showtooltip
/petpassive
/petautocastoff 低吼
/petautocaston 撕咬
/petautocaston 闪电吐息
```

---

## 8. PvP focus macros

### Focus Scatter Shot

```text
焦点驱散射击
#showtooltip 驱散射击
/cast [@focus,harm,nodead][] 驱散射击
```

### Focus Silencing Shot

```text
焦点沉默射击
#showtooltip 沉默射击
/cast [@focus,harm,nodead][] 沉默射击
```

### Focus Concussive Shot

```text
焦点震荡射击
#showtooltip 震荡射击
/cast [@focus,harm,nodead][] 震荡射击
```

### Focus Viper Sting

```text
焦点蝰蛇钉刺
#showtooltip 蝰蛇钉刺
/cast [@focus,harm,nodead][] 蝰蛇钉刺
```

### Mouseover Viper Sting

```text
鼠标指向蝰蛇钉刺
#showtooltip 蝰蛇钉刺
/cast [@mouseover,harm,nodead][] 蝰蛇钉刺
```

### Focus Wyvern Sting

Only usable with the Survival talent.

```text
焦点翼龙钉刺
#showtooltip 翼龙钉刺
/cast [@focus,harm,nodead][] 翼龙钉刺
```

### Focus Intimidation

Only usable with the Beast Mastery talent.

```text
焦点胁迫
#showtooltip 胁迫
/cast [@focus,harm,nodead][] 胁迫
```

### Send pet to focus

```text
宠物攻击焦点
#showtooltip
/petattack [@focus,harm,nodead]
```

### Scorpid attacks focus and applies poison

```text
蝎子攻击焦点+蝎毒
#showtooltip 蝎毒
/petattack [@focus,harm,nodead]
/cast [@focus,harm,nodead] 蝎毒
```

### Wing Clip plus Raptor Strike

```text
摔绊+猛禽一击
#showtooltip 摔绊
/startattack
/cast 摔绊
/cast 猛禽一击
```

---

## 9. Recommended action-bar assignment

A practical PvE layout:

| Key | Action |
|---|---|
| `1` | 稳固射击+自动射击+杀戮命令 |
| `2` | 多重射击 |
| `3` | 奥术射击 |
| `4` | 毒蛇钉刺 |
| `Q` | 猎人印记+宠物攻击 |
| `E` | 宠物攻击/Shift召回 |
| `R` | 误导焦点/鼠标指向/宠物 |
| `F` | 假死+宠物召回 |
| `C` | 宠物加速 |
| `Shift-C` | 宠物紧急召回 |
| `Mouse 4` | 狂野怒火+饰品 |
| `Mouse 5` | 守护整合 |
| `Shift-1` | 冰冻陷阱 |
| `Shift-2` | 冰霜陷阱 |
| `Shift-3` | 爆炸陷阱 |
| `Shift-4` | 毒蛇陷阱 |

For TK skip duty, place these next to each other:

1. 风暴跳怪准备+野兽之眼
2. 宠物加速
3. 风蛇远程补拉
4. 风蛇跳怪后召回

---

## 10. Important limitations

- A macro cannot fully automate the Hunter rotation.
- One hardware key press cannot intelligently choose and execute multiple protected global-cooldown actions.
- The Steady Shot macro still requires correct timing around the ranged swing timer.
- Do not repeatedly spam a rotation macro so quickly that Steady Shot clips Auto Shot.
- The Feign Death trap macros normally require two presses while already in combat.
- Pet autocast settings persist until changed, so verify **低吼** before entering a dungeon or raid.
- Wind Serpent Lightning Breath is a single-target ranged pet ability; the pet itself still uses melee auto-attacks.
- Macro spell names must exactly match the Simplified Chinese client. Do not insert English spell names into these macros unless the game client language is changed.

---

## 验证记录

| 宏 ID | 状态 | enUS | zhCN | 客户端版本 | 日期 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
