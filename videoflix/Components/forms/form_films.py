import reflex as rx
from videoflix.styles.constants import INSTRUCTIONS_FILM
from videoflix.Components.buttons import *
from videoflix.queries.filmQueries import Film_queries
from videoflix.styles.colors import Color
from videoflix.styles.styles import MAX_WIDTH
from videoflix.styles.styles import Size
from ..inputs import input_form


def form_films() -> rx.Component:
    '''función form_films
    formulario mediante el cual el administrador puede añadir, editar o elimina una película'''
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
                    "Editor de películas",
                    size="8",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                rx.heading(
                    "Introduce los datos de la película a añadir",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                form_del_film(),
                rx.text(rx.text.strong("Instrucciones:"),
                        INSTRUCTIONS_FILM),
                direction="column",
                spacing="5",
                width="100%",
                max_width=MAX_WIDTH
            ),
        ),
        input_form(accion=Film_queries.set_id, texto="Introduce la id si vas a modificar una película ya existente.",
                icono="smile", texto_input="id"),
        input_form(accion=Film_queries.set_titulo, texto="Introduce el nombre de la película.", 
                icono="film", texto_input="Película"),
        input_form(accion= Film_queries.set_year, texto="Introduce el año de estreno", 
                icono="calendar-search", texto_input="Año"),
        input_form(accion=Film_queries.set_duracion, texto="Introduce la duración en minutos", 
                icono="clock", texto_input="Minutos"),
        input_form(accion=Film_queries.set_video, texto="Introduce el código o link del vídeo", 
                icono="video", texto_input="Vídeo"),
        rx.text_area(
            placeholder="Introduce la sinopsis",
            name="Sinopsis",icon="film", 
            on_blur=Film_queries.set_sinopsis,
            padding_x=Size.DEFAULT.value),
        rx.vstack(
            rx.text(
                "Portada",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.vstack(
                rx.upload(
                    rx.vstack(
                        rx.button(
                            "Arrastra una imagen o clica aquí para seleccionarla", 
                            color=Color.SECONDARY.value,
                            bg=Color.PRIMARY.value, 
                            TextColor=Color.SECONDARY.value, 
                            border=f"1px solid {Color.PRIMARY.value}",
                            padding=Size.MEDIUM.value,
                            align="center",
                            width="100%",
                            padding_x=Size.DEFAULT.value
                        ),
                        rx.text(""),
                    ),
                    id="upload1",
                    image_name= rx.selected_files("upload1")[0]._var_name,
                    border=f"1px dotted {Color.SECONDARY.value}",
                    padding="5em",
                ),
                rx.hstack(rx.foreach(rx.selected_files("upload1"),  rx.text, ),
                ),
            ),
        ),
        rx.box(
            rx.hstack(
                rx.button(
                    "Subir película",
                    size="3", 
                    on_click=Film_queries.handle_upload_add(rx.upload_files(upload_id="upload1")),
                    Reset_on_submit=True,        
                    type="submit",
                    width="100%",
                    max_width="18em"
                ),
                rx.button(
                    "Editar película",
                    size="3", 
                    on_click=  rx.cond(
                        rx.upload_files(upload_id="upload1"),
                        Film_queries.handle_upload_edit(rx.upload_files(upload_id="upload1")),
                        Film_queries.handle_upload_edit()
                        ),
                    Reset_on_submit=True,
                    type="submit",
                    width="100%",
                    max_width="18em"
                    
                ),
                spacing="3",
                width="100%",
                align="center",
                padding_top=Size.DEFAULT.value
            ),
            spacing="6",
            width="100%",
            max_width="28em"
        ),
    )

def form_del_film() ->rx.Component:
    ''' función form_add_serie
    formulario mediante un administrador elimina películas de la base de datos a ttravés de la id'''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Eliminar Película", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Eliminar película",
            ),
            rx.alert_dialog.description(
                "Introduce la id de la película que quieres eliminar",
            ),
            rx.form(
                rx.flex(
                    input_form(accion=Film_queries.set_id, texto="Introduce el id de la película.", icono="film", texto_input="Id"),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Eliminar película", 
                                type="submit", 
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=  Film_queries.delete_film(),
                reset_on_submit=False
            ),
            max_width="450px",
        ),
    )
