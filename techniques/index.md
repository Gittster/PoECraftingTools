# PoE Crafting Techniques

A tagged repository of Path of Exile crafting techniques: what each one does, when to use it, and what it costs. Structured so it can also feed a reverse-crafting recommender.

Every entry explains the mechanic, when you'd choose it over alternatives, and its limitations. Browse by category below, or use the [tag index](tags.md) to filter by action type, guarantee strength, or cost.

## Categories

- **[Essence](essence/essence.md)**: guarantee one specific modifier while rerolling everything else.
- **[Fossil](fossil/fossil-weighted-reforge.md)**: reroll everything with weights biased toward (or away from) chosen mod themes.
- **Harvest**: the most surgical tools available.
  - [Reforge with a guaranteed tag](harvest/harvest-reforge-tag-biased.md)
  - [Augment: add a new tagged mod](harvest/harvest-augment-add-mod.md) (needs an open affix slot)
  - [Remove a random mod, add a new tagged mod](harvest/harvest-remove-add.md) (works even when full)
- **[Eldritch currency](eldritch/eldritch-reroll-implicit.md)**: reroll the Eldritch implicit slot without touching prefixes/suffixes.

## How this fits together

This site is the human-readable half of the [PoECraftingTools](https://github.com/Gittster/PoECraftingTools) repository. Each technique page here is generated from the same file that feeds a rule-based reverse-crafting engine. Given a target item and a starting item, it searches for technique sequences that could get you there. That engine currently runs locally (see the repo's `examples/dire_stride_demo.py`), it isn't wired into this site yet.

Real mod-weight/tier data would let chains get ranked by actual expected cost instead of just relevance. See the repo README for the roadmap.
