import sys
from pathlib import Path

# Clearly add the project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from database.database import engine, metadata
from database.models import songs

# Create tables based on models
metadata.create_all(engine)

print("Database and tables created!")
