import reflex as rx
from videoflix.queries.seriesQueries import Series_queries
from videoflix.queries.multiples_queries import consultarDB, FavoritosState
from videoflix.models import  Series
from videoflix.styles.constants import BACKEND
from videoflix.styles.styles import Size

def listar(serie: object):
    # Imprime el directorio de uploads

    print(serie)
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.card(
                    rx.link(
                        rx.image(
                            src=f"{BACKEND}/_upload/{serie.portada}",  # Usa la ruta directa
                            alt=serie.titulo, 
                            size= Size.VERY_BIG.value,
                            width="200px",
                            high="auto",
                        ),
                        href=f"/series/{serie.id}",
                        on_click=lambda: [Series_queries.set_id(serie.id)]
                    ),
                    width="25%"
                ),
                rx.card(
                    rx.vstack(
                        rx.heading(serie.titulo, size="4"),
                        rx.text(
                            f'''Temporadas: {serie.num_temporadas} minutos.
                            Año de estreno: {serie.year}.'''
                        ),
                        rx.text(
                            f"Sinopsis:{serie.sinopsis}.",
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

@rx.event
def listar_cap(cap: object):
    '''Función listar cap
    recibe un capitulo e imprime en la web los resultados'''
    return rx.card(      
        rx.link(
            rx.heading(cap.titulo_capitulo, size="6"),
            href=f"/series/{cap.serie_id}/{cap.num_temporada}/{cap.id}",
        ),
        rx.text(
            f'''Duración: {cap.duracion} minutos.
            Temporada: {cap.num_temporada}.
            Capítulo: {cap.num_capitulo}.'''
        ),
        rx.text(
            f"Sinopsis:{cap.sinopsis_capitulo}.",
            text_align="justify",
            padding_botton= Size.DEFAULT.value
        ),
        rx.divider(),
        margin_y= Size.BIG.value,
        margin_x= Size.BIG.value,
        
    )


def mostrar_serie() -> rx.Component:
    '''Función que imprime los títulos de las películas en la web utilizando un estado de Reflex'''
    return rx.box(
        rx.heading("Las series de Videoflix", size="8", text_align="center"),        
        rx.foreach(consultarDB(Series), listar),
        spacing="4",
        padding="4"
    )

def mostrar_favourite_caps(accion=FavoritosState.cap_favoritos) -> rx.Component:
    '''Función que imprime los títulos de los capítulos en la web utilizando un estado de Reflex'''

    print(FavoritosState.cap_favoritos)
    return rx.box(
        rx.heading("Capítulos Favoritos", size="8", text_align="center"),
        rx.foreach(accion, listar_cap),
        spacing="4",
        padding="4"
    )