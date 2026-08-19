# Class locale-page schema

## Contents

- Player inputs
- Locale files
- Status model
- Required page structure
- Macro pair contract
- Import handling
- Verification logs

## Player inputs

Capture these fields before deriving macros. Record `Not supplied` or `未提供` rather than guessing.

| Field | Why it matters |
| --- | --- |
| Game version and client build | Macro conditionals and supported behavior can differ. |
| Class and level | Determines learned spells, ranks, forms, stances, and pets. |
| Talent build or point allocation | Determines available abilities and rotation. |
| Key talents | Highlights abilities that need dedicated macros. |
| Role and content | Changes targeting, utility, threat, and emergency needs. |
| Opener and sustained rotation | Provides the source actions from which macros are derived. |
| Cooldown and emergency plan | Identifies burst, survival, and recovery macros. |
| Pets, forms, stances, items | Determines stateful commands and localized tokens. |
| Target priority | Defines mouseover, focus, target, party, arena, or self fallbacks. |
| Addons and input devices | Affects raid-frame mouseover use and practical keybinds. |

## Locale files

Every class directory contains exactly this pair:

- `README.md`: English default page. Put `[简体中文](README_zhCN.md)` directly below the title.
- `README_zhCN.md`: Simplified Chinese page. Put `[English](README.md)` directly below the title.

Do not mix Chinese prose or `zhCN` spell tokens into the English page. Keep source-language backlog only on its source page; summarize and link to it from the other page.

## Status model

Use exactly one of these statuses on both locale pages:

| Status | Meaning | Location |
| --- | --- | --- |
| `verified` | Both locale variants were tested on the recorded TBC client build. | Macro set / 宏组合 |
| `ready-for-client-test` | Both variants exist and passed static review but lack full client testing. | Macro set / 宏组合 |
| `imported-reference` | Raw session material, a single-language macro, or an unreviewed claim. | Backlog / 导入参考资料 |

Never use a date alone as evidence of client testing. Record the result and client build in both verification logs.

## Required page structure

English `README.md` headings, in order:

1. `## Player profile`
2. `## Rotation and talent model`
3. `## Macro set`
4. `## Imported reference backlog`
5. `## Verification log`

Chinese `README_zhCN.md` headings, in order:

1. `## 玩家配置`
2. `## 技能循环与天赋模型`
3. `## 宏组合`
4. `## 导入参考资料`
5. `## 验证记录`

Both profile tables capture the same facts. Both rotation sections distinguish the player's actual rotation, macro opportunities, and actions deliberately left manual.

## Macro pair contract

Each level-three macro entry has one locale-specific Lua block and these fields.

English fields: `ID`, `Status`, `Derived from`, `Use case`, `Targeting`, `Limitations`.

Chinese fields: `ID`, `状态`, `来源`, `用途`, `目标`, `限制`.

For every macro in either macro set:

- use the same stable ID and status on both pages;
- keep the same number and order of commands;
- keep conditionals, target order, modifiers, sequence resets, ranks, and numerical item slots structurally identical;
- localize only client-visible game tokens;
- add brief locale-specific usage notes when needed.

## Import handling

Place useful original session material under the source locale's backlog until it satisfies the macro pair contract. Record source scope, source locale, game version, import date, and verification status. On the other locale page, include a concise localized summary and a link to the full source backlog.

Large imports may keep their original subsections on the source page. Normalize them progressively; do not translate hundreds of untested macros merely to make the two pages look equally long.

## Verification logs

English table:

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Chinese table:

| 宏 ID | 状态 | enUS | zhCN | 客户端版本 | 日期 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |

The same macro IDs and statuses must appear in both logs. A `verified` row requires successful results for both locales and a named client build.
