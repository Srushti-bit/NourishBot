from agents.recipe_agent import generate_recipe

foods = [
    "rice",
    "chicken",
    "broccoli",
    "egg"
]

print(generate_recipe(
    foods,
    "Vegan"
))