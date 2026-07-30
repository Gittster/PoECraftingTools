---
id: eldritch-reroll-implicit
name: "Eldritch Currency: Reroll Eldritch Implicit"
category: eldritch
action: reroll_implicit
affects: [implicit]
mod_pool_tags: ["eldritch_exarch", "eldritch_eater"]
guarantee: biased
destructive: none
preconditions:
  rarity: [normal, magic, rare]
  influence: ["searing_exarch", "eater_of_worlds"]
  requires_open_affix: false
  requires_existing_mod_tag: ["eldritch_implicit_eligible"]
cost_tier: medium
inputs:
  - "Eldritch Ichor (Searing Exarch, any tier)"
  - "Eldritch Ember (Eater of Worlds, any tier)"
see_also:
  - harvest-augment-add-mod
---

## What it does

Eldritch Ichors (from the Searing Exarch) and Eldritch Embers (from the Eater of Worlds) reroll the item's **Eldritch implicit** modifier — a separate slot from prefixes/suffixes, unlocked once the item has been made eligible via the corresponding boss fight/altar mechanic.

- Prefixes and suffixes are **untouched** — this only affects the eldritch implicit slot.
- Higher currency tiers roll from a stronger pool of possible implicits for that influence (Exarch vs Eater), but which specific implicit you get within that tier is still random.
- Applying it again rerolls/upgrades the implicit again; it does not stack multiple implicits.

## Why you'd use it

The natural finishing step once prefixes/suffixes are locked in by other techniques (essence/fossil/harvest) — it adds a meaningfully powerful extra stat without touching or risking anything you already crafted. On something like the Dire Stride example, this is the kind of layer you'd add *after* getting energy shield/resistance/speed sorted via other means, not before.

## Limitations

- Requires the item to already be eldritch-eligible (touched by the relevant boss encounter) — it doesn't grant that eligibility itself.
- Ichor only works toward Exarch (fire-aligned) implicits; Ember only toward Eater (cold-aligned) implicits — you need the matching currency for the influence you want.
- The specific implicit rolled within the tier's pool is random, not chosen.

## Data completeness

Conceptual mechanic confirmed at a high level. Exact tier names, the full implicit pool per tier/influence, and eligibility mechanics still need to be pulled in from wiki data — treat the specifics here as provisional until verified.
