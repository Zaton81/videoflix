import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, MAX_WIDTH
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.forms.form_user import form_add_user, form_edit_user, form_delete_user

@rx.page(route=ADMIN_USERS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin_user() -> rx.Component:
    '''función admin_series
    retorna los componentes de la pestaña desde la que un administrador puede añadir, y editar series'''
    return rx.box(
        header(),
        rx.heading(f"Hola, {AuthState.user.nombre}", padding_top=Size.VERY_BIG.value, 
                   padding_x=Size.BIG.value),
        rx.center(
            rx.vstack(
                rx.heading("Selecciona una opción:"),    
                rx.link(
                    rx.heading(
                    "Regresar a la página principal",
                    size="5"
                    ),
                    href=ADMIN
                ),
                rx.card(
                    rx.vstack(
                        form_add_user(),
                        form_edit_user(),
                        form_delete_user(),
                        margin="3",
                        widtn=MAX_WIDTH
                    ),
                ),
            ),
            padding_bottom=Size.VERY_BIG.value
        ),
        footer(),
        width="100%"
    )