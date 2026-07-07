from typing import Optional, Union

UNRESOLVED = object()

GENERIC_DEFAULTS = {
    "rice": "white rice cooked",
    "white rice": "white rice cooked",

    "chicken": "chicken breast cooked",
    "egg": "egg boiled",
    "banana": "banana",
    "broccoli": "broccoli raw",

    "milk": UNRESOLVED,
}

CANONICAL_OVERRIDES = {
    "white rice raw": "white rice cooked",
    "raw white rice": "white rice cooked",
}


def alias_lookup(food: str) -> Optional[Union[str, object]]:
    """
    Returns:
        str         -> canonical alias
        UNRESOLVED  -> intentionally unresolved
        None        -> no alias exists
    """
    return GENERIC_DEFAULTS.get(food.lower().strip())