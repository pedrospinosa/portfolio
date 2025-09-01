from __future__ import annotations

import math
from collections import Counter
from typing import Any


def flatten_grouped_skills(skills_section: list[object]) -> list[dict[str, object]]:
    """Validate and flatten grouped skills into a flat list of skill dicts.

    Expected input items: {"category": str, "values": list[str], "priority"?: int}
    Returns items: {"name": str, "category": str, "priority"?: int}
    """
    if not isinstance(skills_section, list):
        raise ValueError("skills must be a list of groups")

    flattened_skills: list[dict[str, object]] = []
    for group in skills_section:
        if not isinstance(group, dict):
            raise ValueError("each skills item must be a mapping with 'category' and 'values'")
        category = group.get("category")
        values = group.get("values")
        priority = group.get("priority", None)

        if not isinstance(category, str) or not category:
            raise ValueError("skills group missing valid 'category'")
        if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
            raise ValueError("skills group 'values' must be a non-empty list of strings")
        if priority is not None and not isinstance(priority, int):
            raise ValueError("skills group 'priority' must be an integer if provided")

        for name in values:
            skill_dict: dict[str, object] = {"name": name, "category": category}
            if priority is not None:
                skill_dict["priority"] = priority
            flattened_skills.append(skill_dict)

    return flattened_skills


def process_skills(skills_section: object) -> list[dict[str, object]]:
    """Validate top-level skills section and return flattened skills list.

    Enforces grouped-only format and forbids mixing with flat items.
    """
    if not isinstance(skills_section, list):
        raise ValueError("skills must be a list of groups")

    if len(skills_section) == 0:
        return []

    has_values_key = any(isinstance(it, dict) and "values" in it for it in skills_section)
    has_flat_items = any(isinstance(it, dict) and "name" in it for it in skills_section)

    if not has_values_key:
        raise ValueError(
            "skills must use grouped format: each item must include 'category' and 'values'"
        )
    if has_flat_items:
        raise ValueError("skills must not mix grouped and flat formats; grouped format is required")

    return flatten_grouped_skills(skills_section)


def sort_skills(skills: list[Any]) -> list[Any]:
    """Return a new list of skills sorted by category min priority (asc),
    then category count (desc), then name (asc, case-insensitive).

    Assumes each item has attributes: category, name, priority (int|None).
    """
    if not skills:
        return []

    category_counts: Counter[str] = Counter(s.category for s in skills)
    category_priority: dict[str, int] = {}
    for s in skills:
        prio = s.priority
        if prio is None:
            continue
        current = category_priority.get(s.category)
        if current is None or prio < current:
            category_priority[s.category] = prio

    return sorted(
        skills,
        key=lambda s: (
            category_priority.get(s.category, math.inf),
            -category_counts.get(s.category, 0),
            s.name.lower(),
        ),
    )
