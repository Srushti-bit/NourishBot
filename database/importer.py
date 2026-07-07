import sqlite3
import pandas as pd
from pathlib import Path

# Paths
DB_PATH = Path(__file__).parent / "nutrition.db"
CSV_PATH = Path(__file__).parent / "datasets" / "cleaned_nutrition_dataset_per100g.csv"

print("📂 Loading dataset...")

# Read CSV
df = pd.read_csv(CSV_PATH)

print(f"✅ Found {len(df)} rows")

# Replace NaN with 0
df = df.fillna(0)

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

imported = 0
skipped = 0

for _, row in df.iterrows():

    try:
        cursor.execute("""
            INSERT OR IGNORE INTO foods (
                name,
                normalized_name,
                calories,
                protein,
                carbs,
                fat,
                fiber,
                sugar,
                sodium,
                calcium,
                iron,
                vitamin_c,
                vitamin_b11
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            str(row["food"]),
            str(row["food_normalized"]),

            float(row["Calories (kcal per 100g)"]),
            float(row["Protein (g per 100g)"]),
            float(row["Carbohydrates (g per 100g)"]),
            float(row["Fat (g per 100g)"]),
            float(row["Dietary Fiber (g per 100g)"]),
            float(row["Sugars (g per 100g)"]),

            float(row["Sodium (mg per 100g)"]),
            float(row["Calcium (mg per 100g)"]),
            float(row["Iron (mg per 100g)"]),

            float(row["Vitamin C (mg per 100g)"]),
            float(row["Vitamin B11 (mg per 100g)"])

        ))

        if cursor.rowcount:
            imported += 1
        else:
            skipped += 1

    except Exception as e:
        skipped += 1
        print(f"⚠ Skipped row: {e}")

conn.commit()
conn.close()

print("\n==============================")
print(f"✅ Imported : {imported}")
print(f"⚠ Skipped  : {skipped}")
print("🎉 Database Ready!")
print("==============================")