# food_mapper/matcher.py

from rapidfuzz import process, fuzz
from typing import List, Tuple


class FoodMatcher:
    """
    Generates fuzzy match candidates from DB index.
    Does NOT choose the final match.
    """

    def __init__(self, db_index):
        self.db_index = db_index
        self._names = [
            name for name in db_index.all_food_names()
            if name is not None
        ]

    def get_candidates(
        self,
        query: str,
        limit: int = 5,
        score_cutoff: int = 60
    ) -> List[Tuple[str, float]]:
        """
        Returns:
            List of (normalized_name, score)
        """

        if not query:
            return []

        results = process.extract(
            query,
            self._names,
            scorer=fuzz.WRatio,
            limit=limit
        )

        # filter + normalize output
        candidates = [
            (name, score)
            for name, score, _ in results
            if score >= score_cutoff
        ]

        return candidates