"""Phase 1 reverse-crafting search: rule-based candidate chain generation.

Given a starting ItemState and a TargetSpec, this searches for sequences of
Techniques that plausibly get from one to the other. It has NO real
probability model -- every technique that guarantees or is biased toward a
tag is simulated as succeeding at that tag in the best case. That's enough to
answer "which techniques/orderings are even relevant here", which is the
useful question before real mod-weight data (Phase 2) lets us rank chains by
true expected cost. See README.md for the phase split.
"""

from __future__ import annotations

from dataclasses import dataclass

from models import ItemState, Mod, Technique, TargetSpec

COST_ORDER = {"low": 1, "medium": 2, "high": 3}

# mod_pool_tags values that mean "the crafter picks the specific tag when they
# use this technique" (e.g. which essence, which harvest tag) rather than a
# fixed tag baked into the technique itself.
PARAMETERIZED_MARKERS = {
    "depends-on-essence",
    "depends-on-fossil-combo",
    "chosen-at-craft-time",
}


@dataclass
class Step:
    technique: Technique
    chosen_tag: str | None
    notes: list[str]


def is_parameterized(t: Technique) -> bool:
    return any(tag in PARAMETERIZED_MARKERS for tag in t.mod_pool_tags)


def relevant_tags(t: Technique, needed_tags: set[str]) -> set[str]:
    if t.targets_any() or is_parameterized(t):
        return set(needed_tags)
    return set(t.mod_pool_tags) & set(needed_tags)


def applicable(t: Technique, state: ItemState) -> bool:
    if state.rarity not in t.preconditions.rarity:
        return False
    if t.preconditions.influence and not any(
        i in state.influences for i in t.preconditions.influence
    ):
        return False
    if t.preconditions.requires_open_affix:
        affix_slots = [s for s in t.affects if s in ("prefix", "suffix")]
        if not any(state.has_open_affix(s) for s in affix_slots):
            return False
    if t.preconditions.requires_existing_mod_tag:
        if not all(state.has_tag(tag) for tag in t.preconditions.requires_existing_mod_tag):
            return False
    if t.destructive == "reroll_all" and not state.is_blank():
        # Never recommend wiping mods you already crafted.
        return False
    return True


def missing_tags(state: ItemState, target: TargetSpec) -> set[str]:
    required = target.required_tags()
    return {tag for tag in required if not state.has_tag(tag)}


def apply_optimistic(t: Technique, state: ItemState, needed_tags: set[str]) -> tuple[ItemState, str | None, list[str]]:
    new_state = state.clone()
    pool = relevant_tags(t, needed_tags)
    chosen_tag = sorted(pool)[0] if pool else None
    notes: list[str] = []

    if t.destructive == "reroll_all":
        new_state.mods = [m for m in new_state.mods if m.slot == "implicit"]
        if chosen_tag:
            new_state.mods.append(Mod(f"<{chosen_tag} mod, via {t.name}>", "prefix", [chosen_tag], True))
        notes.append(
            "Optimistic best case: assumes the rest of the reroll also lands "
            "acceptable mods, which this rule-based model does not check."
        )
    elif t.destructive == "remove_one":
        removable = [
            m for m in new_state.mods
            if m.slot in ("prefix", "suffix") and not needed_tags.intersection(m.tags)
        ]
        if removable:
            new_state.mods.remove(removable[0])
        else:
            notes.append(
                "Risk: this craft removes a RANDOM existing mod -- it could "
                "destroy one you need to keep."
            )
        if chosen_tag:
            slot = "prefix" if new_state.has_open_affix("prefix") else "suffix"
            new_state.mods.append(Mod(f"<{chosen_tag} mod, via {t.name}>", slot, [chosen_tag], True))
    elif t.action == "add_mod":
        slot = next((s for s in t.affects if s in ("prefix", "suffix") and new_state.has_open_affix(s)), None)
        if chosen_tag and slot:
            new_state.mods.append(Mod(f"<{chosen_tag} mod, via {t.name}>", slot, [chosen_tag], True))
    elif t.action == "reroll_implicit":
        new_state.mods = [m for m in new_state.mods if m.slot != "implicit"]
        if chosen_tag:
            new_state.mods.append(Mod(f"<{chosen_tag} implicit, via {t.name}>", "implicit", [chosen_tag], True))

    return new_state, chosen_tag, notes


def recommend(
    start: ItemState,
    target: TargetSpec,
    techniques: list[Technique],
    max_depth: int = 3,
    max_results: int = 5,
) -> list[list[Step]]:
    results: list[list[Step]] = []

    def recurse(state: ItemState, chain: list[Step], depth: int) -> None:
        missing = missing_tags(state, target)
        if not missing:
            results.append(list(chain))
            return
        if depth >= max_depth:
            return
        for t in techniques:
            if not applicable(t, state):
                continue
            rel = relevant_tags(t, missing)
            if not rel:
                continue
            new_state, chosen_tag, notes = apply_optimistic(t, state, missing)
            if chosen_tag is None:
                continue
            chain.append(Step(t, chosen_tag, notes))
            recurse(new_state, chain, depth + 1)
            chain.pop()

    recurse(start, [], 0)

    def score(chain: list[Step]) -> tuple[int, int]:
        return (len(chain), sum(COST_ORDER[s.technique.cost_tier] for s in chain))

    results.sort(key=score)
    return results[:max_results]


def describe_chain(chain: list[Step]) -> str:
    lines = []
    for i, step in enumerate(chain, 1):
        line = f"  {i}. {step.technique.name} -> targeting '{step.chosen_tag}' ({step.technique.cost_tier} cost)"
        lines.append(line)
        for note in step.notes:
            lines.append(f"     note: {note}")
    return "\n".join(lines)
