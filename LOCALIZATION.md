# Client localization / 客户端本地化

## English

### Locale pages

| Locale | Client language | Class page |
| --- | --- | --- |
| `enUS` | English | `README.md` |
| `zhCN` | Simplified Chinese | `README_zhCN.md` |

The English `README.md` is the default page and links to `[简体中文](README_zhCN.md)` at the top. The Chinese page links back with `[English](README.md)`.

Store English explanations and `enUS` macros only in `README.md`. Store Chinese explanations and matching `zhCN` macros in `README_zhCN.md`. Use the same stable ID and status for a macro on both pages. Keep commands, conditionals, target order, modifiers, ranks, and numerical item slots structurally identical; localize only client-visible game tokens.

Keep a single-language import in the source locale's backlog. On the other page, summarize it and link to the source backlog. Move it into both macro sets only when both locale entries exist. Mark it `verified` only after both variants are tested on the recorded client build.

Verify localized names in the matching client or an authoritative localized Blizzard source. Do not publish a guessed or machine-translated game token as verified.

## 中文

### 语言页面

| 区域代码 | 客户端语言 | 职业页面 |
| --- | --- | --- |
| `enUS` | 英文 | `README.md` |
| `zhCN` | 简体中文 | `README_zhCN.md` |

英文 `README.md` 是默认页面，顶部使用 `[简体中文](README_zhCN.md)` 链接到中文页面。中文页面顶部使用 `[English](README.md)` 返回英文页面。

英文说明和 `enUS` 宏只保存在 `README.md`；中文说明和对应的 `zhCN` 宏保存在 `README_zhCN.md`。同一个宏在两个页面必须使用相同的稳定 ID 和状态。命令、条件、目标顺序、修饰键、等级和数字物品栏位必须保持相同结构，只有客户端可见的游戏名称可以本地化。

单语言导入内容保存在来源语言页面的待处理区。另一语言页面只提供摘要和来源链接。只有两个语言条目都存在后，才能移入两个页面的宏组合；只有两个版本都在已记录的客户端版本中通过测试后，才能标记为 `verified`。

本地化名称必须在对应客户端或暴雪官方本地化资料中验证。未经验证的猜测或机器翻译不得标记为已验证。
