import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.logo import logo_central
from videoflix.Components.card_options import options

@rx.page(route=ADMIN, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin() -> rx.Component:
    '''función admin
    página principal del administrados, desde donde puede seleccionar acciones a realizar'''
    return rx.box(
        header(),
        rx.vstack(
                logo_central("200px"),
                rx.heading(f"Hola, {AuthState.user.nombre}", size="9"),
                padding_top=Size.MAX_BIG.value,
                padding_x=Size.DEFAULT. value
                ),
        
        rx.center(
            rx.vstack(
                
                rx.heading("Panel de administración", size="8", weight="bold"),
                options(
                    text_heading=f"{AuthState.user.username}, ¿qué desas hacer?",
                    texto1="Añadir o editar películas",
                    texto2="Añadir o editar series",
                    texto3="Añadir o editar capítulos.",
                    texto4="Añadir o editar usuarios",
                    texto5="Consultar estadísticas.",
                    links=[ADMIN_FILMS, ADMIN_SERIES, ADMIN_CHAPTERS, ADMIN_USERS,  ADMIN_ESTADISTICAS]
                ),
                margin=Size.DEFAULT.value,
                spacing="5"  
            ),
        ),
        footer(),
        width="100%"
    )

