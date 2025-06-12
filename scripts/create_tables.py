from database.database import engine, metadata
from database.models import songs

# Create tables based on models
metadata.create_all(engine)

print("Database and tables created!")
