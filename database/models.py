from sqlalchemy import Table, Column, Integer, String
from .database import metadata

# Define a table named 'songs' to store song details clearly
songs = Table(
    "songs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("artist", String, nullable=False),
    Column("mood", String, nullable=False),
)
