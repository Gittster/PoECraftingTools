"""Worked example: recreating something like the Dire Stride boots.

This is a *simplified* representative target (four distinct mod tags), not a
byte-for-byte reproduction of the real item's exact affixes/tiers -- that
would require real mod-pool data (Phase 2). The point here is to exercise the
Phase 1 reverse-crafting engine end to end and show what its candidate chains
look like.

Run with: python3 examples/dire_stride_demo.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "engine"))

from models import ItemState, Mod, TargetSpec  # noqa: E402
from reverse_craft import describe_chain, recommend  # noqa: E402
from technique_loader import load_all_techniques  # noqa: E402


def main() -> None:
    techniques = load_all_techniques()

    start = ItemState(
        base_type="Warlock Boots",
        rarity="rare",
        item_level=84,
        influences=[],
        mods=[],  # blank rare base -- nothing crafted yet
    )

    target = TargetSpec(
        mods=[
            Mod("+# to maximum Energy Shield", "prefix", ["energy_shield_flat"], required=True),
            Mod("#% increased Energy Shield", "prefix", ["energy_shield_increased"], required=True),
            Mod("+#% to Fire/Cold/Lightning Resistances", "suffix", ["resistance"], required=True),
            Mod("#% increased Movement Speed", "suffix", ["speed"], required=True),
        ]
    )

    # 4 distinct target tags: a full reroll can only guarantee one of them,
    # so the worst-case chain needs one reroll plus up to three single-mod
    # add/remove-add steps -- max_depth needs enough room for that.
    chains = recommend(start, target, techniques, max_depth=5, max_results=5)

    print(f"Loaded {len(techniques)} techniques.\n")
    print(f"Target tags needed: {sorted(target.required_tags())}\n")

    if not chains:
        print("No candidate chains found within the search depth.")
        return

    for i, chain in enumerate(chains, 1):
        print(f"Candidate chain #{i} ({len(chain)} step(s)):")
        print(describe_chain(chain))
        print()


if __name__ == "__main__":
    main()
