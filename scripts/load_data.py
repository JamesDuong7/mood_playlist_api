import csv
from database.database import engine
from database.models import songs

with engine.connect() as connection:
    with open('data/music_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["id", "title", "artist", "mood"])

        # Skip header row explicitly
        next(reader)

        # Convert the 'id' fields explicitly to integers
        rows = [
            {"id": int(row["id"]), "title": row["title"], "artist": row["artist"], "mood": row["mood"]}
            for row in reader
        ]

        connection.execute(songs.insert(), rows)

print("Data loaded successfully!")
