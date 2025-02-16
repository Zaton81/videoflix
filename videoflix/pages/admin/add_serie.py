import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import  footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.forms.form_series import form_series

@rx.page(route=ADMIN_SERIES, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin_series() -> rx.Component:
    '''función admin_series
    retorna los componentes de la pestaña desde la que un administrador puede añadir, y editar series'''
    return rx.box(
        header(),
        rx.heading(f"Hola, {AuthState.user.nombre}", padding_top=Size.MAX_BIG.value),
        rx.center(
            rx.vstack(
                rx.link(
                    rx.heading(
                    "Regresar a la página principal",
                    size="5"
                    ),
                    href=ADMIN
                ),
                form_series(),
                padding_bottom = Size.MAX_BIG.value
            ),
        ),
        footer(),
        width="100%"
    )