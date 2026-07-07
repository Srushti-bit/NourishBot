import sqlite3
import sys

DB_PATH = "database/nutrition.db"


def search_food(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT normalized_name
        FROM foods
        WHERE LOWER(normalized_name) LIKE ?
        ORDER BY normalized_name
        LIMIT 20
    """, (f"%{query.lower()}%",))

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print(f"\n❌ No foods found for '{query}'")
        return

    print(f"\n========== Results for '{query}' ==========\n")

    for row in rows:
        print(row[0])

    print(f"\nTotal Matches: {len(rows)}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python tools/inspect_database.py <food_name>")
        sys.exit()

    search_food(sys.argv[1])