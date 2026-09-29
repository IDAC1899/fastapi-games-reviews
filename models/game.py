# models/game.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .review import ReviewModel
from .user import UserModel

class GameModel(BaseModel):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    platform = Column(String)
    genre = Column(String)

    # one game has many reviews
    reviews = relationship("ReviewModel", back_populates="game", cascade="all, delete-orphan")

    # each game belongs to the user who added it
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", back_populates="games")