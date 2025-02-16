import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.lists.list_films import mostrar_pelicula
from videoflix.Components.lists.list_series import mostrar_favourite_caps
from videoflix.queries.multiples_queries import FavoritosState



@rx.page(route=VISTAS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=[AuthState.check_login(), 
                                                                                    FavoritosState.load_vistos(),
                                                                                    FavoritosState.load_cap_vistos()])
def vistas() -> rx.Component:
    '''función favourite_films
    retorna los componentes que dan forma a la ventana donde ver un listado de las películas vistas por el usuario'''
    return rx.box(
            header(),
                rx.center(
                    rx.vstack(
                        rx.heading(f"Hola, {AuthState.user.nombre}. Estas son tus peliculas y series vistas"),
                        mostrar_pelicula(texto="Tus películas vistas", accion=FavoritosState.vistas),
                        mostrar_favourite_caps(FavoritosState.cap_vistos),
                        width="100%",
                    ),
                    margin_top="100px",
                    padding_x= Size.DEFAULT.value,
                    padding_bottom=Size.VERY_BIG.value
                ),
            footer(),
        )
    