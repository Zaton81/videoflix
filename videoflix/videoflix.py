"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from videoflix.pages.home import index
from videoflix.pages.sign_up import sign_up
from videoflix.pages.login import login
from videoflix.pages.user import user
from videoflix.pages.admin.adminLogin import admin_login
from videoflix.pages.admin.admin import admin       
from videoflix.pages.admin.add_serie import admin_series
from videoflix.pages.admin.add_film import admin_films
from videoflix.pages.admin.add_user import admin_user
from videoflix.pages.admin.add_chapter import admin_chapter
from videoflix.pages.user.user_film import user_film
from videoflix.pages.user.film_page import film_page
from videoflix.pages.user.user_series import user_series
from videoflix.pages.stadistics import estadisticas
from videoflix.pages.user.favourite_films import favourite_films
from videoflix.pages.user.serie_page import serie_page
from videoflix.pages.user.capitulo_page import capitulo_page
from videoflix.pages.admin.admin_statistics import admin_stadisticas
from videoflix.pages.user.vistas import vistas
from videoflix.styles.styles import BASE_STYLE


class State(rx.State):
    """The app state."""

    ...


'''def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
'''

app = rx.App(style=BASE_STYLE)
#app.add_page(index)
