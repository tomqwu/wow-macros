# WoW Macros

A versioned library of World of Warcraft macros and talent loadouts distilled from working conversations.

一个从对话中整理并版本化保存的《魔兽世界》宏命令与天赋配置库。

## Layout

Each Retail class has separate areas for macros and talents. Add one macro or build per file so changes stay easy to review and reuse.

| Class | Specializations | Macros | Talents |
| --- | --- | --- | --- |
| Death Knight | Blood, Frost, Unholy | [Macros](classes/death-knight/macros/) | [Talents](classes/death-knight/talents/) |
| Demon Hunter | Devourer, Havoc, Vengeance | [Macros](classes/demon-hunter/macros/) | [Talents](classes/demon-hunter/talents/) |
| Druid | Balance, Feral, Guardian, Restoration | [Macros](classes/druid/macros/) | [Talents](classes/druid/talents/) |
| Evoker | Augmentation, Devastation, Preservation | [Macros](classes/evoker/macros/) | [Talents](classes/evoker/talents/) |
| Hunter | Beast Mastery, Marksmanship, Survival | [Macros](classes/hunter/macros/) | [Talents](classes/hunter/talents/) |
| Mage | Arcane, Fire, Frost | [Macros](classes/mage/macros/) | [Talents](classes/mage/talents/) |
| Monk | Brewmaster, Mistweaver, Windwalker | [Macros](classes/monk/macros/) | [Talents](classes/monk/talents/) |
| Paladin | Holy, Protection, Retribution | [Macros](classes/paladin/macros/) | [Talents](classes/paladin/talents/) |
| Priest | Discipline, Holy, Shadow | [Macros](classes/priest/macros/) | [Talents](classes/priest/talents/) |
| Rogue | Assassination, Outlaw, Subtlety | [Macros](classes/rogue/macros/) | [Talents](classes/rogue/talents/) |
| Shaman | Elemental, Enhancement, Restoration | [Macros](classes/shaman/macros/) | [Talents](classes/shaman/talents/) |
| Warlock | Affliction, Demonology, Destruction | [Macros](classes/warlock/macros/) | [Talents](classes/warlock/talents/) |
| Warrior | Arms, Fury, Protection | [Macros](classes/warrior/macros/) | [Talents](classes/warrior/talents/) |

The list reflects Retail as verified on 2026-08-18. It includes the Devourer Demon Hunter specialization introduced with Midnight. See Blizzard's [playable class reference](https://worldofwarcraft.blizzard.com/en-us/game/classes) and [Midnight launch overview](https://worldofwarcraft.blizzard.com/en-us/news/24243639/world-of-warcraft-midnight%E2%84%A2-goes-live-march-2).

## File conventions

- English macro: `classes/<class>/macros/<specialization>-<purpose>.enUS.macro`
- Simplified Chinese macro: `classes/<class>/macros/<specialization>-<purpose>.zhCN.macro`
- Traditional Chinese macro: `classes/<class>/macros/<specialization>-<purpose>.zhTW.macro`
- Client-neutral macro: `classes/<class>/macros/<specialization>-<purpose>.macro`
- Talent build: `classes/<class>/talents/<specialization>-<build>.md`
- Use lowercase kebab-case filenames.
- Record the game version or patch and verification date when behavior can change.
- Keep explanations next to the macro or import string they describe.
- Keep English and Chinese macro variants behaviorally identical. Talent files use one shared import string with English, 简体中文, and 繁體中文 explanation sections.

See [LOCALIZATION.md](LOCALIZATION.md) for client-language and verification rules. / 客户端语言及验证规则请参阅 [LOCALIZATION.md](LOCALIZATION.md)。

No macro or talent build has been supplied yet; the repository is ready for the next class-specific conversation.
