---
id: harvest-reforge-tag-biased
name: "Harvest: Reforge with Guaranteed Tag"
category: harvest
action: reforge
affects: [prefix, suffix]
mod_pool_tags: ["chosen-at-craft-time"]
guarantee: guaranteed
destructive: reroll_all
preconditions:
  rarity: [rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: medium
inputs:
  - "Harvest Lifeforce (type/amount matching the chosen tag)"
see_also:
  - essence-guaranteed-mod-reroll
  - fossil-weighted-reforge
  - harvest-remove-add
---

## What it does

"Reforge a rare item with a new set of random modifiers, including a new **&lt;tag&gt;** modifier." Example from the prompt: *reforge with random modifiers, including a Life modifier.*

1. Removes all existing modifiers.
2. Rolls a completely fresh set of modifiers for a rare item at that base/item level.
3. **Guarantees** at least one of the new modifiers matches the chosen tag (life, resistance, physical damage, attack, caster, speed, etc. — the tag is picked when you craft, not fixed per-item like an essence).

Functionally similar to essence rerolling, but the guarantee is by **tag** (broader — "a life mod," any tier/type) rather than one exact fixed modifier, and it's only available on items that are already rare.

## Why you'd use it

Good fit when you know the *theme* you want guaranteed (e.g. "definitely has energy shield") but don't need one specific fixed modifier, and are fine gambling everything else. Cheaper in practice than chaining several targeted crafts if the guaranteed tag is your only hard requirement.

## Limitations

- Full reroll — same destructive caveat as essences/fossils.
- Only works on items already rare.
- The guarantee is tag-level, not tier-level: you can still get the *worst* roll of that tag.

## Data completeness

Conceptual mechanic confirmed (this is a very stable, long-standing Harvest craft). Exact list of available tags, lifeforce type/quantity cost per tag, and any base-type restrictions still need to be pulled in from wiki data.
