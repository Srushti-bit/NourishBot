from typing import Optional

from .aliases import GENERIC_DEFAULTS, UNRESOLVED
from .db_index import FoodDBIndex
from .matcher import FoodMatcher
from .selector import FoodSelector

# Type alias for better readability
FoodRow = dict[str, object]


class FoodResolver:
    """
    Resolves user-provided food names into canonical database records.

    Resolution Pipeline:
        1. Exact database lookup
        2. Alias lookup
        3. Fuzzy matching
        4. Candidate selection
    """

    def __init__(self, db_path: str):
        """
        Initialize all resolver components.

        Args:
            db_path: Path to the nutrition SQLite database.
        """
        self.db = FoodDBIndex(db_path)
        self.db.load()

        self.matcher = FoodMatcher(self.db)
        self.selector = FoodSelector()

    def resolve(self, query: str) -> Optional[FoodRow]:
        """
        Resolve a food query into its database record.

        Args:
            query: User-provided food name.

        Returns:
            Database row if successfully resolved, otherwise None.
        """
        if not query or not query.strip():
            return None

        query = query.strip().lower()

        # Step 1: Exact database lookup
        row = self._exact_lookup(query)
        if row:
            return row

        # Step 2: Alias lookup
        row = self._alias_lookup(query)
        if row:
            return row

        # Step 3: Fuzzy lookup
        return self._fuzzy_lookup(query)

    def _exact_lookup(self, query: str) -> Optional[FoodRow]:
        """
        Perform an exact database lookup.
        """
        return self.db.get_by_exact_name(query)

    def _alias_lookup(self, query: str) -> Optional[FoodRow]:
        """
        Resolve the query using predefined aliases.
        """
        alias = GENERIC_DEFAULTS.get(query)

        if alias is UNRESOLVED:
            return None

        if alias:
            return self.db.get_by_exact_name(alias)

        return None

    def _fuzzy_lookup(self, query: str) -> Optional[FoodRow]:
        """
        Resolve the query using fuzzy matching.
        """
        candidates = self.matcher.get_candidates(query)

        selected = self.selector.select_best(candidates)

        if selected is None:
            return None

        food_name, _ = selected

        return self.db.get_by_exact_name(food_name)