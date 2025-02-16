import reflex as rx
from videoflix.queries.filmQueries import Film_queries
from videoflix.queries.multiples_queries import FavoritosState
from videoflix.styles.constants import BACKEND
from videoflix.styles.styles import Size


def listar(pelicula: object):
    '''función listar
    recibe  un objeto de tipo película y retorna un box de reflex con los resultados'''
    print(pelicula)
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.link(
                        rx.image(
                            src=f"{BACKEND}/_upload/{pelicula.portada}",  # Usa la ruta directa
                            alt=pelicula.titulo, 
                            size= Size.VERY_BIG.value,
                            width="200px",
                            high="auto",
                        ),
                        href=f"/films/{pelicula.id}",
                        on_click=lambda: [Film_queries.set_id(pelicula.id)]
                    ),
                    width="25%"
                ),
                rx.card(
                    rx.vstack(
                        rx.link(
                        rx.heading(pelicula.titulo, size="4"),
                        href=f"/films/{pelicula.id}",
                        on_click=lambda: [Film_queries.set_id(pelicula.id)]
                        ),
                        rx.text(
                            f'''Duración: {pelicula.duracion} minutos.
                            Año de estreno: {pelicula.year}.'''
                        ),
                        rx.text(
                            f"Sinopsis:{pelicula.sinopsis}.",
                            text_align="justify"
                        )
                    ),
                    width="75%"    
                ),
                margin="4",
                padding_x="4",
                width="100%"
            ),
            padding_bottom= Size.BIG.value,
        ),
        rx.divider(),
        margin_y= Size.BIG.value,
        margin_x= Size.BIG.value,
    )



def mostrar_pelicula(texto= "Tus Películas favoritas", accion=FavoritosState.favoritos) -> rx.Component:
    '''Función que imprime los títulos de las películas en la web utilizando un estado de Reflex
    recibe una acción de consulta a la base de datos y lo imprime en la web'''

    return rx.box(
        rx.heading(texto, size="8", text_align="center"),
        rx.foreach(accion, listar),
        spacing="4",
        padding="4"
    )




