# WoW Macros

A versioned library of World of Warcraft macros distilled from working conversations.

一个从对话中整理并按游戏版本保存的《魔兽世界》宏命令库。

## Active version / 当前版本

| Version | Status | Browse |
| --- | --- | --- |
| TBC Classic / TBC Anniversary | Active | [Classes and macros](tbc/) |

Content is currently organized for TBC only. Future game versions should use sibling top-level folders so incompatible macros are never mixed.

目前内容仅按 TBC 整理。其他游戏版本应使用独立的顶层目录，避免混用不兼容的宏。

## Generation workflow / 生成流程

Use the repository's [TBC Macro Builder skill](skills/build-tbc-macros/SKILL.md) to turn a player's level, talent build, key talents, rotation, role, content, targeting preferences, and client details into a compact macro set.

使用仓库中的 [TBC 宏生成 Skill](skills/build-tbc-macros/SKILL.md)，根据玩家等级、天赋配置、关键天赋、技能循环、职责、玩法、目标优先级和客户端信息生成精简宏组合。

Every class page uses the same player profile, rotation/talent model, paired macro set, imported-reference backlog, and verification log. English-only or Chinese-only source material remains backlog until both variants exist and are tested.

## File conventions

- Class macro collection and default class page: `<version>/classes/<class>/README.md`
- Cross-session macro references awaiting verification stay in the matching class's `README.md` with an explicit status.
- Use lowercase kebab-case filenames.
- Record the game version or patch and verification date when behavior can change.
- Give each macro a specialization-and-purpose heading and keep its explanation beside its code.
- Keep matching English (`enUS`) and Simplified Chinese (`zhCN`) code blocks together under the same macro entry and behaviorally identical.
- Do not create a separate file for each macro.

See [LOCALIZATION.md](LOCALIZATION.md) for client-language and verification rules. / 客户端语言及验证规则请参阅 [LOCALIZATION.md](LOCALIZATION.md)。
