---
id: essence-reforge-rare
name: "Essence: Reforge Rare Item"
category: essence
action: reroll_all
affects: [prefix, suffix]
mod_pool_tags: ["depends-on-essence"]
guarantee: guaranteed
destructive: reroll_all
preconditions:
  rarity: [rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: medium
inputs:
  - "Essence of <type>, tier 5+ only (Screaming, Shrieking, or Deafening)"
see_also:
  - essence-upgrade-normal-to-rare
  - fossil-weighted-reforge
  - harvest-reforge-tag-biased
tags:
  - essence
  - action:reroll_all
  - guarantee:guaranteed
  - destructive:reroll_all
  - cost:medium
---

# Essence: Reforge Rare Item

## What it does

Source: [PoE Wiki – Essence, §Crafting](https://www.poewiki.net/wiki/Essence).

> "Essences of tier 5 (Screaming) and above can also be used to reforge the affixes of rare equipment, like a Chaos Orb, with a guaranteed affix."

Applying a **Screaming, Shrieking, or Deafening** essence to an already-**rare** item:

1. Removes all existing modifiers (like a Chaos Orb reroll).
2. Rolls a fresh set of rare-appropriate modifiers, uncapped by item level (only tiers 5+ can do this, and those tiers have no secondary-mod level cap — see `essence-upgrade-normal-to-rare` for the cap table).
3. **Guarantees** one specific modifier fixed by the essence's type.

**Tiers 1-4 (Whispering through Wailing) cannot do this at all** — they can only upgrade a normal item, per the wiki's tier table (their "Item reforge" column is explicitly "No"). If you only have low-tier essences, this technique isn't available to you yet.

## Why you'd use it

This is the essence version of "reroll a rare I don't like, but guarantee it keeps/gains the one mod I actually need" — useful when you already have a rare with a good base type and item level but the wrong mods, and you want another shot with one guaranteed anchor. Since tier 5+ essences don't cap secondary mod levels, this is a legitimate way to fish for a strong 2-3 mod foundation before finishing with Harvest or eldritch currency.

## Limitations

- **Requires tier 5+ essences** (Screaming/Shrieking/Deafening) — the far more common lower tiers cannot reforge a rare at all.
- **Blocked entirely by meta-crafted mods.** Per the wiki: *"Essences cannot be used on an item if it has a meta-crafting mod (Ex. Prefixes Cannot Be Changed, Cannot roll Caster Modifiers). Using an Essence on these items will show an error message and do nothing."* This means essence-reforging has to happen **before** you lock anything in with a crafting-bench meta-mod, not after.
- Full reroll — wipes everything, so don't use once you have mods worth keeping.
- Only one mod is guaranteed; the rest is still random (even though uncapped).

## Data completeness

Verified against the PoE Wiki Essence page's §Crafting section and tier table (fetched 2026-07-30), including the meta-crafted-mod block, which is stated as a hard restriction (not a probability/weight effect) and is likely relevant to other reroll-style techniques in this repo too — worth revisiting generally once more categories are reviewed.
