---
id: harvest-augment-add-mod
name: "Harvest: Augment (Add a New Tagged Mod)"
category: harvest
action: add_mod
affects: [prefix, suffix]
mod_pool_tags: ["chosen-at-craft-time"]
guarantee: guaranteed
destructive: none
preconditions:
  rarity: [magic, rare]
  influence: []
  requires_open_affix: true
  requires_existing_mod_tag: []
cost_tier: low
inputs:
  - "Harvest Lifeforce (type/amount matching the chosen tag)"
see_also:
  - harvest-remove-add
  - harvest-reforge-tag-biased
---

## What it does

"Augment an item with a new **&lt;tag&gt;** modifier." Adds one new modifier matching the chosen tag into an unused prefix or suffix slot — nothing existing is touched, removed, or rerolled.

## Why you'd use it

The safest, most surgical harvest craft: use it once you already like everything on the item and just have a spare affix slot to fill with something specific (e.g. adding a resistance you're missing without risking anything else).

## Limitations

- Only applies to magic or rare items — a normal (white) item needs to be upgraded first (e.g. Orb of Transmutation/Alchemy, an essence, or a fossil reforge).
- **Requires an open affix slot** of the matching type (prefix mods need an open prefix slot, suffix mods need an open suffix slot). If the item is already full (2 prefixes + 2 suffixes on a rare), this craft isn't available — you'd need `harvest-remove-add` or another removal step first.
- Guarantee is by tag only, not exact modifier or tier — you can still land the tag's weakest roll.
- Doesn't let you choose which specific slot (prefix vs suffix) beyond what the tag pool allows.

## Data completeness

Conceptual mechanic confirmed. Exact tag list and lifeforce cost still need to be pulled in from wiki data.
