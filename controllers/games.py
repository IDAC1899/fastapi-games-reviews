# controllers/games.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List

# models
from models.game import GameModel
from models.user import UserModel

# serializers
from serializers.game import GameSchema, CreateGameSchema, UpdateGameSchema

# db
from sqlalchemy.orm import Session
from database import get_db

# auth
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/games", response_model=List[GameSchema])
def get_games(db: Session = Depends(get_db)):
    games = db.query(GameModel).all()

    return games

@router.get("/games/{game_id}", response_model=GameSchema)
def get_single_game(game_id: int, db: Session = Depends(get_db)):
    game_in_database = db.query(GameModel).filter(GameModel.id == game_id).first()

    if not game_in_database:
        raise HTTPException(status_code=404, detail="Game not found")

    return game_in_database

# any logged in user can add a game
@router.post("/games", response_model=GameSchema, status_code=201)
def create_game(game: CreateGameSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # the logged in user becomes the game's owner
    new_game = GameModel(**game.dict(), user_id=current_user.id)

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game

# only the game's owner can update it
@router.put("/games/{game_id}", response_model=GameSchema)
def update_game(game_id: int, game: UpdateGameSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    game_in_database = db.query(GameModel).filter(GameModel.id == game_id).first()

    if not game_in_database:
        raise HTTPException(status_code=404, detail="Game not found")

    # check if the current user added the game
    if game_in_database.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    game_data = game.dict(exclude_unset=True)

    # replace each field with the new value
    for key, value in game_data.items():
        setattr(game_in_database, key, value)

    db.commit()
    db.refresh(game_in_database)

    return game_in_database

# only the game's owner can delete it
@router.delete("/games/{game_id}", status_code=204)
def delete_game(game_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    game_in_database = db.query(GameModel).filter(GameModel.id == game_id).first()

    if not game_in_database:
        raise HTTPException(status_code=404, detail="Game not found")

    # check if the current user added the game
    if game_in_database.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(game_in_database)
    db.commit()

    return None