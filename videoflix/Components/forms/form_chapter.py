import reflex as rx
from videoflix.Components.buttons import *
from videoflix.queries.chapterQueries import Chapter_queries
from videoflix.styles.styles import MAX_WIDTH, Size
from ..inputs import input_form

def form_del_chapter() -> rx.Component:
    ''' función form_del_chapter
    a través de la ID, elimina un capítulo de la base de datos '''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("minus", size=26),
                rx.text("Eliminar Capítulo", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Elimina un capítulo",
            ),
            rx.alert_dialog.description(
                "Inserta la ID del capítulo que quieres eliminar",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Id", name="id",
                        on_blur=Chapter_queries.set_id
                    ),
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
                                "Eliminar capítulo", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=Chapter_queries.delete_serie(),
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )

def form_chapter() -> rx.Component:
    '''función form_chapter
    formulario mediante el cual el administrador puede añadir, editar o elimina un capítulo de serie'''
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
                    "Editor de series",
                    size="8",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                rx.heading(
                    "Introduce los datos del capítulo a añadir",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                rx.heading("Instrucciones", size="4"),
                rx.text(rx.text.strong("Si quieres eliminar un capítulo, introduce la id y pulsa el botón eliminar.", text_align="justify"),
                        "En caso de nuevos capñitulos, el campo id no es necesario. Para modificar un cpitulo existente, rellenar el campo de id y SOLO los campos a modificar.", text_align="justify"),
                        rx.text("Por ejemplo, si quieres modificar solo la duración de un capítulo, añade la id de dicho capítulo y el campo duración", text_align="justify"),
                    direction="column",
                    spacing="5",
                    width="100%",
                    max_width=MAX_WIDTH
                ),
                rx.text("haz clic en el botón para eliminar un capítulo"),
                form_del_chapter(),
            ),
        input_form(accion=Chapter_queries.set_id, texto="Introduce la id del capítulo a modificar.", icono="smile", texto_input="id"),
        input_form(accion=Chapter_queries.set_serie_id, texto="Introduce la id la serie.", icono="smile", texto_input="id"),
        input_form(accion=Chapter_queries.set_titulo_capitulo, texto="Introduce el nombre del capítulo.", icono="film", texto_input="Título"),
        input_form(accion=Chapter_queries.set_num_temporada, texto="Introduce el número de la temporada", icono="file-digit", texto_input="Número de temporada"),
        input_form(accion=Chapter_queries.set_num_capitulo, texto="Introduce el número del capítulo", icono="file-digit", texto_input="Número de capítulo"),
        input_form(accion= Chapter_queries.set_duracion, texto="Introduce la duración en minutos", icono="calendar-search", texto_input="minutos"),
        input_form(accion=Chapter_queries.set_video, texto="Introduce el cósigo del vídeo", icono="film", texto_input="Vídeo"),
        rx.text_area(placeholder="Introduce la sinopsis",name="Sinopsis",icon="film", on_blur=Chapter_queries.set_sinopsis_capitulo),
        rx.box(
            rx.hstack(
                rx.button(
                    "Subir capítulo",
                    size="3", 
                    on_click =  lambda: Chapter_queries.add_chapter(),        
                    type="submit",
                    width="100%",
                    max_width="18em"
                ),
                rx.button(
                    "Editar capítulo",
                    size="3", 
                    on_click= Chapter_queries.edit_chapter(),
                    reset_on_submit=True,
                    type="submit",
                    width="100%",
                    max_width="18em"                
                ),
                spacing="3",
                margin="3",
                padding_top=Size.SMALL.value
            ),
        spacing="6",
        width="100%",
        max_width="28em"
    ),
    )
