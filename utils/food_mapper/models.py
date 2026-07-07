from dataclasses import dataclass


@dataclass
class FoodMatch:
    input_name: str
    canonical_name: str | None
    confidence: float
    method: str        # alias | exact | fuzzy | unmatched