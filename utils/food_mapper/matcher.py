# food_mapper/matcher.py

from rapidfuzz import process, fuzz
from .db_index import FoodDBIndex

DEFAULT_LIMIT = 5
DEFAULT_SCORE_CUTOFF = 60


class FoodMatcher:
    """
    Generates fuzzy match candidates from the database index.

    This class is responsible only for finding similar food names.
    It does not select the best match or perform validation.
    """

    def __init__(self, db_index: FoodDBIndex):
        """
        Initialize the matcher with all normalized food names.

        Args:
            db_index: Food database index containing normalized food names.
        """
        self._names = [
            name
            for name in db_index.all_food_names()
            if name
        ]

    def get_candidates(
        self,
        query: str,
        limit: int = DEFAULT_LIMIT,
        score_cutoff: int = DEFAULT_SCORE_CUTOFF,
    ) -> list[tuple[str, float]]:
        """
        Generate fuzzy match candidates for a food query.

        Args:
            query: Food name to search for.
            limit: Maximum number of candidates to return.
            score_cutoff: Minimum similarity score (0-100).

        Returns:
            A list of tuples in the form:
            (food_name, similarity_score)
        """

        # Ignore empty or whitespace-only queries.
        if not query or not query.strip():
            return []

        # Normalize the input query.
        query = query.strip().lower()

        # Perform fuzzy matching.
        results = process.extract(
            query,
            self._names,
            scorer=fuzz.WRatio,
            limit=limit,
        )

        # Keep only candidates above the similarity threshold.
        candidates = [
            (name, score)
            for name, score, _ in results
            if score >= score_cutoff
        ]

        return candidates