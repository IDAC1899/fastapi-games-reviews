# data/game_data.py
from models.game import GameModel
from models.review import ReviewModel

# games to seed into the database
games_list = [
    GameModel(name="Valorant", platform="PC", genre="Shooter"),
    GameModel(name="Minecraft", platform="PC", genre="Sandbox"),
    GameModel(name="Mario Kart 8 Deluxe", platform="Switch", genre="Racing"),
    GameModel(name="Spider-Man 2", platform="PS5", genre="Action"),
    GameModel(name="Zelda: Tears of the Kingdom", platform="Switch", genre="Adventure"),
]

# reviews linked to games by game_id
reviews_list = [
    ReviewModel(content="Great gunplay but the ranked queue is stressful", rating=8, game_id=1),
    ReviewModel(content="Fun with friends, frustrating solo", rating=6, game_id=1),
    ReviewModel(content="Endless building, never gets old", rating=9, game_id=2),
    ReviewModel(content="Best party game on the Switch", rating=9, game_id=3),
    ReviewModel(content="Swinging around the city feels amazing", rating=8, game_id=4),
]