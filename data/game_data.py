# data/game_data.py
from models.game import GameModel
from models.review import ReviewModel

# games to seed into the database, each owned by a user
games_list = [
    GameModel(name="Valorant", platform="PC", genre="Shooter", user_id=1),
    GameModel(name="Minecraft", platform="PC", genre="Sandbox", user_id=2),
    GameModel(name="Mario Kart 8 Deluxe", platform="Switch", genre="Racing", user_id=3),
    GameModel(name="Spider-Man 2", platform="PS5", genre="Action", user_id=4),
    GameModel(name="Zelda: Tears of the Kingdom", platform="Switch", genre="Adventure", user_id=5),
]

# reviews linked to games by game_id, and to their writer by user_id
reviews_list = [
    ReviewModel(content="Great gunplay but the ranked queue is stressful", rating=8, game_id=1, user_id=2),
    ReviewModel(content="Fun with friends, frustrating solo", rating=6, game_id=1, user_id=3),
    ReviewModel(content="Endless building, never gets old", rating=9, game_id=2, user_id=1),
    ReviewModel(content="Best party game on the Switch", rating=9, game_id=3, user_id=4),
    ReviewModel(content="Swinging around the city feels amazing", rating=8, game_id=4, user_id=5),
]