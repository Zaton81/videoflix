import reflex as rx
from videoflix.styles.constants import TITTLE, DESCRIPTION, LOGIN, REGISTRO
from videoflix.Components.navbar import navbar_buttons as navbar
from videoflix.Components.footer import footer
from videoflix.Components.logo import logo_central as logo
from videoflix.Components.buttons import link_button as button
from videoflix.styles.styles import Size

@rx.page(route="/", title=TITTLE, description=DESCRIPTION)
def index() -> rx.Component:
    '''función home. 
    Retorna la página de inicio del usuario. 
    '''
    return rx.box(
        navbar(), #header
        rx.center(
            rx.vstack(
                logo("550px"),
                rx.heading(TITTLE, size="9"),
                rx.card(
                    rx.hstack(
                        rx.center(
                        button(text="Inicia Sesión", link=LOGIN),
                        button(text="Regístrate", link=REGISTRO),
                        spacing="5",
                        margin= Size.DEFAULT.value,
                        width= "100%" ,
                        padding= Size.SMALL.value,
                        justify= "center"
                    )
                    ),
                    width="100%"
                ), 
                margin=Size.DEFAULT.value,
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
            padding_top= Size.VERY_BIG.value,
            padding_bottom= Size.VERY_BIG.value
        ),
        footer(),
    )