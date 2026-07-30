# PoE Crafting Techniques

A tagged, explained repository of Path of Exile crafting techniques — what each one does, when to reach for it, and what it costs, structured so it can also feed a reverse-crafting recommender.

This isn't just a data dump: every entry explains the mechanic in plain language, why you'd choose it over alternatives, and its limitations. Browse by category below, or jump to the [tag index](tags.md) to filter by action type, guarantee strength, or cost.

## Categories

- **Essence** — guarantee one specific modifier while rerolling everything else:
  - [Upgrade a normal item to rare](essence/essence-upgrade-normal-to-rare.md) (any tier)
  - [Reforge an existing rare](essence/essence-reforge-rare.md) (tier 5+ only)
- **[Fossil](fossil/fossil-weighted-reforge.md)** — reroll everything with weights biased toward (or away from) chosen mod themes.
- **Harvest** — the most surgical tools available:
  - [Reforge with a guaranteed tag](harvest/harvest-reforge-tag-biased.md)
  - [Augment: add a new tagged mod](harvest/harvest-augment-add-mod.md) (needs an open affix slot)
  - [Remove a random mod, add a new tagged mod](harvest/harvest-remove-add.md) (works even when full)
- **[Eldritch currency](eldritch/eldritch-reroll-implicit.md)** — reroll the Eldritch implicit slot without touching prefixes/suffixes.

## How this fits together

This site is the human-readable half of the [PoECraftingTools](https://github.com/Gittster/PoECraftingTools) repository. Each technique page you're browsing is generated from the exact same file that feeds a rule-based reverse-crafting engine — given a target item and a starting item, it searches for technique sequences that could plausibly get you there. That engine currently runs locally (see the repo's `examples/dire_stride_demo.py`); it isn't wired into this site yet.

**Where this is headed:** real mod-weight/tier data (from community sources like RePoE) to rank chains by true expected cost, and an interactive version of the recommender running right on this page. See the repo README for the full roadmap.
