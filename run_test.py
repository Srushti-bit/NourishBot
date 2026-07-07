from utils.food_mapper import FoodResolver

resolver = FoodResolver("database/nutrition.db")

tests = [
    "rice",
    "white rice",
    "chicken",
    "grilled chicken",
    "egg",
    "banana smoothie",
    "milk",
    "broccoli",
    "unknownfoodxyz"
]

for t in tests:
    print(resolver.resolve_food(t))