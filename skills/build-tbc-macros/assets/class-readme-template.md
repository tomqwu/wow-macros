# {{CLASS}} macros

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
| Client locales | English (`enUS`), Simplified Chinese (`zhCN`) |
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

Paired macros belong here only when both locale variants exist. Use `ready-for-client-test` until both are tested on the recorded client build.

### {{TALENT_TREE}} — {{PURPOSE}}

- ID: `{{STABLE_MACRO_ID}}`
- Status: `ready-for-client-test`
- Derived from: {{ROTATION_STEP_TALENT_OR_UTILITY_REQUIREMENT}}
- Use case: {{WHEN_TO_PRESS}}
- Targeting: {{TARGET_PRIORITY_OR_ACTIVATION}}
- Limitations: {{KNOWN_LIMITS}}

#### English (`enUS`)

```lua
#showtooltip {{ENGLISH_SPELL}}
/cast {{ENGLISH_SPELL}}
```

#### 简体中文 (`zhCN`)

```lua
#showtooltip {{SIMPLIFIED_CHINESE_SPELL}}
/cast {{SIMPLIFIED_CHINESE_SPELL}}
```

## Imported reference backlog

> Status: `imported-reference`

- Source scope: {{SOURCE}}
- Source locale: {{LOCALE}}
- Game version: {{GAME_VERSION}}
- Imported: {{YYYY-MM-DD}}
- Verification: Not independently tested

### Source material

{{PRESERVED_SOURCE_CONTEXT}}

## Verification log

| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `{{STABLE_MACRO_ID}}` | `ready-for-client-test` | static review | static review | {{BUILD_OR_NOT_SUPPLIED}} | {{YYYY-MM-DD}} | Requires in-client test. |
