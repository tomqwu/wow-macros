# Nature's Swiftness + Healing Touch

- Game: WoW TBC Classic / TBC Anniversary
- Specialization: Restoration Druid
- Purpose: One-button emergency mouseover heal
- Client locales: `enUS`, `zhCN`, `zhTW`
- Verification date: 2026-08-18
- Source: User-supplied `enUS` and `zhCN` session context; `zhTW` spell terminology cross-checked against official Blizzard localization

## Macro variants

| Behavior | English | Simplified Chinese | Traditional Chinese |
| --- | --- | --- | --- |
| Recommended | [enUS](restoration-natures-swiftness-healing-touch.enUS.macro) | [zhCN](restoration-natures-swiftness-healing-touch.zhCN.macro) | [zhTW](restoration-natures-swiftness-healing-touch.zhTW.macro) |
| Arena-safe | [enUS](restoration-natures-swiftness-healing-touch-arena-safe.enUS.macro) | [zhCN](restoration-natures-swiftness-healing-touch-arena-safe.zhCN.macro) | [zhTW](restoration-natures-swiftness-healing-touch-arena-safe.zhTW.macro) |

## English

The macro stops the current cast, cancels any shapeshift form, activates Nature's Swiftness, and casts the highest learned rank of Healing Touch.

The recommended version uses this target priority:

1. Friendly, living mouseover unit.
2. Friendly, living current target.
3. Player character.

The arena-safe version skips the current target and uses mouseover, then the player. This avoids healing an unintended friendly target.

### Cell and mouse usage

A keyboard-bound mouseover macro works over Cell and other secure raid frames. Put the macro on an action bar and bind that slot. On macOS, a Logitech MX side button can be mapped to an unused key such as `F8` or `F9` in Logi Options+, then that key can be bound in WoW.

### Limitation

WoW macros cannot conditionally test whether the Nature's Swiftness buff is active. If it is on cooldown, pressing the macro can begin a normal hard-cast Healing Touch. Keep the Nature's Swiftness tooltip visible and use the macro when the cooldown is ready.

Suggested binding: `R`, `Shift-R`, or a mapped mouse button.

## 简体中文

此宏会停止当前施法、取消变形形态、激活自然迅捷，并施放已学会的最高等级治疗之触。

推荐版的目标优先级为：友方存活鼠标指向目标、友方存活当前目标、玩家自己。竞技场安全版会跳过当前目标，只治疗鼠标指向目标，否则治疗自己。

普通按键绑定的鼠标指向宏可在 Cell 等安全团队框架上使用。自然迅捷冷却时，此宏可能开始正常读条施放治疗之触；请保留自然迅捷的提示图标，并只在技能可用时使用。

## 繁體中文

此巨集會停止目前施法、取消變形形態、啟動自然迅捷，並施放已學會的最高等級治療之觸。

建議版的目標優先順序為：存活的友方滑鼠指向目標、存活的友方目前目標、玩家自己。競技場安全版會略過目前目標，只治療滑鼠指向目標，否則治療自己。

一般按鍵綁定的滑鼠指向巨集可在 Cell 等安全團隊框架上使用。自然迅捷冷卻時，此巨集可能開始正常讀條施放治療之觸；請保留自然迅捷的提示圖示，並只在技能可用時使用。

## Localization sources

- `enUS` and `zhCN` macro text was supplied directly in the session context.
- Blizzard's Traditional Chinese [Druid class article](https://worldofwarcraft.blizzard.com/zh-tw/news/19956929/) uses `治療之觸`.
- Blizzard's Traditional Chinese [5.4 patch notes](https://worldofwarcraft.blizzard.com/zh-tw/news/10788364/) use `自然迅捷`.

If any localized token is rejected by the TBC client, replace it by Shift-clicking the exact spell from that client's spellbook into the macro editor.
