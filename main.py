# main.py

from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.games import router as GamesRouter
from controllers.reviews import router as ReviewsRouter
from controllers.users import router as UsersRouter

app = FastAPI()

# front-end addresses allowed to call this api, read from .env
origins = [
    origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",")
    if origin.strip()
]

# let those front-ends make requests to the api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(GamesRouter, prefix='/api')
app.include_router(ReviewsRouter, prefix='/api')
app.include_router(UsersRouter, prefix='/api')

@app.get('/')
def home():
    return {'message': 'Welcome to the games reviews API!'}