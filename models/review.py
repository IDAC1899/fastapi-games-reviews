# models/review.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class ReviewModel(BaseModel):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)

    # each review belongs to one game, and gets deleted if its game is deleted
    game_id = Column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False)
    game = relationship("GameModel", back_populates="reviews", passive_deletes=True)