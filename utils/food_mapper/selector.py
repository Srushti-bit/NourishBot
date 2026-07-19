from typing import Optional

RAW_PENALTY = 3.0
COOKED_BONUS = 2.0
LONG_NAME_PENALTY = 2.0
MAX_NAME_WORDS = 6
DEFAULT_THRESHOLD = 85.0


class FoodSelector:
    """
    Selects the best food candidate from a list of fuzzy matches.

    The selector applies domain-specific scoring rules to improve
    match quality after fuzzy matching.
    """

    def __init__(self, threshold: float = DEFAULT_THRESHOLD):
        self.threshold = threshold

    def _adjust_score(self, food_name: str, score: float) -> float:
        """
        Apply domain-specific score adjustments.

        Args:
            food_name: Candidate food name.
            score: Original fuzzy similarity score.

        Returns:
            Adjusted similarity score.
        """
        adjusted_score = score
        tokens = food_name.lower().split()

        # Prefer cooked foods over raw foods.
        if "raw" in tokens:
            adjusted_score -= RAW_PENALTY

        if "cooked" in tokens:
            adjusted_score += COOKED_BONUS

        # Penalize unusually long food names.
        if len(tokens) > MAX_NAME_WORDS:
            adjusted_score -= LONG_NAME_PENALTY

        return adjusted_score

    def select_best(
        self,
        candidates: list[tuple[str, float]]
    ) -> Optional[tuple[str, float]]:
        """
        Select the highest-ranked food candidate.

        Args:
            candidates: List of (food_name, similarity_score).

        Returns:
            Best candidate after score adjustment,
            or None if no candidate passes the threshold.
        """
        if not candidates:
            return None

        best_candidate = None
        highest_score = float("-inf")

        for food_name, score in candidates:
            adjusted_score = self._adjust_score(food_name, score)

            if adjusted_score > highest_score:
                highest_score = adjusted_score
                best_candidate = (food_name, adjusted_score)

        if highest_score < self.threshold:
            return None

        return best_candidate