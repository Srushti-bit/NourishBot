import sqlite3

from utils.food_mapper import FoodResolver

DB_PATH = "database/nutrition.db"


class NutritionDB:

    def __init__(self):
        self.conn = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )
        self.cursor = self.conn.cursor()

        # Initialize the Food Resolver
        self.resolver = FoodResolver(DB_PATH)

    def exact_lookup(self, food_name):

        self.cursor.execute(
            """
            SELECT
                normalized_name,
                calories,
                protein,
                carbs,
                fat
            FROM foods
            WHERE LOWER(normalized_name)=?
            LIMIT 1
            """,
            (food_name.lower(),),
        )

        return self.cursor.fetchone()

    def get_food(self, food_name):

        # Resolve using FoodResolver
        match = self.resolver.resolve_food(food_name)

        if match.canonical_name is None:
            return None, match.method

        result = self.exact_lookup(match.canonical_name)

        if result:
            return result, match.method

        return None, "unmatched"


# Singleton database instance
db = NutritionDB()


def calculate_nutrition(food_list):

    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
    }

    print("\n========== MATCHED DATABASE ITEMS ==========")

    for food in food_list:

        result, method = db.get_food(food)

        if result is None:
            print(f"❌ {food} -> NOT FOUND ({method})")
            continue

        name, calories, protein, carbs, fat = result

        print(f"✅ {food} -> {name} ({method})")

        total["calories"] += calories or 0
        total["protein"] += protein or 0
        total["carbs"] += carbs or 0
        total["fat"] += fat or 0

    print("============================================\n")

    return total