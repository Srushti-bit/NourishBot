import sqlite3

conn = sqlite3.connect("database/nutrition.db")
cursor = conn.cursor()

foods = [
    "rice",
    "white rice",
    "chicken",
    "egg",
    "banana",
    "broccoli",
    "apple",
    "milk",
    "pizza",
]

for food in foods:
    print(f"\n========== {food.upper()} ==========")

    cursor.execute(
        """
        SELECT name, normalized_name
        FROM foods
        WHERE normalized_name LIKE ?
        LIMIT 10
        """,
        (f"%{food}%",),
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No matches found.")

conn.close()