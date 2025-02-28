from models import Base
from database import engine

# WARNING: This will delete all data and recreate the tables
print("Dropping existing tables...")
Base.metadata.drop_all(bind=engine)  # Deletes all tables

print("Creating new tables...")
Base.metadata.create_all(bind=engine)  # Recreates all tables

print("Database reset complete!")
