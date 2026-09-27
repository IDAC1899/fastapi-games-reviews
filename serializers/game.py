# serializers/game.py

from pydantic import BaseModel
from typing import List
from .review import ReviewSchema

class GameSchema(BaseModel):
  id: int
  name: str
  platform: str
  genre: str
  reviews: List[ReviewSchema] = []

  class Config:
    orm_mode = True