# {{CLASS}} macros

[简体中文](README_zhCN.md)

## Player profile

| Field | Value |
| --- | --- |
| Game version | {{GAME_VERSION}} |
| Class | {{CLASS}} |
| Level | {{LEVEL_OR_NOT_SUPPLIED}} |
| Talent build | {{TALENT_BUILD_OR_NOT_SUPPLIED}} |
| Key talents | {{KEY_TALENTS_OR_NOT_SUPPLIED}} |
| Role / content | {{ROLE_AND_CONTENT}} |
| Rotation source | {{USER_SUPPLIED_OR_NOT_SUPPLIED}} |
| Client locale | English (`enUS`) |
| Last updated | {{YYYY-MM-DD}} |
| Overall status | {{STATUS_SUMMARY}} |

## Rotation and talent model

### Player rotation

- Opener: {{OPENER_OR_NOT_SUPPLIED}}
- Sustained priority: {{PRIORITY_OR_NOT_SUPPLIED}}
- Cooldowns / emergencies: {{COOLDOWN_PLAN_OR_NOT_SUPPLIED}}

### Macro opportunities

- {{OPPORTUNITY_DERIVED_FROM_ROTATION_OR_TALENT}}

### Deliberately not macroed

- {{ACTION_LEFT_MANUAL_AND_REASON}}

## Macro set

### {{TALENT_TREE}} — {{PURPOSE}}

- ID: `{{STABLE_MACRO_ID}}`
- Status: `ready-for-client-test`
- Derived from: {{ROTATION_STEP_TALENT_OR_UTILITY_REQUIREMENT}}
- Use case: {{WHEN_TO_PRESS}}
- Targeting: {{TARGET_PRIORITY_OR_ACTIVATION}}
- Limitations: {{KNOWN_LIMITS}}

#### Macro

```lua
#showtooltip {{ENGLISH_SPELL}}
/cast {{ENGLISH_SPELL}}
```

## Imported reference backlog

> Status: `imported-reference`

- Source scope: {{SOURCE_OR_LINK_TO_ZHCN_BACKLOG}}
- Source locale: {{LOCALE}}
- Game version: {{GAME_VERSION}}
- Imported: {{YYYY-MM-DD}}
- Verification: Not independently tested

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `{{STABLE_MACRO_ID}}` | `ready-for-client-test` | static review | static review | {{BUILD_OR_NOT_SUPPLIED}} | {{YYYY-MM-DD}} | Requires in-client test. |
