'''archivo de inputs'''
import reflex as rx
from videoflix.styles.styles import Size, Spacing
def input_form(accion, texto="", icono="film", texto_input="", ) ->rx.Component:
    '''función input.
    retorna un input para añadir al formulario'''
    return rx.vstack(
        rx.text(
            texto,
            size="3",
            weight="medium",
            text_align="left",
            width="100%",
        ),
        rx.input(
            rx.input.slot(rx.icon(icono)),
            placeholder=texto_input,
            type="code",
            on_blur=accion,
            size="3",
            width="100%",
            reset_on_submit=True
        ),
        justify="start",
        spacing=Spacing.DEFAULT.value,
        padding=Size.MEDIUM.value,
        width="100%",
    ),