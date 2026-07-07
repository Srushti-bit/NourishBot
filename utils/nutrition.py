import json
from pathlib import Path

# Get absolute path to nutrition database
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "nutrition_db.json"

with open(DB_PATH, "r") as file:
    nutrition_db = json.load(file)


def calculate_nutrition(food_items):
    """
    Calculate total nutrition values for detected food items.
    """

    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    for item in food_items:

        item = item.lower()

        if item in nutrition_db:

            totals["calories"] += nutrition_db[item]["calories"]
            totals["protein"] += nutrition_db[item]["protein"]
            totals["carbs"] += nutrition_db[item]["carbs"]
            totals["fat"] += nutrition_db[item]["fat"]

    return totals