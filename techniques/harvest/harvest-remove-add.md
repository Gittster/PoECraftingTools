---
id: harvest-remove-add
name: "Harvest: Remove a Random Mod, Add a New Tagged Mod"
category: harvest
action: remove_add
affects: [prefix, suffix]
mod_pool_tags: ["chosen-at-craft-time"]
guarantee: guaranteed
destructive: remove_one
preconditions:
  rarity: [magic, rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: medium
inputs:
  - "Harvest Lifeforce (type/amount matching the chosen tag)"
see_also:
  - harvest-augment-add-mod
  - harvest-reforge-tag-biased
---

## What it does

"Add a new **&lt;tag&gt;** modifier and remove another random modifier." Removes one existing modifier at random, then adds a new modifier matching the chosen tag — and, unlike Augment, it works even when the item is already full, since it frees a slot as part of the same craft.

The prompt's example — *"Add a new Physical modifier and remove another random modifier from a non-Influenced item"* — is this craft. Some Harvest remove/add crafts have a **non-Influenced item only** variant (and separately, influence-specific variants exist for influenced items); which one you have access to depends on which Harvest crafting-bench unlocks you've collected.

## Why you'd use it

Use this when the item is full and you need to swap in a specific tag without doing a full reroll — e.g. sacrificing a mediocre random mod to guarantee an energy shield mod on an otherwise-good item. It's the "surgical fix" craft for items that are close but not quite there.

## Limitations

- Only applies to magic or rare items — a normal (white) item needs to be upgraded first.
- The mod that gets removed is **random** — you can't choose which existing modifier to sacrifice. If you have a mod worth protecting, this craft can destroy it.
- Guarantee is by tag only, not exact modifier or tier.
- The influenced/non-influenced restriction on some variants of this craft means it isn't always available for every item — check which bench unlock you actually have.

## Data completeness

Conceptual mechanic confirmed. Exact tag list, lifeforce cost, and the full set of influenced/non-influenced variants still need to be pulled in from wiki data.
