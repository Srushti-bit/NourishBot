import sqlite3
from typing import Optional


class FoodDBIndex:
    """
    In-memory index for fast food lookups.

    Loads the food database once and provides efficient
    exact-name lookups and food name retrieval.
    """

    def __init__(self, db_path: str):
        """
        Initialize the food database index.

        Args:
            db_path: Path to the SQLite database.
        """
        self.db_path = db_path
        self._foods: list[dict] = []
        self._name_to_row: dict[str, dict] = {}

    def load(self) -> None:
        """
        Load all food records into memory.
        """

        self._foods.clear()
        self._name_to_row.clear()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM foods")
            rows = cursor.fetchall()

            column_names = [column[0] for column in cursor.description]

        for row_values in rows:
            row = dict(zip(column_names, row_values))

            self._foods.append(row)

            food_name = (
                row.get("normalized_name")
                or row.get("food_name")
                or row.get("name")
            )

            if food_name:
                self._name_to_row[food_name.lower()] = row

    def get_by_exact_name(self, name: str) -> Optional[dict]:
        """
        Retrieve a food by its normalized name.

        Args:
            name: Food name to search.

        Returns:
            Matching database row or None.
        """

        if not name:
            return None

        row = self._name_to_row.get(name.lower())

        if row is None:
            return None

        # Return a copy to avoid modifying cached data.
        result = row.copy()

        result["normalized_name"] = self.normalize_name_preference(
            result.get("normalized_name", "")
        )

        return result

    def all_food_names(self) -> list[str]:
        """
        Return all searchable food names.
        """

        return [
            row.get("normalized_name")
            or row.get("food_name")
            or row.get("name")
            for row in self._foods
            if row
        ]

    @staticmethod
    def normalize_name_preference(name: str) -> str:
        """
        Apply project-specific canonical naming rules.

        Example:
            'white rice raw' -> 'white rice cooked'
        """

        if not name:
            return ""

        name_lower = name.lower()

        if name_lower == "white rice raw":
            return "white rice cooked"

        return name