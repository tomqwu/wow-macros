# Client localization / 客户端本地化

## English

### Supported clients

| Locale | Client language | Section heading |
| --- | --- | --- |
| `enUS` | English | `English (enUS)` |
| `zhCN` | Simplified Chinese | `简体中文 (zhCN)` |

Keep every class's macros in its single `README.md` document. When a macro contains localized spell, item, talent, aura, or other game text, place both client variants under the same macro entry using the headings above. Keep their conditionals and behavior identical; only localized tokens should differ. Use one client-neutral code block only when every token works unchanged in both supported clients.

Verify localized names in the matching client or an authoritative localized Blizzard source. Do not publish a guessed or machine-translated game token as verified.

## 中文

### 支持的客户端

| 区域代码 | 客户端语言 | 小节标题 |
| --- | --- | --- |
| `enUS` | 英文 | `English (enUS)` |
| `zhCN` | 简体中文 | `简体中文 (zhCN)` |

每个职业的所有宏都保存在该职业目录的 `README.md` 文档中，这样打开职业目录时会自动显示。如果宏包含本地化的法术、物品、天赋、光环或其他游戏文本，应在同一宏条目下使用上述标题放置英文和简体中文两个代码块。两个版本的条件与功能应完全一致，只有本地化名称可以不同。仅当所有内容在两个客户端中都无需翻译时，才使用一个客户端通用代码块。

本地化名称必须在对应客户端或暴雪官方本地化资料中验证。未经验证的猜测或机器翻译不得标记为已验证。
