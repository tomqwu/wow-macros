# Druid macros

## Player profile

| Field | Value |
| --- | --- |
| Game version | WoW TBC Classic / TBC Anniversary; exact client build not supplied |
| Class | Druid |
| Level | Not supplied |
| Talent build | Restoration; point allocation not supplied |
| Key talents | Nature's Swiftness |
| Role / content | Emergency healing through Cell or another secure raid frame; arena-safe fallback requested |
| Rotation source | Only the emergency-heal step was supplied; full healing rotation was not supplied |
| Client locales | English (`enUS`), Simplified Chinese (`zhCN`) |
| Last updated | 2026-08-18 |
| Overall status | Two paired macros are `ready-for-client-test`; no in-client results recorded |

## Rotation and talent model

### Player rotation

- Opener: Not supplied.
- Sustained priority: Not supplied.
- Cooldowns / emergencies: Stop the current cast, leave form if necessary, activate Nature's Swiftness, then cast the highest learned Healing Touch on the intended friendly unit.

### Macro opportunities

- Combine the explicit Nature's Swiftness emergency step with a documented friendly target priority.
- Provide a raid-frame version that falls back to a friendly target, plus an arena-safe version that skips the current target.
- Preserve one-key access from Bear, Cat, Travel, or Tree Form by cancelling form first.

### Deliberately not macroed

- The normal Restoration healing rotation was not supplied and is not inferred.
- Cooldown or buff detection remains manual; the macro must not claim to decide whether Nature's Swiftness is ready.

## Macro set

### Restoration — Nature's Swiftness emergency heal

- ID: `restoration-natures-swiftness-healing-touch`
- Status: `ready-for-client-test`
- Derived from: The supplied Nature's Swiftness emergency-heal step and Restoration talent choice
- Use case: Stop the current cast and perform the emergency heal from any form
- Targeting: Friendly living mouseover, friendly living target, then player
- Limitations: If Nature's Swiftness is unavailable, Healing Touch can begin a normal hard cast; exact client build was not supplied

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

### Restoration — Nature's Swiftness emergency heal, arena-safe

- ID: `restoration-natures-swiftness-healing-touch-arena-safe`
- Status: `ready-for-client-test`
- Derived from: The same emergency step with the requested arena-safe target restriction
- Use case: Emergency heal without accidentally selecting a friendly current target
- Targeting: Friendly living mouseover, then player; current target is intentionally skipped
- Limitations: If Nature's Swiftness is unavailable, Healing Touch can begin a normal hard cast; exact client build was not supplied

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

### Usage notes

A keyboard-bound mouseover macro works over Cell and other secure raid frames. Put the macro on an action bar and bind that slot. On macOS, a Logitech MX side button can be mapped to an unused key such as `F8` or `F9`, then that key can be bound in WoW.

自然迅捷冷却时，此宏可能开始正常读条施放治疗之触。请保留自然迅捷的提示图标，并只在技能可用时使用。如果本地化名称被客户端拒绝，请从对应客户端的法术书中按 Shift 点击插入准确名称。

## Imported reference backlog

No unpaired macro backlog remains for the supplied Druid context. The original `enUS` and `zhCN` emergency-heal variants were incorporated into the macro set; client test evidence is still missing.

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `restoration-natures-swiftness-healing-touch` | `ready-for-client-test` | source supplied; static review | source supplied; static review | Not supplied | 2026-08-18 | Test form cancellation, target fallbacks, and cooldown failure behavior. |
| `restoration-natures-swiftness-healing-touch-arena-safe` | `ready-for-client-test` | source supplied; static review | source supplied; static review | Not supplied | 2026-08-18 | Test mouseover and self fallback without a friendly target fallback. |
