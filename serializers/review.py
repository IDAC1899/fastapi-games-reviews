# serializers/review.py

from pydantic import BaseModel
from .user import UserSchema

class ReviewSchema(BaseModel):
  id: int
  content: str
  rating: int
  # the user who wrote the review
  user: UserSchema

  class Config:
    orm_mode = True

class CreateReviewSchema(BaseModel):
  content: str
  rating: int

  class Config:
    orm_mode = True

class UpdateReviewSchema(BaseModel):
  content: str
  rating: int

  class Config:
    orm_mode = True