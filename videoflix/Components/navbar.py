'''archivo navbar
en él se encuentran las diferentes barras de navegación (nabvar) del header'''

import reflex as rx
from videoflix.styles.constants import *
from videoflix.Components.searchbar import searchbar
from videoflix.styles.styles import HEADER_STYLE, Size
from videoflix.state.states import AuthState

def navbar_link(text: str, url: str) -> rx.Component:
    '''función nabvar_link
    retorna un componente para añadir enlaces al header o navbar'''
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar_buttons() -> rx.Component:
    '''función navbar_buttons
    retorna la cabecera de la web de la página principal.
    Esta solo se muestra cuando el usuario no está logado'''
    return rx.box(
        rx.desktop_only(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/logoSin.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",            
                        ),
                        rx.heading(
                            "Videoflix", size="7", weight="bold"
                        ),
                        align_items="center",
                        margin_left=Size.MEDIUM.value
                    ),
                    rx.hstack(
                        navbar_link("Inicio", "/"),
                        navbar_link("Películas", PELICULAS),
                        navbar_link("Series", SERIES),
                        spacing="5",
                    ),
                    searchbar(),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Regístrate",
                                size="3",
                                variant="outline",
                            ),
                            href=REGISTRO
                        ),
                        rx.link(
                            rx.button("Inicia Sesión", size="3"),
                            href=LOGIN
                            ),
                            rx.color_mode.button(),
                            spacing="4",
                            justify="end",
                            
                        ),
                    justify="between",
                    position="sticky",
                    z_index="999",
                    top="0",
                    margin_top=Size.MEDIUM.value,
                    margin_bottom=Size.DEFAULT.value
                ),
            justify="between",
            position="relative",
            align_items="center",
            z_index="999",
            top="0"
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logoSin.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Videoflix", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        
                        rx.menu.item(rx.link("Inicio", href=HOME),
                        href=HOME
                        ),
                        rx.menu.item(rx.link("Películas", href=PELICULAS),
                        href=HOME
                        ), 
                        rx.menu.item(rx.link("Series", href=SERIES),
                        href=HOME
                        ),                       
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                rx.color_mode.button(),
                justify="between",
                align_items="center",
            ),
            #rx.color_mode.button(position="top-right"),
        ),
        rx.divider(),
        bg=rx.color("accent", 3),
        margin_bottom= Size.BIG.value,
        justify="center",
        align_items="center",
        position="fixed",
        z_index="1000",
        top="0",
        width="100%",
        style=HEADER_STYLE
    )


def navbar_user() -> rx.Component:
    '''función navbar_user
    retorna la cabecera de la web que se muestra cuando el usuario está logado'''
    return rx.box(
        rx.desktop_only(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/logoSin.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Videoflix", size="7", weight="bold"
                        ),
                        align_items="center",
                    ),
                    rx.hstack(
                        navbar_link("Inicio", "/user/[alias]"),
                        navbar_link("Películas", PELICULAS),
                        navbar_link("Series", SERIES),
                        navbar_link("Favoritos", PEL_FAVS),
                        navbar_link("Estadísticas", ESTADISTICAS),
                        navbar_link("Vistas", VISTAS),
                        spacing="5",
                    ),
                    searchbar(),
                    rx.button(
                    "cerrar sesión",
                    on_click=AuthState.logout()
                    ),
                    rx.hstack(
                        rx.color_mode.button(),
                        spacing="4",
                        justify="end",
                        
                    ),
                    justify="between",
                    margin_top=Size.MEDIUM.value,
                    padding_bottom=Size.DEFAULT.value
                ),
            justify="between",
            position="relative",
            align_items="center",
            z_index="999",
            top="0"
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logoSin.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Videoflix", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        
                        rx.menu.item(rx.link("Inicio", href="/user/[alias]"),
                        href=HOME
                        ),
                        rx.menu.item(rx.link("Películas", href=PELICULAS),
                        href=HOME
                        ), 
                        rx.menu.item(rx.link("Series", href=SERIES),
                        href=HOME
                        ),                       
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                rx.color_mode.button(),
                justify="between",
                align_items="center",
            ),
            #rx.color_mode.button(position="top-right"),
        ),
        rx.divider(),
        bg=rx.color("accent", 3),
        justify="center",
        align_items="center",
        position="fixed",
        z_index="1000",
        top="0",
        width="100%",
        style=HEADER_STYLE,
        padding_x = Size.DEFAULT.value,
        padding_top=Size.DEFAULT.value
    )