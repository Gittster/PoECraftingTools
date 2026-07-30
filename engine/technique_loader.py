"""Loads Technique objects out of techniques/**/*.md frontmatter."""

from __future__ import annotations

import glob
import os

import yaml

from models import Preconditions, Technique

FRONTMATTER_DELIM = "---"


def _split_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        raise ValueError("technique file missing opening '---' frontmatter delimiter")
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_DELIM:
            frontmatter_text = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1 :]).strip()
            return yaml.safe_load(frontmatter_text) or {}, body
    raise ValueError("technique file missing closing '---' frontmatter delimiter")


def load_technique(path: str) -> Technique:
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    fm, body = _split_frontmatter(raw)

    pre = fm.get("preconditions", {}) or {}
    preconditions = Preconditions(
        rarity=pre.get("rarity", []),
        influence=pre.get("influence", []),
        requires_open_affix=pre.get("requires_open_affix", False),
        requires_existing_mod_tag=pre.get("requires_existing_mod_tag", []),
    )

    return Technique(
        id=fm["id"],
        name=fm["name"],
        category=fm["category"],
        action=fm["action"],
        affects=fm.get("affects", []),
        mod_pool_tags=fm.get("mod_pool_tags", []),
        guarantee=fm["guarantee"],
        destructive=fm["destructive"],
        preconditions=preconditions,
        cost_tier=fm["cost_tier"],
        inputs=fm.get("inputs", []),
        see_also=fm.get("see_also", []),
        body=body,
        source_path=path,
    )


def load_all_techniques(root: str | None = None) -> list[Technique]:
    if root is None:
        root = os.path.join(os.path.dirname(__file__), "..", "techniques")
    # Only category subdirectories (techniques/<category>/*.md) hold technique
    # files. Top-level pages like index.md/tags.md are site content, not
    # techniques, and don't have technique frontmatter.
    paths = sorted(glob.glob(os.path.join(root, "*", "*.md")))
    return [load_technique(p) for p in paths]
