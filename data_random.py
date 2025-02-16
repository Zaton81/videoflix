import reflex as rx
from randomuser import RandomUser
from videoflix.models import User
#archivo utilizado para crear de manera aleatoria usuarios

def aniadir_usuario():
    user_list = RandomUser.generate_users(10)


    for user in user_list:
        with rx.session() as session:
            session.add(
                User(
                    username=user.get_username(),
                    nombre=user.get_first_name(),
                    email=user.get_email(),
                    password=user.get_password(),
                    admin=False
                )
            )
            session.commit()

def add_admin():
    with rx.session() as session:
        session.add(
             User(
                username="admin",
                nombre="Jorge Zatón Pérez",
                email="admin@videoflix.com",
                password="admin",
                admin=True
            )
        )
        session.commit()

aniadir_usuario()
add_admin()

