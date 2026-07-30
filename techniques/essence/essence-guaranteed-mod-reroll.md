---
id: essence-guaranteed-mod-reroll
name: "Essence: Guaranteed Mod Reroll"
category: essence
action: reroll_all
affects: [prefix, suffix]
mod_pool_tags: ["depends-on-essence"]
guarantee: guaranteed
destructive: reroll_all
preconditions:
  rarity: [normal, magic, rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: low
inputs:
  - "Essence of <type> (any tier)"
see_also:
  - fossil-weighted-reforge
  - harvest-reforge-tag-biased
---

## What it does

Using an essence on a normal, magic, or rare item:

1. Upgrades the item to rare rarity (if it isn't already).
2. Removes **all** existing modifiers.
3. Rolls a fresh set of modifiers appropriate to a rare item of that rarity/item level.
4. **Guarantees** one specific modifier determined by the essence type, in a fixed prefix or suffix slot (e.g. an "Essence of Insulation" guarantees a cold resistance modifier).

Essences come in ascending tiers (roughly Muttering → Deafening, exact tier names have shifted between leagues) — higher tiers guarantee a higher-value roll of the same guaranteed mod, but the rest of the item's mods are still fully random.

## Why you'd use it

This is the cheapest way to lock in **one** specific mod you care about while treating everything else as a lottery. It's a good opening move when the guaranteed mod is your hardest requirement (e.g. a specific high-tier resistance or damage mod) and you're prepared to reroll or patch up the rest afterward with something more targeted (harvest, veiled orbs, eldritch currency).

## Limitations

- Wipes the entire item — don't use this once you already have other mods worth keeping.
- Only one mod is guaranteed; everything else, including whether you get useful prefix/suffix balance, is random.
- Not usable on unique items.
- Corrupted-only essence variants (the "Essence of Delirium/Horror/Hysteria/Insanity" family) behave differently and are not covered by this entry yet.

## Data completeness

Conceptual mechanic confirmed. Exact tier list, guaranteed-mod value ranges per tier, and which slot (prefix/suffix) each essence type guarantees still need to be pulled in from wiki/RePoE data.
