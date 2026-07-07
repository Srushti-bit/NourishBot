import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "nutrition.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS foods")

cursor.execute("""
CREATE TABLE foods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    normalized_name TEXT UNIQUE,

    category TEXT,
    cuisine TEXT,
    serving_size TEXT DEFAULT '100 g',

    calories REAL,
    protein REAL,
    carbs REAL,
    fat REAL,
    fiber REAL,
    sugar REAL,

    sodium REAL,
    calcium REAL,
    iron REAL,

    vitamin_c REAL,
    vitamin_b11 REAL
)
""")

conn.commit()
conn.close()

print("✅ Database schema created successfully!")