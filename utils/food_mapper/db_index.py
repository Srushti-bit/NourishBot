import sqlite3
from typing import List, Dict


class FoodDBIndex:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._foods: List[Dict] = []
        self._name_to_row: Dict[str, Dict] = {}

    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM foods")
        rows = cursor.fetchall()

        col_names = [desc[0] for desc in cursor.description]
        conn.close()

        for r in rows:
            row = dict(zip(col_names, r))
            self._foods.append(row)

            name = (
                row.get("normalized_name")
                or row.get("food_name")
                or row.get("name")
            )

            if name:
                self._name_to_row[name.lower()] = row

    # -----------------------------
    # FIXED METHOD (correct indentation)
    # -----------------------------
    def get_by_exact_name(self, name: str):
        row = self._name_to_row.get(name.lower())

        if row:
            row["normalized_name"] = self.normalize_name_preference(
                row.get("normalized_name", "")
            )
            return row

        return None

    def all_food_names(self) -> List[str]:
        return [
            r.get("normalized_name")
            or r.get("food_name")
            or r.get("name")
            for r in self._foods
            if r
        ]

    # -----------------------------
    # Canonical preference rule
    # -----------------------------
    def normalize_name_preference(self, name: str) -> str:
        name_lower = name.lower()

        # prefer cooked over raw
        if "white rice raw" in name_lower:
            return "white rice cooked"

        return name