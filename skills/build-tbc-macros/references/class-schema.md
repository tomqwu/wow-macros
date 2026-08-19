# Class page schema

## Contents

- Player inputs
- Status model
- Required page structure
- Macro entry contract
- Import handling
- Verification log

## Player inputs

Capture these fields before deriving macros. Record `Not supplied` rather than guessing.

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
| Supported locales | This repository requires `enUS` and `zhCN`. |

## Status model

Use exactly one of these statuses:

| Status | Meaning | Location |
| --- | --- | --- |
| `verified` | Both locale variants were tested on the recorded TBC client build. | `Macro set` |
| `ready-for-client-test` | Both variants exist and passed static review but lack full client testing. | `Macro set` |
| `imported-reference` | Raw session material, a single-language macro, or an unreviewed claim. | `Imported reference backlog` |

Never use a verification date by itself as evidence of client testing. Record what was tested, on which locale and build, in the verification log.

## Required page structure

Every `tbc/classes/<class>/README.md` must contain these level-two headings in order:

1. `## Player profile`
2. `## Rotation and talent model`
3. `## Macro set`
4. `## Imported reference backlog`
5. `## Verification log`

The player profile table must include game version, class, level, talent build, key talents, role/content, rotation source, client locales, last updated, and overall status.

The rotation section must distinguish:

- the player's actual opener and priority;
- macro opportunities derived from that rotation;
- actions deliberately left manual.

## Macro entry contract

Each level-three macro entry in `Macro set` must contain:

- stable `ID`;
- `Status` (`verified` or `ready-for-client-test`);
- `Derived from` rotation step, talent, or utility requirement;
- `Use case`;
- `Targeting` or activation behavior;
- `Limitations`;
- paired `English (enUS)` and `简体中文 (zhCN)` Lua blocks;
- brief usage and test notes when needed.

The two locale blocks must be structurally identical. Spell, item, talent, aura, pet ability, and other client-visible tokens may differ.

## Import handling

Keep useful original session material, but place it under `Imported reference backlog` until it satisfies the macro entry contract. Add source scope, source locale, game version, import date, and verification status. Never mix raw single-language imports into the paired macro set.

Large imports may keep their original subsections below a clearly labeled source heading. Normalize them progressively; do not translate hundreds of untested macros merely to make the page look complete.

## Verification log

Use this table:

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Use `not tested`, `static review`, or a concrete test result. A `verified` row requires successful results for both locales and a named client build.
