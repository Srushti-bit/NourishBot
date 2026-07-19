"""
Validation utilities for Food Resolver aliases.

Ensures that all alias mappings are valid before the resolver is used.
"""

from .aliases import GENERIC_DEFAULTS, UNRESOLVED
from .db_index import FoodDBIndex


def validate_aliases(db_index: FoodDBIndex) -> None:
    """
    Validate alias mappings against the loaded database index.

    Validation rules:
    - UNRESOLVED is allowed.
    - None is not allowed (use UNRESOLVED instead).
    - Every string alias must exist in the database.

    Args:
        db_index: Loaded food database index.

    Raises:
        RuntimeError:
            If one or more invalid alias mappings are found.
    """

    errors: list[str] = []

    # Build a set for fast O(1) lookups.
    db_names = {
        name.lower()
        for name in db_index.all_food_names()
        if name
    }

    for alias, canonical_name in GENERIC_DEFAULTS.items():

        # None indicates an accidental programming error.
        if canonical_name is None:
            errors.append(
                f"[ALIASES] '{alias}' maps to None. "
                "Use UNRESOLVED instead."
            )
            continue

        # Explicitly unresolved aliases are allowed.
        if canonical_name is UNRESOLVED:
            continue

        # Canonical food must exist in the database.
        if canonical_name.lower() not in db_names:
            errors.append(
                f"[ALIASES] '{alias}' -> "
                f"'{canonical_name}' does not exist in the database."
            )

    if errors:
        raise RuntimeError(
            "Alias validation failed:\n\n" + "\n".join(errors)
        )