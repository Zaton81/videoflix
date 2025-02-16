import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, MAX_WIDTH
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.forms.signinform import form_login
from videoflix.state.states import *


@rx.page(route=ADMIN_LOGIN, title=TITTLE_LOGIN)
def admin_login() -> rx.Component:
    '''función login
    retorna los componentes que dan forma a la pestaña de logado de la web de administrador'''
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                form_login(on_click=AuthState.login_admin()),
                padding_top=Size.MAX_BIG.value,
                padding_bottom=Size.MAX_BIG.value,
                width=MAX_WIDTH
            ),
            display="flex",
            align_items="center",  # Centrar verticalmente
            justify_content="center",  # Centrar horizontalmente
            height="100vh"  # Asegurar que el contenedor ocupe toda la altura de la ventana
        ),
        footer()
    )