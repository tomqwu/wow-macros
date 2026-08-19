# Druid macros

TBC talent trees: Balance, Feral, Restoration.

Each macro entry keeps its English (`enUS`) and Simplified Chinese (`zhCN`) client variants together in this document.

## Restoration — Nature's Swiftness + Healing Touch

- Game: WoW TBC Classic / TBC Anniversary
- Specialization: Restoration Druid
- Purpose: One-button emergency mouseover heal
- Client locales: `enUS`, `zhCN`
- Verification date: 2026-08-18
- Source: User-supplied `enUS` and `zhCN` session context

### Recommended

Target priority: friendly living mouseover, friendly living target, then the player.

#### English (`enUS`)

```lua
#showtooltip Nature's Swiftness
/stopcasting
/cancelform
/cast Nature's Swiftness
/cast [@mouseover,help,nodead][@target,help,nodead][@player] Healing Touch
```

#### 简体中文 (`zhCN`)

```lua
#showtooltip 自然迅捷
/stopcasting
/cancelform
/cast 自然迅捷
/cast [@mouseover,help,nodead][@target,help,nodead][@player] 治疗之触
```

### Arena-safe

Target priority: friendly living mouseover, then the player. The current target is intentionally skipped.

#### English (`enUS`)

```lua
#showtooltip Nature's Swiftness
/stopcasting
/cancelform
/cast Nature's Swiftness
/cast [@mouseover,help,nodead][@player] Healing Touch
```

#### 简体中文 (`zhCN`)

```lua
#showtooltip 自然迅捷
/stopcasting
/cancelform
/cast 自然迅捷
/cast [@mouseover,help,nodead][@player] 治疗之触
```

### English notes

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

### 简体中文说明

此宏会停止当前施法、取消变形形态、激活自然迅捷，并施放已学会的最高等级治疗之触。

推荐版的目标优先级为：友方存活鼠标指向目标、友方存活当前目标、玩家自己。竞技场安全版会跳过当前目标，只治疗鼠标指向目标，否则治疗自己。

普通按键绑定的鼠标指向宏可在 Cell 等安全团队框架上使用。自然迅捷冷却时，此宏可能开始正常读条施放治疗之触；请保留自然迅捷的提示图标，并只在技能可用时使用。

### Localization sources

- `enUS` and `zhCN` macro text was supplied directly in the session context.

If any localized token is rejected by the TBC client, replace it by Shift-clicking the exact spell from that client's spellbook into the macro editor.
