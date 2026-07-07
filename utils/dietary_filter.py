def filter_ingredients(ingredients, diet):
    """
    Remove ingredients that violate dietary restrictions.
    """

    restrictions = {
        "Vegan": [
            "chicken",
            "beef",
            "fish",
            "egg",
            "milk"
        ],

        "Vegetarian": [
            "chicken",
            "beef",
            "fish"
        ],

        "Gluten-Free": [
            "bread",
            "pasta"
        ],

        "Keto": [
            "rice",
            "bread",
            "pasta"
        ]
    }

    if diet not in restrictions:
        return ingredients

    return [
        ingredient
        for ingredient in ingredients
        if ingredient.lower() not in restrictions[diet]
    ]