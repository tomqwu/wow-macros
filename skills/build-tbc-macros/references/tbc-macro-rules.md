# TBC macro design rules

## Contents

- Rotation-to-macro model
- Combat decision limits
- Useful patterns
- Build-sensitive behavior
- Localization
- Review checklist

## Rotation-to-macro model

Start from the player's actual spell priority and talent build. Macros should reduce targeting friction, expose modifiers, coordinate explicitly chosen cooldowns, control pets/forms/stances, or provide safe emergency actions. Keep the rotation itself as player-readable guidance.

For each rotation step, decide:

1. Does the spell need a target fallback such as mouseover, focus, target, then self?
2. Does a key talent add a new action or change the spell used?
3. Does the action require a form, stance, pet, item slot, or cancel command?
4. Would a modifier reduce keybind pressure without hiding behavior?
5. Is the action safer and clearer as a separate key?

## Combat decision limits

- Never claim that a macro can choose actions from cooldowns, auras, procs, resources, range, threat, or target health.
- Never present a macro as an automated or adaptive combat rotation.
- Do not assume several protected or global-cooldown actions will execute from one keypress.
- Treat `/castsequence` as a fixed user-driven sequence. Document reset conditions and failure modes; do not describe it as smart.
- Describe a macro's exact target priority and self fallback.
- Make destructive toggles, attack cancellation, form cancellation, pet mode changes, and immunity cancellation explicit.

## Useful patterns

Consider these only when they match the player profile:

- friendly or hostile mouseover fallbacks;
- focus crowd control, interrupts, dispels, or pet abilities;
- modifier-based spell or rank selection;
- `!` commands that avoid accidental toggle cancellation;
- `/stopcasting`, `/stopattack`, `/cancelform`, or aura cancellation with a documented reason;
- numeric equipment or trinket slots;
- pet attack, recall, mode, and family-ability controls;
- party or arena unit IDs for fixed targeting.

## Build-sensitive behavior

Validate client support before relying on conditionals or commands, especially cursor placement, focus/arena units, pet-family logic, ranked spell syntax, form/stance behavior, and sequence resets. Record uncertainty as a limitation and keep the status `ready-for-client-test` or `imported-reference`.

Do not hardcode a rank unless the player's rotation requires it. When a rank is required, insert the exact spell from the target client's spellbook and record why that rank matters.

## Localization

- Keep `enUS` macros in `README.md` and matching `zhCN` macros in `README_zhCN.md` under the same stable ID.
- Keep commands, conditionals, target order, modifiers, ranks, and item slots structurally identical across the page pair.
- Localize only client-visible game tokens.
- Obtain exact localized spell and item names from the target client, preferably by inserting them from the spellbook or inventory.
- Do not mark machine-translated or guessed tokens as verified.
- Repeat a client-neutral macro on both pages so navigation and macro IDs stay complete.

## Review checklist

- Is the macro derived from a documented rotation step, talent, or utility need?
- Is every protected action expected to require a keypress?
- Are target priority and fallback behavior explicit?
- Are risky cancel, stop, toggle, pet, form, or stance effects documented?
- Are both locale blocks structurally identical?
- Is the status supported by the verification log?
- Does the macro fit the target client's macro editor and work on the named build?
