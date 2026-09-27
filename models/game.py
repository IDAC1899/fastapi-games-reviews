# models/game.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import BaseModel
from .review import ReviewModel

class GameModel(BaseModel):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    platform = Column(String)
    genre = Column(String)

    # one game has many reviews
    reviews = relationship("ReviewModel", back_populates="game", cascade="all, delete-orphan")