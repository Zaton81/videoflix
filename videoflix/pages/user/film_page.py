import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, VIDEO_STYLE, MAX_WIDTH
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.state.states import AuthState 
from videoflix.queries.filmQueries import Film_queries
from videoflix.Components.buttons import confirm_button
from videoflix.queries.add_favourites import AddFavourites

@rx.page(route=FILM, title=f"{Film_queries.titulo}", on_load=[AuthState.check_login(), Film_queries.get_film()])
def film_page():
    '''función film_page
    retorna los componentes que dan forma a la ventana de una película'''

    return rx.box(
        header(),
        rx.vstack(
            rx.box(
                rx.center(
                    rx.hstack(
                        rx.vstack(
                            logo_central("400px"),
                            rx.card(
                                rx.vstack(
                                    rx.heading(Film_queries.film_data["titulo"]),
                                    rx.image(
                                        src=f'{BACKEND}/_upload/{Film_queries.portada}',  # Usa la ruta directa
                                        alt=Film_queries.titulo, 
                                        size= Size.VERY_BIG.value,
                                        width="300px",
                                        high="auto",
                                        padding_bottom=Size.MAX_BIG.value
                                    ),
                                ),
                            ),
                        ),
                        align="start", 
                        margin_right=Size.MAX_BIG.value
                    ),
                    rx.divider(orientation="vertical"),
                    rx.center(
                        rx.vstack(
                            rx.video(
                                url=Film_queries.video,
                                style=VIDEO_STYLE
                            ),
                            rx.card(
                                rx.vstack(
                                    rx.hstack(
                                        confirm_button(text= "Marcar como visto", icono="circle-check-big", 
                                                        accion=[
                                                            AddFavourites.set_id_usuario(AuthState.user.id),
                                                            AddFavourites.set_id_pelicula(Film_queries.id),          
                                                            AddFavourites.marcar_como_vista()
                                                        ]
                                        ),
                                        confirm_button(text= "Añadir a favoritos",
                                                        accion=[
                                                            AddFavourites.set_id_usuario(AuthState.user.id),
                                                            AddFavourites.set_id_pelicula(Film_queries.id),          
                                                            AddFavourites.marcar_como_favorito()
                                                        ]
                                        ),
                                        rx.text(f"Duración: {Film_queries.duracion} minutos. Año de estreno {Film_queries.year} ")                                    
                                    ),
                                    rx.divider(),
                                    rx.text(
                                        rx.text("Sinopsis:", weight="bold"),
                                        rx.text(Film_queries.sinopsis)
                                    ),
                                    width="100%",
                                    max_width=MAX_WIDTH
                                ),
                            ),
                        ),
                    ),
                ),
                width="100%",
                padding_y= Size.VERY_BIG.value,
                padding_top= Size.MAX_BIG,
                justify="between",
                padding_x= Size.DEFAULT.value
            ),    
            footer(),
            width="100%",
            
        )
    )


