import reflex as rx
from .buttons import link_button
from videoflix.styles.styles import *
from videoflix.styles.constants import *

def options(text_heading="¿Qué deseas hacer?",
            texto1="Ver las películas disponibles",
            texto2="ver las series disponibles",
            texto3="ver mis películas y series favoritas",
            texto4="ver mis series y películas vistas",
            texto5="ver mis estadísticas",
            links=[PELICULAS, SERIES, PEL_FAVS, VISTAS, ESTADISTICAS]
            ) ->rx.Component:
    '''función options
    recibe un texto de cabecera, 5 textos para los botones y una lista con 5 links
    retorna una tarjeta de botones con distintas opciones'''
    return rx.card(
        rx.heading(
            text_heading,
            padding_bottom=Size.DEFAULT.value,
            padding_top=Size.SMALL.value
        ),
        rx.vstack(
            link_button(texto1, link=links[0], icono="film"),
            link_button(texto2, link=links[1], icono="tv"),
            link_button(texto3, link=links[2], icono="heart"),
            link_button(texto4, link=links[3], icono= "eye"),
            link_button(texto5, link=links[4], icono="trending_down")
        ),
        width = MAX_WIDTH
    )