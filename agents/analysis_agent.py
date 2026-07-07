from utils.nutrition_db import calculate_nutrition


def analyze_meal(food_items):

    nutrients = calculate_nutrition(food_items)

    report = f"""
========== NUTRITION REPORT ==========

Detected Foods:
{", ".join(food_items)}

Calories: {nutrients['calories']} kcal
Protein : {nutrients['protein']} g
Carbs   : {nutrients['carbs']} g
Fat     : {nutrients['fat']} g

======================================
"""

    return report