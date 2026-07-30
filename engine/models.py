"""Core data model for items and techniques.

Kept deliberately small: this is the Phase 1 (rule-based) model. It has no
notion of real probabilities or mod weights -- those belong to Phase 2 once
real mod-pool data (e.g. from RePoE) is wired in. See README.md.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Mod:
    """A single modifier on an item, or a single desired modifier in a target."""

    text: str
    slot: str  # "prefix" | "suffix" | "implicit"
    tags: list[str] = field(default_factory=list)
    required: bool = True  # only meaningful on TargetSpec mods


@dataclass
class ItemState:
    """The current state of the item being crafted."""

    base_type: str
    rarity: str  # "normal" | "magic" | "rare"
    item_level: int
    influences: list[str] = field(default_factory=list)
    mods: list[Mod] = field(default_factory=list)
    max_prefixes: int = 3
    max_suffixes: int = 3

    def count(self, slot: str) -> int:
        return sum(1 for m in self.mods if m.slot == slot)

    def has_open_affix(self, slot: str) -> bool:
        if slot == "prefix":
            return self.count("prefix") < self.max_prefixes
        if slot == "suffix":
            return self.count("suffix") < self.max_suffixes
        return True  # implicits aren't capacity-limited here

    def has_tag(self, tag: str) -> bool:
        return any(tag in m.tags for m in self.mods)

    def is_blank(self) -> bool:
        """True if the item has no crafted prefix/suffix mods yet (implicits aside)."""
        return not any(m.slot in ("prefix", "suffix") for m in self.mods)

    def clone(self) -> "ItemState":
        return ItemState(
            base_type=self.base_type,
            rarity=self.rarity,
            item_level=self.item_level,
            influences=list(self.influences),
            mods=[Mod(m.text, m.slot, list(m.tags), m.required) for m in self.mods],
            max_prefixes=self.max_prefixes,
            max_suffixes=self.max_suffixes,
        )


@dataclass
class TargetSpec:
    """What you're trying to end up with."""

    mods: list[Mod]

    def required_tags(self) -> set[str]:
        tags: set[str] = set()
        for m in self.mods:
            if m.required:
                tags.update(m.tags)
        return tags


@dataclass
class Preconditions:
    rarity: list[str]
    influence: list[str] = field(default_factory=list)
    requires_open_affix: bool = False
    requires_existing_mod_tag: list[str] = field(default_factory=list)


@dataclass
class Technique:
    id: str
    name: str
    category: str
    action: str
    affects: list[str]
    mod_pool_tags: list[str]
    guarantee: str  # "guaranteed" | "biased" | "none"
    destructive: str  # "none" | "remove_one" | "reroll_all"
    preconditions: Preconditions
    cost_tier: str  # "low" | "medium" | "high"
    inputs: list[str] = field(default_factory=list)
    see_also: list[str] = field(default_factory=list)
    body: str = ""
    source_path: str = ""

    def targets_any(self) -> bool:
        return "any" in self.mod_pool_tags
