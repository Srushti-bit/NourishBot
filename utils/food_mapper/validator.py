# food_mapper/validator.py

from food_mapper.aliases import UNRESOLVED, GENERIC_DEFAULTS


def validate_aliases(db_index):
    """
    Validates alias mappings against the loaded database index.

    Rules:
    - UNRESOLVED is allowed
    - None is NOT allowed (accidental bug)
    - All string mappings must exist in DB normalized_name set
    """

    errors = []

    # build DB lookup set once
    db_names = {
        name.lower()
        for name in db_index.all_food_names()
        if name is not None
    }

    for key, canonical in GENERIC_DEFAULTS.items():

        # 1. accidental None catch
        if canonical is None:
            errors.append(f"[ALIASES] '{key}' mapped to None (use UNRESOLVED instead)")
            continue

        # 2. explicitly unresolved is fine
        if canonical is UNRESOLVED:
            continue

        # 3. must exist in DB
        if canonical.lower() not in db_names:
            errors.append(
                f"[ALIASES] '{key}' → '{canonical}' not found in database"
            )

    if errors:
        raise RuntimeError("\n".join(errors))