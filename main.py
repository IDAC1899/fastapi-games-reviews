# main.py

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from controllers.games import router as GamesRouter
from controllers.reviews import router as ReviewsRouter
from controllers.users import router as UsersRouter

app = FastAPI()

app.include_router(GamesRouter, prefix='/api')
app.include_router(ReviewsRouter, prefix='/api')
app.include_router(UsersRouter, prefix='/api')

@app.get('/')
def home():
    return {'message': 'Welcome to the games reviews API!'}