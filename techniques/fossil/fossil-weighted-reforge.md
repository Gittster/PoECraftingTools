---
id: fossil-weighted-reforge
name: "Fossil: Weighted Reforge"
category: fossil
action: reroll_all
affects: [prefix, suffix]
mod_pool_tags: ["depends-on-fossil-combo"]
guarantee: biased
destructive: reroll_all
preconditions:
  rarity: [normal, magic, rare]
  influence: []
  requires_open_affix: false
  requires_existing_mod_tag: []
cost_tier: medium
inputs:
  - "Resonator (Primitive/Potent/Prime/Powerful, matching socket count to fossils used)"
  - "1-4 Fossils (e.g. Pristine, Dense, Serrated, ...)"
see_also:
  - essence
  - harvest-reforge-tag-biased
tags:
  - fossil
  - action:reroll_all
  - guarantee:biased
  - destructive:reroll_all
  - cost:medium
---

# Fossil: Weighted Reforge

## What it does

Socket 1-4 fossils into a matching resonator, then apply the resonator+fossils combo to a normal, magic, or rare item like a currency item:

1. Removes **all** existing modifiers.
2. Rerolls a fresh set of modifiers, but with weights adjusted by the socketed fossils — some mod tags become much more likely, others are suppressed or blocked outright, and some fossils add side effects (forced corrupted outcome, extra explicit slot, reduced attribute requirements, etc.).
3. Rarity stays whatever it was (a rare stays rare); item level and base type are untouched.

Unlike essences, nothing is *guaranteed* — fossils only bias the odds. Combining fossils multiplies/stacks their effects (both the tags they favor and the tags they suppress), so the right combo can make a specific outcome (e.g. "energy shield + resistances, no physical/attack mods") land much more often than a plain reroll would.

## Worked example: Pristine Fossil

Pristine Fossil biases toward energy shield modifiers and excludes physical/attack-oriented ones. On an energy-shield base (like the Warlock Boots in the Dire Stride example), a Pristine-biased reforge is a reasonable way to fish for a strong flat/percent ES roll before layering on more targeted techniques for the remaining slots.

## Why you'd use it

Best used when you want a *biased* full reroll rather than a *guaranteed* one — e.g. you need good rolls across several mods of a similar theme (all defensive, all energy-shield-adjacent) rather than one single guaranteed mod. Also useful to suppress tags you actively don't want appearing (e.g. blocking physical damage rolls on a caster item).

## Limitations

- Wipes the entire item, same as essences — don't use once you have mods worth keeping.
- Nothing is guaranteed; a bad combo of fossils can still whiff.
- Fossil availability/combos are themselves a resource-management problem (found via Delve), which affects real-world cost more than the currency-tier fields here currently capture.

## Data completeness

Conceptual mechanic confirmed. Exact weight multipliers per fossil, the full fossil-to-tag table, and resonator socket/rarity requirements still need to be pulled in from wiki/RePoE data.
