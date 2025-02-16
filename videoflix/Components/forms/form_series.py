import reflex as rx
from videoflix.Components.buttons import *
from videoflix.queries.seriesQueries import Series_queries
from videoflix.styles.colors import Color
from videoflix.styles.styles import MAX_WIDTH, Size
from ..inputs import input_form

def form_del_serie() -> rx.Component:
    ''' función form_delete_serie
    a través de la ID, elimina a una serie de la base de datos '''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("minus", size=26),
                rx.text("Eliminar Serie", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Elimina una serie",
            ),
            rx.alert_dialog.description(
                "Inserta la ID de la serie que quieres eliminar",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Id", name="id",
                        on_blur=Series_queries.set_id
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
                                "Eliminar serie", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=Series_queries.delete_serie(),
                reset_on_submit=True,
            ),
            max_width=MAX_WIDTH,
        ),
    )







def form_series() -> rx.Component:
    '''función form_series
    formulario mediante el cual el administrador puede añadir, editar o elimina una serie'''
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
                    "Introduce los datos de la serie a añadir",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                rx.heading("Instrucciones", size="4"),
                rx.text(rx.text.strong("""Si quieres eliminar una serie, introduce la id y pulsa el botón eliminar.
                                        Nota: ten en cuenta que al eliminar la serie se eliminarán todos
                                       los capítulos relacionados""", text_align="justify"),
                        "En caso de nuevas series, el campo id no es necesario. Para modificar una serie existente, rellenar el campo de id y SOLO los campos a modificar.", text_align="justify"),
                        rx.text("Por ejemplo, si quieres modificar solo la duración de un capítulo, añade la id de dicho capítulo y el campo duración", text_align="justify"),
                    direction="column",
                    spacing="5",
                    width="100%",
                    max_width=MAX_WIDTH
                ),
                rx.text("Haz clic en el botón para eliminar una serie"),
                form_del_serie(),
            ),
        input_form(accion=Series_queries.set_id, texto="Introduce la id de la serie a modificar.", icono="smile", texto_input="id"),
        input_form(accion=Series_queries.set_titulo, texto="Introduce el nombre de la serie.", icono="film", texto_input="Serie"),
        input_form(accion=Series_queries.set_num_temporadas, texto="Introduce el número de temporadas", icono="file-digit", texto_input="Número de temporadas"),
        input_form(accion= Series_queries.set_year, texto="Introduce el año de estreno", icono="calendar-search", texto_input="Año"),
        rx.text_area(placeholder="Introduce la sinopsis",name="Sinopsis",icon="film", on_blur=Series_queries.set_sinopsis),
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
                        ),
                        rx.text(""),
                    ),
                    id="upload1",
                    image_name= rx.selected_files("upload1")[0]._var_name,
                    border=f"1px dotted {Color.SECONDARY.value}",
                    padding="5em",
                ),
                rx.hstack(rx.foreach(rx.selected_files("upload1"),   rx.text ),
                )
            )
        ),
        rx.box(
            rx.checkbox(
                "¿Estás seguro de querer realizar los cambios?",
                default_checked=False,
                spacing="2",
            ),
            width="100%",
        ),
        rx.hstack(
            rx.button(
                "Subir serie",
                size="3", 
                on_click =  lambda: Series_queries.handle_upload_add( rx.upload_files(upload_id="upload1") ),        
                type="submit",
                width="100%",
                max_width="17em"
            ),
            rx.button(
                "Editar serie",
                size="3", 
                on_click=  rx.cond(
                        rx.upload_files(upload_id="upload1"),
                        Series_queries.handle_upload_edit(rx.upload_files(upload_id="upload1")),
                        Series_queries.handle_upload_edit(),    
                        ),
                reset_on_submit=True,
                type="submit",   
                width="100%",
                max_width="17em"             
            ),
            spacing="3",
            width="100%",
            align="center",
            padding_top=Size.DEFAULT.value,
            padding_x=Size.SMALL.value
        ),
        spacing="6",
        width="100%",
        max_width=MAX_WIDTH
    ),
