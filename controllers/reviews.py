# controllers/reviews.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List

# models
from models.game import GameModel
from models.review import ReviewModel
from models.user import UserModel

# serializers
from serializers.review import ReviewSchema, CreateReviewSchema, UpdateReviewSchema

# db
from sqlalchemy.orm import Session
from database import get_db

# auth
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/games/{game_id}/reviews", response_model=List[ReviewSchema])
def get_reviews_for_game(game_id: int, db: Session = Depends(get_db)):
    game_in_database = db.query(GameModel).filter(GameModel.id == game_id).first()

    if not game_in_database:
        raise HTTPException(status_code=404, detail="Game not found")

    return game_in_database.reviews

@router.get("/reviews/{review_id}", response_model=ReviewSchema)
def get_single_review(review_id: int, db: Session = Depends(get_db)):
    review_in_database = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review_in_database:
        raise HTTPException(status_code=404, detail="Review not found")

    return review_in_database

# any logged in user can review a game
@router.post("/games/{game_id}/reviews", response_model=ReviewSchema, status_code=201)
def create_review(game_id: int, review: CreateReviewSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    game_in_database = db.query(GameModel).filter(GameModel.id == game_id).first()

    if not game_in_database:
        raise HTTPException(status_code=404, detail="Game not found")

    # the logged in user becomes the review's owner
    new_review = ReviewModel(**review.dict(), game_id=game_id, user_id=current_user.id)

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

# only the review's owner can update it
@router.put("/reviews/{review_id}", response_model=ReviewSchema)
def update_review(review_id: int, review: UpdateReviewSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    review_in_database = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review_in_database:
        raise HTTPException(status_code=404, detail="Review not found")

    # check if the current user wrote the review
    if review_in_database.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    review_data = review.dict(exclude_unset=True)

    # replace each field with the new value
    for key, value in review_data.items():
        setattr(review_in_database, key, value)

    db.commit()
    db.refresh(review_in_database)

    return review_in_database

# only the review's owner can delete it
@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    review_in_database = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review_in_database:
        raise HTTPException(status_code=404, detail="Review not found")

    # check if the current user wrote the review
    if review_in_database.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(review_in_database)
    db.commit()

    return None