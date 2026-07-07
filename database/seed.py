import sqlite3
import csv
from pathlib import Path

DB_PATH = Path(__file__).parent / "nutrition.db"
CSV_PATH = Path(__file__).parent / "foods.csv"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(CSV_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT OR IGNORE INTO foods (
                name,
                category,
                cuisine,
                serving_size,
                calories,
                protein,
                carbs,
                fat,
                fiber,
                sugar,
                sodium
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["name"],
            row["category"],
            row["cuisine"],
            row["serving_size"],
            float(row["calories"]),
            float(row["protein"]),
            float(row["carbs"]),
            float(row["fat"]),
            float(row["fiber"]),
            float(row["sugar"]),
            float(row["sodium"])
        ))

conn.commit()
conn.close()

print("✅ Food database imported successfully!")