# config/environment.py
import os
from dotenv import load_dotenv

# load the variables from .env
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
JWT_SECRET = os.getenv('JWT_SECRET')