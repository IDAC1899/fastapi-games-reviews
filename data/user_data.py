from models.user import UserModel

def create_test_users():
    user1 = UserModel(username="khalil_Khunji", email="Khalil.Khunji@email.in")
    user1.set_password("123")
    user2 = UserModel(username="Noor_Sharf", email="Noor.Sharaf@email.com")
    user2.set_password("123")
    user3 = UserModel(username="Isa_Daaysi", email="Isa.Daaysu@correo.br")
    user3.set_password("123")
    user4 = UserModel(username="Dennis_Sanchez", email="Denis.Sanchez@email.ae")
    user4.set_password("123")
    user5 = UserModel(username="Mohammed_Derazi", email="Mohammed.Derazi@mail.ru")
    user5.set_password("123")

    return [user1, user2, user3, user4, user5]

user_list = create_test_users()