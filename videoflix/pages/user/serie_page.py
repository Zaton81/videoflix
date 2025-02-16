import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, MAX_WIDTH
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.state.states import AuthState 
from videoflix.queries.seriesQueries import Series_queries, CapituloState
from videoflix.styles.constants import BACKEND

@rx.page(route=SERIE, title=f"{Series_queries.titulo}", on_load=[AuthState.check_login(), Series_queries.get_serie2, 
                                                             CapituloState.get_temporadas, CapituloState.cargar_capitulos])
def serie_page():
    '''función serie_page
    retorna los componentes que dan forma a la ventana de una serie'''
    
    return rx.box(
        header(),
        rx.heading(Series_queries.serie_data.titulo, padding_x= Size.DEFAULT.value, padding_top=Size.VERY_BIG.value),
        logo_central("200px"),
        rx.vstack(
            rx.box(
                rx.center(
                    rx.hstack(
                        rx.image(
                            src=f"{BACKEND}/_upload/{Series_queries.portada}",  # Usa la ruta directa
                            alt=Series_queries.titulo, 
                            size= Size.VERY_BIG.value,
                            width="500px",
                            high="auto",
                            padding_bottom=Size.VERY_BIG.value,
                        ),
                        rx.vstack(
                            rx.card(
                                rx.vstack(
                                    rx.hstack(
                                        rx.icon("tv"),
                                        rx.text(f"Año de estreno {Series_queries.year}. Temporadas totales: {Series_queries.num_temporadas}. Temporadas disponibles: {Series_queries.tem_disponibles}"),                                    
                                    ),
                                    rx.divider(),
                                    rx.text(
                                        rx.text("Sinopsis:", weight="bold"),
                                        rx.text(Series_queries.sinopsis)
                                    ),
                                    rx.divider(),
                                    rx.text(f"Temporadas disponibles: {Series_queries.tem_disponibles}."),
                                    rx.foreach(CapituloState.temporadas, 
                                                lambda temporada:
                                                        rx.box(
                                                            rx.link(
                                                                rx.heading(f"Temporada {temporada}"),
                                                                href=f"/series/{Series_queries.id}/{temporada}", 
                                                        ),
                                                    ),
                                    ),
                                width="100%",
                                max_width=MAX_WIDTH
                                ),
                            ),
                        ),
                    ),
                ),
                width="100%",
            ),    
            footer(),
            width="100%"
        )
    )

@rx.page(route=TEMPORADA, title=f"{Series_queries.titulo}", on_load=[AuthState.check_login(), CapituloState.get_capitulos2])
def temporada_page() ->rx.Component:
    '''función temporada_page
    retorna los componentes que dan forma a la ventana de una temporada'''
    return rx.box(
        header(),
        rx.flex(
            logo_central("300px"),
            padding_top=Size.VERY_BIG.value
        ),
        rx.hstack(
            rx.image(
                                src=f"{BACKEND}/_upload/{Series_queries.portada}",  # Usa la ruta directa
                                alt=Series_queries.titulo, 
                                size= Size.VERY_BIG.value,
                                width="500px",
                                high="auto",
                            ),
            rx.vstack(
                rx.heading(f"{Series_queries.titulo}. Temporada {CapituloState.temporada}", size="9"),
                rx.box(
                    rx.center(
                        rx.vstack(
                            rx.foreach(
                                CapituloState.capitulos,
                                lambda cap:
                                    rx.box(
                                        rx.vstack(
                                            rx.link(
                                                rx.heading(f"Capítulo {cap.num_capitulo}: {cap.titulo_capitulo}"),
                                                href=f"/series/{Series_queries.id}/{CapituloState.temporada}/{cap.id}",
                                            ),
                                            rx.text(f"Capítulo {cap.num_capitulo}"),
                                            rx.text(f"Duración: {cap.duracion} minutos"),
                                            rx.text(cap.sinopsis_capitulo),
                                            columns=2,
                                            gap="4",
                                            width="100%",                                                align="start",
                                        ),
                                        rx.divider(),
                                        width="100%",
                                        padding="4",
                                        padding_bottom= Size.MAX_BIG.value
                                    )
                            ),
                        ),
                    ),
                    width="100%",
                    padding_x= Size.DEFAULT.value
                ),
            ),
        ),
        footer(),
        width="100%"
    )
