import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, MAX_WIDTH, Spacing
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.Components.card_options import options
from videoflix.state.states import AuthState 

@rx.page(route="/user/[alias]", title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login())
def user() -> rx.Component:
    '''función user
    retorna los componentes que dan forma a la pestaña de logado de la web'''
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                logo_central("250px"), 
                rx.heading(f"Hola, {AuthState.user.nombre}", size= Spacing.BIG.value),
                options(),
                rx.button(
                    "cerrar sesión",
                    on_click=AuthState.logout()
                ),
                width="100%",
                max_width=MAX_WIDTH,
                justify="center",
                margin=Size.DEFAULT.value,
                align="center"
            ),
            padding_y= Size.MAX_BIG.value
        ),
        footer(),
        width="100%",
        height = "100%"
    )