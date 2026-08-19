# Client localization / 客户端本地化

## English

### Supported clients

| Locale | Client language | Macro suffix |
| --- | --- | --- |
| `enUS` | English | `.enUS.macro` |
| `zhCN` | Simplified Chinese | `.zhCN.macro` |

When a macro contains localized spell, item, talent, aura, or other game text, publish both variants. Keep their conditionals and behavior identical; only localized tokens should differ. Use a single unsuffixed `.macro` file only when every token works unchanged in both supported clients.

Verify localized names in the matching client or an authoritative localized Blizzard source. Do not publish a guessed or machine-translated game token as verified.

Talent import strings are normally client-language neutral. Keep one Markdown file per build and include these sections:

- `English (enUS)`
- `简体中文 (zhCN)`

Record the game version or patch and the verification date once for the shared build.

## 中文

### 支持的客户端

| 区域代码 | 客户端语言 | 宏文件后缀 |
| --- | --- | --- |
| `enUS` | 英文 | `.enUS.macro` |
| `zhCN` | 简体中文 | `.zhCN.macro` |

如果宏中包含本地化的法术、物品、天赋、光环或其他游戏文本，必须同时提供英文和简体中文两个客户端版本。两个版本的条件与功能应完全一致，只有本地化名称可以不同。仅当所有内容在两个客户端中都无需翻译时，才使用不带区域后缀的 `.macro` 文件。

本地化名称必须在对应客户端或暴雪官方本地化资料中验证。未经验证的猜测或机器翻译不得标记为已验证。

天赋导入字符串通常不受客户端语言影响。每套配置使用一个 Markdown 文件，并包含以下小节：

- `English (enUS)`
- `简体中文 (zhCN)`

同一套配置只需记录一次游戏版本或补丁号以及验证日期。
