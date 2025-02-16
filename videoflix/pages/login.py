import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, MAX_WIDTH
from videoflix.Components.footer import footer 
from videoflix.Components.navbar import navbar_buttons as header
from videoflix.Components.logo import logo_central
from videoflix.Components.forms.signinform import form_login

@rx.page(route=LOGIN, title=TITTLE_LOGIN)
def login() -> rx.Component:
    '''función login
    retorna los componentes que dan forma a la pestaña de logado de la web'''
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                logo_central("250px"),
                form_login(),
                width="100%",
                max_width=MAX_WIDTH,
                justify="center", 
                align="center"   
            ),
            margin=Size.DEFAULT.value,
            padding_y = Size.VERY_BIG.value
            
        ),
        footer()
    )