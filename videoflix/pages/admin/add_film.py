import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import  footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.forms.form_films import form_films

@rx.page(route=ADMIN_FILMS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin_films() -> rx.Component:
    '''función admin_films
    retorna los componentes de la pestaña desde la que un administrador puede añadir, y editar películas'''
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                rx.link(
                    rx.heading(
                    "Regresar a la página principal",
                    size="5"
                    ),
                    href=ADMIN
                ),
                form_films(),
                padding_y=Size.MAX_BIG.value
            )
        ),
        footer(),
        width="100%"
    )