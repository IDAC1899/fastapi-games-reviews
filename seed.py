# seed.py
from sqlalchemy.orm import sessionmaker
from data.game_data import games_list, reviews_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # drop and recreate tables for a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # seed games first, reviews depend on them
    db.add_all(games_list)
    db.commit()

    db.add_all(reviews_list)
    db.commit()
    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)