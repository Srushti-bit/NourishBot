from typing import List, Tuple, Optional


class FoodSelector:
    def __init__(self, threshold: float = 85.0):
        self.threshold = threshold

    def select_best(self, candidates: List[Tuple[str, float]]) -> Optional[Tuple[str, float]]:
        if not candidates:
            return None

        best_name, best_score = candidates[0]

        name_lower = best_name.lower()

        # -----------------------------
        # DOMAIN BIAS: cooked is preferred over raw
        # -----------------------------
        if "raw" in name_lower:
            best_score -= 3.0

        if "cooked" in name_lower:
            best_score += 2.0

        # -----------------------------
        # EXTRA SAFETY: avoid noisy long entries
        # -----------------------------
        if len(best_name.split()) > 6:
            best_score -= 2.0

        if best_score < self.threshold:
            return None

        return best_name, best_score