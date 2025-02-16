import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.state.states import AuthState 
from videoflix.Components.lists.list_films import mostrar_pelicula
from videoflix.queries.multiples_queries import consultarDB
from videoflix.models import Pelicula




@rx.page(route=PELICULAS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login())
def user_film() -> rx.Component:
    '''función user_film
    retorna los componentes que dan forma a la ventana donde ver un listado de películas'''
    return rx.box(
        header(),
        rx.vstack(
            logo_central("200px"),
            rx.heading(f"Hola, {AuthState.user.nombre}"),
            mostrar_pelicula(texto= "Nuestras Películas disponibles:", accion=consultarDB(Pelicula)),
            padding_y= Size.VERY_BIG.value,
            padding_top= Size.MAX_BIG,
            padding_x= Size.DEFAULT.value
        ),
        footer(),
        width="100%"
    )