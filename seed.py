# seed.py
from sqlalchemy.orm import sessionmaker
from data.game_data import games_list, reviews_list
from data.user_data import user_list
from config.environment import DATABASE_URL
from sqlalchemy import create_engine
from models.base import Base

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # drop and recreate tables for a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # seed users first, games and reviews depend on them
    db.add_all(user_list)
    db.commit()

    # seed games next, reviews depend on them
    db.add_all(games_list)
    db.commit()

    db.add_all(reviews_list)
    db.commit()
    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)