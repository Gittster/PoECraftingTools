"""Builds the essence reference table used by the docs site.

Reads the vendored data/repoe/essences.json snapshot and writes a small,
front-end-friendly JSON file into the mkdocs docs_dir so the site can fetch
and render it client-side. Re-run this after refreshing data/repoe/essences.json.
"""

from __future__ import annotations

import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
SOURCE = os.path.join(ROOT, "data", "repoe", "essences.json")
OUTPUT = os.path.join(ROOT, "techniques", "essence", "essences-data.json")

# The power tier (Whispering=1 ... Deafening=7) is encoded in the name
# prefix, not in the raw type.tier field. That field is actually the
# essence type-group (matches the wiki's Group A-E columns), which is a
# different axis entirely and would mislabel things if shown as "tier".
TIER_BY_PREFIX = {
    "Whispering": 1,
    "Muttering": 2,
    "Weeping": 3,
    "Wailing": 4,
    "Screaming": 5,
    "Shrieking": 6,
    "Deafening": 7,
}


def power_tier(name: str) -> int | None:
    for prefix, tier in TIER_BY_PREFIX.items():
        if name.startswith(prefix):
            return tier
    return None  # corruption-only essences and Essence of Desolation have no power tier prefix


def humanize_mod_id(mod_id: str) -> str:
    """Light cosmetic cleanup of an internal mod id, not an authoritative name."""
    base = mod_id.rstrip("_")
    base = re.sub(r"(\d+)$", r" (\1)", base)
    words = re.findall(r"[A-Z][a-z0-9]*|[a-z0-9()]+", base)
    return " ".join(words).strip()


def main() -> None:
    with open(SOURCE, encoding="utf-8") as f:
        raw = json.load(f)

    entries = []
    for value in raw.values():
        if value["name"] == "Remnant of Corruption":
            continue  # not an essence, a separate currency used in corruption
        entries.append(
            {
                "name": value["name"],
                "tier": power_tier(value["name"]),
                "corruption_only": value["type"]["is_corruption_only"],
                "item_level_cap": value.get("item_level_restriction"),
                "mods": {
                    item_class: humanize_mod_id(mod_id)
                    for item_class, mod_id in value["mods"].items()
                },
            }
        )

    def family(name: str) -> str:
        return name.split(" of ", 1)[-1] if " of " in name else name

    entries.sort(key=lambda e: (family(e["name"]), e["tier"] or 0))

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
        f.write("\n")

    print(f"Wrote {len(entries)} essence entries to {OUTPUT}")


if __name__ == "__main__":
    main()
