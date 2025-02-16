import reflex as rx
from videoflix.state.states import AuthState
from videoflix.styles.constants import *

def signup_form() -> rx.Component:
    '''función sign_op form
    retorna el formulario de registro a la web'''
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
                    "Crea tu cuenta",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Nombre y apellidos",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="Escribe tu nombre",
                    on_blur=AuthState.set_nombre,
                    id="nombre",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
                        rx.vstack(
                rx.text(
                    "Alias",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("person-standing")),
                    placeholder="Usuario",
                    id="username",
                    on_blur=AuthState.set_username,
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
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
                    id="email",
                    type="email",
                    on_blur=AuthState.set_email,
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Contraseña",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Introduce tu contraseña",
                    id="password",
                    on_blur=AuthState.set_password,
                    type="password",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Repite la Contraseña",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Introduce de nuevo tu contraseña",
                    id="confirm_password",
                    type="password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.box(
                rx.checkbox(
                    "Acepto los términos y Condiciones",
                    default_checked=False,
                    on_change=AuthState.set_accepted_terms,
                    spacing="2",
                ),
                width="100%",
            ),
            rx.button(
                "Regístrate",
                size="3", 
                on_click=AuthState.signup,
                width="100%",
                type="submit"
            ),
            rx.center(
                rx.text("¿Ya estás registrado?", size="3"),
                rx.link("Inicia Sesión", href=LOGIN, size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )

