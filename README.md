# WoW Macros

A versioned library of World of Warcraft macros and talent loadouts distilled from working conversations.

一个从对话中整理并按游戏版本保存的《魔兽世界》宏命令与天赋配置库。

## Active version / 当前版本

| Version | Status | Browse |
| --- | --- | --- |
| TBC Classic / TBC Anniversary | Active | [Classes, macros, and talents](tbc/) |

Content is currently organized for TBC only. Future game versions should use sibling top-level folders so incompatible macros and talent trees are never mixed.

目前内容仅按 TBC 整理。其他游戏版本应使用独立的顶层目录，避免混用不兼容的宏和天赋树。

## File conventions

- English macro: `<version>/classes/<class>/macros/<specialization>-<purpose>.enUS.macro`
- Simplified Chinese macro: `<version>/classes/<class>/macros/<specialization>-<purpose>.zhCN.macro`
- Traditional Chinese macro: `<version>/classes/<class>/macros/<specialization>-<purpose>.zhTW.macro`
- Client-neutral macro: `<version>/classes/<class>/macros/<specialization>-<purpose>.macro`
- Talent build: `<version>/classes/<class>/talents/<specialization>-<build>.md`
- Cross-session reference awaiting verification or localization: `<version>/classes/<class>/context/<topic>.md`
- Use lowercase kebab-case filenames.
- Record the game version or patch and verification date when behavior can change.
- Keep explanations next to the macro or import string they describe.
- Keep English and Chinese macro variants behaviorally identical. Talent files include English, 简体中文, and 繁體中文 explanation sections.

See [LOCALIZATION.md](LOCALIZATION.md) for client-language and verification rules. / 客户端语言及验证规则请参阅 [LOCALIZATION.md](LOCALIZATION.md)。
