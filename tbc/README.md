# TBC macros

World of Warcraft: The Burning Crusade Classic / TBC Anniversary content, organized by class and client locale.

《魔兽世界：燃烧的远征》经典版 / 周年纪念服内容，按职业与客户端语言整理。

| Class | TBC talent trees | Current status |
| --- | --- | --- |
| [Druid](classes/druid/) | Balance, Feral, Restoration | Two paired emergency-heal macros are ready for client testing |
| [Hunter](classes/hunter/) | Beast Mastery, Marksmanship, Survival | Imported `zhCN` rotation and pet backlog; active build not selected |
| [Mage](classes/mage/) | Arcane, Fire, Frost | Awaiting player build and rotation |
| [Paladin](classes/paladin/) | Holy, Protection, Retribution | Imported multi-build `zhCN` backlog; active build not selected |
| [Priest](classes/priest/) | Discipline, Holy, Shadow | Imported `enUS` pack with partial `zhCN` glossary; active build not selected |
| [Rogue](classes/rogue/) | Assassination, Combat, Subtlety | Imported Combat `zhCN` backlog; activity needs selection |
| [Shaman](classes/shaman/) | Elemental, Enhancement, Restoration | Awaiting player build and rotation |
| [Warlock](classes/warlock/) | Affliction, Demonology, Destruction | Imported Destruction `zhCN` backlog; build and pet plan need selection |
| [Warrior](classes/warrior/) | Arms, Fury, Protection | Awaiting player build and rotation |

Each class keeps all macros in its `README.md`, which GitHub displays automatically when the class folder is opened. Client-sensitive entries place their English (`enUS`) and Simplified Chinese (`zhCN`) code blocks together. Imported session material stays in the same class document with an unverified status until it is tested.

每个职业的所有宏都保存在该职业目录的 `README.md` 中，因此打开职业目录时会自动显示。宏中的法术或物品名称依赖客户端语言时，英文（`enUS`）和简体中文（`zhCN`）代码块放在同一条目中。从其他会话导入的资料会在同一职业文档中标记为未验证，测试完成后再更新状态。

See the repository [localization guide](../LOCALIZATION.md) for publishing and verification rules.

Use the [TBC Macro Builder skill](../skills/build-tbc-macros/SKILL.md) to add or normalize player-specific macro sets.
