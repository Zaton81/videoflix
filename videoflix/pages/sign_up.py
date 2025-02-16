import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import *
from videoflix.Components.footer import footer 
from videoflix.Components.navbar import navbar_buttons as header
from videoflix.Components.logo import logo_central
from videoflix.Components.forms.sigunpform import signup_form

@rx.page(route=REGISTRO, title=TITTLE_REGISTRO)
def sign_up() -> rx.Component:
    '''función SIGN_UP
    retorna los componentes que dan forma a la pestaña de registro de un usuario a la web'''
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                logo_central("250px"),
                signup_form(),
                width="100%",
                maw_width=MAX_WIDTH,
                align="center"
            ),
            #padding=Size.DEFAULT.value,  
            padding_y = Size.MAX_BIG.value
        ),
        footer()
    )