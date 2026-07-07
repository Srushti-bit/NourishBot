from utils.dietary_filter import filter_ingredients


def generate_recipe(food_items, diet):

    filtered_items = filter_ingredients(
        food_items,
        diet
    )

    recipe = f"""
========== RECIPE ==========

Recipe Name:
Healthy {diet} Bowl

Ingredients:
{", ".join(filtered_items)}

Instructions:

1. Wash all ingredients.
2. Prepare ingredients as needed.
3. Cook if necessary.
4. Combine everything.
5. Serve and enjoy.

============================
"""

    return recipe