import sqlite3

conn = sqlite3.connect("database/nutrition.db")
cursor = conn.cursor()

foods = [
    "apple",
    "pizza",
    "banana",
    "rice",
    "chicken",
    "biryani",
    "sushi",
    "ramen"
]

for food in foods:

    cursor.execute("""
        SELECT
            name,
            calories,
            protein,
            carbs,
            fat
        FROM foods
        WHERE LOWER(normalized_name) LIKE ?
        LIMIT 1
    """, (f"%{food.lower()}%",))

    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print(f"{food}: NOT FOUND")

conn.close()