'''archivo buttons
da forma a los distintos botones utilizados en la web'''

import reflex as rx
from videoflix.styles.constants import LOGIN
from videoflix.styles.colors import Color

def link_button(text="", size="4", link=LOGIN, color=Color.BUTTON.value, icono="film") ->rx.Component:
    '''función link_button
    retorna un componente de reflex en forma de botón de enlace
    recibe los parámetros
    text: el texto que mostrará el botón
    size: el tamaño del botón
    link: el enlace al que redirige cuando pulsas el botón
    color: el color del botón
    icono: el icono del botón'''

    return rx.link(
        rx.button(
            rx.icon(icono),
            text,
            size=size,
            width="100%",
            color_scheme=color
            ),
        href=link,
        width="100%"
    )

def confirm_button(text="", size="4", accion=None, icono="heart"):
    ''' función confirm button
    recibe:
    texto: el texto que muestra el botón
    size: el tamaño del botón
    acción: la acción que realiza al pulsar el botón
    icono: el icono que muestra el botón
    retorna un componente que, al hacer click sobre él, salta un mensaje de confirmación'''
    return rx.button(
        rx.icon(icono),
        text=text,
        size=size,
        on_click=accion,
        type="submit"


    )
