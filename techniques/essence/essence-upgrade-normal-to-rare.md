---
id: essence-upgrade-normal-to-rare
name: "Essence: Upgrade Normal Item to Rare"
category: essence
action: reroll_all
affects: [prefix, suffix]
mod_pool_tags: ["depends-on-essence"]
guarantee: guaranteed
destructive: reroll_all
preconditions:
  rarity: [normal]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: low
inputs:
  - "Essence of <type>, any of the 7 natural tiers (Whispering through Deafening)"
see_also:
  - essence-reforge-rare
  - fossil-weighted-reforge
  - harvest-reforge-tag-biased
tags:
  - essence
  - action:reroll_all
  - guarantee:guaranteed
  - destructive:reroll_all
  - cost:low
---

# Essence: Upgrade Normal Item to Rare

## What it does

Source: [PoE Wiki – Essence, §Crafting](https://www.poewiki.net/wiki/Essence).

> "All essences can be used to upgrade a piece of normal rarity equipment to rare, similar to an Orb of Alchemy, and apply one guaranteed affix."

Applying any essence to a **normal (white)** item:

1. Upgrades it to rare.
2. Rolls a full set of rare-appropriate modifiers.
3. **Guarantees** one specific modifier fixed by the essence's type (e.g. an "Essence of Hatred" guarantees a cold-damage-family modifier), at whatever value the essence's tier grants.

This is the only essence interaction available on a normal item — essences do not apply to magic items at all, per the wiki's documented mechanics.

## The tier cap that changes the calculus

Essences come in 7 natural tiers (Whispering → Muttering → Weeping → Wailing → Screaming → Shrieking → Deafening). Higher tiers aren't just "bigger guaranteed roll" — **tiers 1-4 also cap how high the *other*, non-guaranteed modifiers can roll**, regardless of the item's actual item level:

| Tier | Max level for random (non-guaranteed) mods | Min. item level required |
|---|---|---|
| Whispering | 35 | 1 |
| Muttering | 45 | 8 |
| Weeping | 60 | 20 |
| Wailing | 75 | 33 |
| Screaming | uncapped | 46 |
| Shrieking | uncapped | 59 |
| Deafening | uncapped | 65 |

Tiers 5-7 (Screaming/Shrieking/Deafening) roll their non-guaranteed mods with **no level cap** — full access to the item's actual tier potential. Tiers 1-4 will always hand back weak secondary mods even on a high item-level base, because the cap applies regardless of the item's real item level.

## Why you'd use it (best-use-case takeaway)

- **Tier 5+ (Screaming/Shrieking/Deafening) is the real "kickstart a high-value rare" tool**: one guaranteed mod plus a real shot at 1-2 other high-tier mods, since nothing caps them. This is the tier range worth using as an opening move before layering Harvest/Eldritch/etc.
- **Tiers 1-4 are budget/leveling tools, not endgame kickstarters**: cheap and useful for guaranteeing a specific early mod on leveling gear, but the capped secondary mods mean they won't produce a strong base for high-item-level rares no matter how good the underlying base is.
- Since Deafening is obtainable only by upgrading (never a natural drop — see the wiki's tier table), Shrieking is usually the more readily farmable "no-cap" tier for repeated attempts.

## Limitations

- Only usable on normal-rarity items — has no effect on magic items, and rare items need the separate reforge interaction (see `essence-reforge-rare`), only available at tier 5+.
- Not usable on unique items.
- Only one mod is guaranteed; the rest (even uncapped at tier 5+) is still random.
- The corrupted-only essence family (Insanity/Horror/Hysteria/Delirium) is not covered by this entry — the source page's crafting table doesn't document their item-application rules, and that needs a dedicated look at those essences' own pages before writing it up.

## Data completeness

Verified against the PoE Wiki Essence page's §Crafting section and tier table (fetched 2026-07-30). Tier-cap table and rarity restriction are wiki-sourced. Corrupted-only essence mechanics remain unverified — do not treat any assumption about them as confirmed.
