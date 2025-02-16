import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import  footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.forms.form_chapter import form_chapter

@rx.page(route=ADMIN_CHAPTERS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin_chapter() -> rx.Component:
    '''función admin_chapter
    retorna los componentes de la pestaña desde la que un administrador puede añadir, y editar capítulos'''
    return rx.box(
        header(),
        rx.heading(f"Hola, {AuthState.user.nombre}",
                padding_top=Size.VERY_BIG.value, 
                padding_x=Size.BIG.value),
        rx.center(
            rx.vstack(
                rx.link(
                    rx.heading(
                    "Regresar a la página principal",
                    size="5"
                    ),
                    href=ADMIN
                ),
                form_chapter(),
                padding_bottom=Size.MAX_BIG.value,
            ),
        ),
        footer(),
        width="100%"
    )