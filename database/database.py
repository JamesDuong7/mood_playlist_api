from databases import Database
from sqlalchemy import create_engine, MetaData

# Database URL (SQLite)
DATABASE_URL = "sqlite:///./database/database.db"

# Create an async database connection
database = Database(DATABASE_URL)

# Engine to handle connection with SQLite
engine = create_engine(DATABASE_URL)

# Metadata holds details about tables in your database
metadata = MetaData()
