---
id: essence
name: "Essence"
category: essence
action: reroll_all
affects: [prefix, suffix]
mod_pool_tags: ["depends-on-essence"]
guarantee: guaranteed
destructive: reroll_all
preconditions:
  rarity: [normal, rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: low
inputs:
  - "Essence of <type>, any tier"
see_also:
  - fossil-weighted-reforge
  - harvest-reforge-tag-biased
tags:
  - essence
  - action:reroll_all
  - guarantee:guaranteed
  - destructive:reroll_all
  - cost:low
---

# Essence

Source: [PoE Wiki - Essence, Crafting section](https://www.poewiki.net/wiki/Essence).

## What it does

Using an essence on a normal item upgrades it to rare, rerolls all mods, and guarantees one specific mod fixed by the essence's type.

Tier 5+ essences (Screaming, Shrieking, Deafening) can also be used directly on a rare item instead. This works the same way: full reroll, one guaranteed mod. Tiers 1-4 can't do this, they only work on normal items.

Essences don't work on magic items.

Tiers 1-4 also cap the level of the other, non-guaranteed mods (35/45/60/75 depending on tier), regardless of the item's actual item level. Tier 5+ has no cap.

Corrupted-only essences (Insanity, Horror, Hysteria, Delirium) work the same way, but guarantee a unique modifier instead of a normal one.

Essences cannot be used on an item with a meta-crafted mod, like Prefixes Cannot Be Changed or Cannot Roll Caster Modifiers. It just errors out and does nothing.

## Limitations

- Full reroll. Don't use once you have mods worth keeping.
- Only one mod is guaranteed, the rest is random.
- Not usable on unique items.
- Blocked entirely by meta-crafted mods.

See the [essence guaranteed modifiers table](essence-modifiers.md) for what each essence guarantees per item class.

## Data completeness

Core mechanic, tier caps, and meta-mod block verified against the PoE Wiki Essence page (fetched 2026-07-30). The corrupted-only family's "guarantees a unique modifier" behavior is per your description, not independently wiki-verified yet.
