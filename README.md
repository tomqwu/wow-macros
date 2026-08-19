# WoW Macros

A versioned library of World of Warcraft macros and talent loadouts distilled from working conversations.

一个从对话中整理并版本化保存的《魔兽世界》宏命令与天赋配置库。

## Layout

Each Retail class has separate areas for macros and talents. Add one macro or build per file so changes stay easy to review and reuse.

| Class | Specializations | Macros | Talents |
| --- | --- | --- | --- |
| Druid | Balance, Feral, Guardian, Restoration | [Macros](tbc/classes/druid/macros/) | [Talents](tbc/classes/druid/talents/) |
| Hunter | Beast Mastery, Marksmanship, Survival | [Macros](tbc/classes/hunter/macros/) | [Talents](tbc/classes/hunter/talents/) |
| Mage | Arcane, Fire, Frost | [Macros](tbc/classes/mage/macros/) | [Talents](tbc/classes/mage/talents/) |
| Paladin | Holy, Protection, Retribution | [Macros](tbc/classes/paladin/macros/) | [Talents](tbc/classes/paladin/talents/) |
| Priest | Discipline, Holy, Shadow | [Macros](tbc/classes/priest/macros/) | [Talents](tbc/classes/priest/talents/) |
| Rogue | Assassination, Outlaw, Subtlety | [Macros](tbc/classes/rogue/macros/) | [Talents](tbc/classes/rogue/talents/) |
| Shaman | Elemental, Enhancement, Restoration | [Macros](tbc/classes/shaman/macros/) | [Talents](tbc/classes/shaman/talents/) |
| Warlock | Affliction, Demonology, Destruction | [Macros](tbc/classes/warlock/macros/) | [Talents](tbc/classes/warlock/talents/) |
| Warrior | Arms, Fury, Protection | [Macros](tbc/classes/warrior/macros/) | [Talents](tbc/classes/warrior/talents/) |

The list reflects Retail as verified on 2026-08-18. It includes the Devourer Demon Hunter specialization introduced with Midnight. See Blizzard's [playable class reference](https://worldofwarcraft.blizzard.com/en-us/game/classes) and [Midnight launch overview](https://worldofwarcraft.blizzard.com/en-us/news/24243639/world-of-warcraft-midnight%E2%84%A2-goes-live-march-2).

## File conventions

- English macro: `classes/<class>/macros/<specialization>-<purpose>.enUS.macro`
- Simplified Chinese macro: `classes/<class>/macros/<specialization>-<purpose>.zhCN.macro`
- Traditional Chinese macro: `classes/<class>/macros/<specialization>-<purpose>.zhTW.macro`
- Client-neutral macro: `classes/<class>/macros/<specialization>-<purpose>.macro`
- Talent build: `classes/<class>/talents/<specialization>-<build>.md`
- Cross-session reference awaiting verification or localization: `classes/<class>/context/<topic>.md`
- Use lowercase kebab-case filenames.
- Record the game version or patch and verification date when behavior can change.
- Keep explanations next to the macro or import string they describe.
- Keep English and Chinese macro variants behaviorally identical. Talent files use one shared import string with English, 简体中文, and 繁體中文 explanation sections.

See [LOCALIZATION.md](LOCALIZATION.md) for client-language and verification rules. / 客户端语言及验证规则请参阅 [LOCALIZATION.md](LOCALIZATION.md)。

No fully localized and verified macro or talent build has been released yet. Imported reference context is linked from the relevant class index until it is promoted into client-specific files.
