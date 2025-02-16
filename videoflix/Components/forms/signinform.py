import reflex as rx
from videoflix.styles.constants import REGISTRO
from videoflix.state.states import *

def form_login(on_click=AuthState.login) ->rx.Component:
    '''funcion form_login
    retorna un formulario para ciar sesión en la web'''
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/favicon.ico",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                    
                ),
                rx.heading(
                    "Inicia sesión en tu cuenta",
                    size="6",
                    as_="h2",
                    width="100%",
                    align="center"
                ),
                rx.hstack(
                    rx.text(
                        "¿No estás registrado?",
                        size="3",
                        text_align="center",
                    ),
                    rx.link("Regístrate aquí", href=REGISTRO, size="3"),
                    spacing="2",
                    opacity="0.8",
                    width="100%",
                ),
                justify="center",
                direction="column",
                spacing="4",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Correo electrónico",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("mail")),
                    placeholder="usuario@videoflix.com",
                    on_blur=AuthState.set_email,
                    type="email",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                justify="start",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Contraseña",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "¿Olvidaste tu contraseña?",
                        href="#",
                        size="3",
                        on_click=rx.window_alert("Esta opción está temporalmente deshabilitada")
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Introduce tu contraseña",
                    type="password",
                    on_blur=AuthState.set_password,
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button(
                "Inicia sesión", 
                size="3", 
                on_click=on_click,
                width="100%", 
                type="submit"
            ),
            rx.hstack(
                rx.divider(margin="0"),
                rx.text(
                    "O inicia sesión con:",
                    white_space="nowrap",
                    weight="medium",
                ),
                rx.divider(margin="0"),
                align="center",
                width="100%",
            ),
            rx.center(
                rx.icon_button(
                    rx.icon(tag="github"),
                    on_click=rx.window_alert("Esta opción está temporalmente deshabilitada"),
                    variant="soft",
                    size="3",
                    
                ),
                rx.icon_button(
                    rx.icon(tag="facebook"),
                    on_click=rx.window_alert("Esta opción está temporalmente deshabilitada"),
                    variant="soft",
                    size="3",
                ),
                rx.icon_button(
                    rx.icon(tag="twitter"),
                    on_click=rx.window_alert("Esta opción está temporalmente deshabilitada"),
                    variant="soft",
                    size="3",
                ),
                spacing="4",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )