# scripts/load_data.py
import sys
from pathlib import Path
import csv

# Add project root to Python path for reliable imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

from database.database import engine
from database.models import songs

# Set the CSV file path
CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "music_data.csv"

# --- Read CSV and prepare rows ---
with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = []
    for row in reader:
        # Skip rows with invalid or blank ids
        if not row["id"].strip().isdigit():
            continue
        rows.append({
            "id": int(row["id"]),
            "title": row["title"].strip(),
            "artist": row["artist"].strip(),
            "mood": row["mood"].strip().lower()
        })

print(f"Parsed {len(rows)} rows from CSV.")
if not rows:
    print("No data found in CSV. Nothing loaded.")
else:
    # Insert rows into the songs table in a single transaction
    with engine.begin() as conn:
        conn.execute(songs.insert(), rows)
    print("Data loaded into database.db.")
