"""
Recipe Agent for NourishBot.

Responsible for:
- Filtering ingredients based on dietary preference
- Generating a simple recipe
"""

from utils.dietary_filter import filter_ingredients

RECIPE_SEPARATOR = "=" * 30


def generate_recipe(
    food_items: list[str],
    diet: str,
) -> str:
    """
    Generate a recipe based on detected foods and dietary preference.

    Args:
        food_items: List of detected foods.
        diet: User-selected diet.

    Returns:
        Formatted recipe.
    """

    if not food_items:
        return (
            f"{RECIPE_SEPARATOR}\n"
            "RECIPE\n"
            f"{RECIPE_SEPARATOR}\n\n"
            "No ingredients were detected.\n"
        )

    filtered_items = filter_ingredients(
        food_items,
        diet,
    )

    if not filtered_items:
        return (
            f"{RECIPE_SEPARATOR}\n"
            "RECIPE\n"
            f"{RECIPE_SEPARATOR}\n\n"
            f"No ingredients match the '{diet}' diet.\n"
        )

    recipe = (
        f"{RECIPE_SEPARATOR}\n"
        "RECIPE\n"
        f"{RECIPE_SEPARATOR}\n\n"
        f"Recipe Name:\n"
        f"Healthy {diet.title()} Bowl\n\n"
        f"Ingredients:\n"
        f"{', '.join(filtered_items)}\n\n"
        "Instructions:\n\n"
        "1. Wash all ingredients.\n"
        "2. Prepare the ingredients.\n"
        "3. Cook them if required.\n"
        "4. Combine everything in a bowl.\n"
        "5. Season to taste.\n"
        "6. Serve and enjoy!\n\n"
        f"{RECIPE_SEPARATOR}"
    )

    return recipe