import reflex as rx
from videoflix.styles.constants import *
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.styles.styles import Size
from videoflix.state.states import AuthState 
from videoflix.Components.lists.list_series import mostrar_serie




@rx.page(route=SERIES, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login())
def user_series() -> rx.Component:
    '''función user_series
    retorna los componentes que dan forma a la ventana donde ver un listado de las series'''
    return rx.box(
        header(),
        rx.vstack(
            rx.heading(f"Hola, {AuthState.user.nombre}"),
            rx.center(
                rx.vstack(
                    logo_central("200px"),
                    mostrar_serie(),
                ),
            ),
            padding_top= Size.MAX_BIG.value,
            padding_bottom= Size.DEFAULT.value,
            padding_x= Size.DEFAULT.value
        ),
        footer(),
        width="100%"
    )