# serializers/game.py

from pydantic import BaseModel
from typing import List
from .review import ReviewSchema
from .user import UserSchema

class GameSchema(BaseModel):
  id: int
  name: str
  platform: str
  genre: str
  # the user who added the game
  user: UserSchema
  reviews: List[ReviewSchema] = []

  class Config:
    orm_mode = True

class CreateGameSchema(BaseModel):
  name: str
  platform: str
  genre: str

class UpdateGameSchema(BaseModel):
  name: str
  platform: str
  genre: str