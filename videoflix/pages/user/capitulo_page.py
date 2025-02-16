import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size, VIDEO_STYLE, MAX_WIDTH
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.state.states import AuthState 
from videoflix.Components.buttons import confirm_button
from videoflix.queries.add_favourites import AddFavourites
from videoflix.queries.seriesQueries import Series_queries, CapituloState
    
@rx.page(route=CAPITULO, title=f"{Series_queries.titulo}, {CapituloState.titulo_capitulo}", on_load=[AuthState.check_login(),
                                                                                                CapituloState.get_capitulo()])
def capitulo_page():
    '''función capitulo_page
    retorna los componentes que dan forma a la ventana de un capitulo'''
    return rx.box(
        header(),
        rx.flex(
            logo_central("300px"),
            padding_top=Size.MAX_BIG.value,
            padding_x=Size.DEFAULT.value
        ),
        rx.vstack(
            rx.heading(f"{Series_queries.titulo}, temporada {CapituloState.temporada}: {CapituloState.titulo_capitulo}", padding_x=Size.DEFAULT.value),
            rx.box(
                rx.center(
                    rx.vstack(
                        rx.video(
                            url=CapituloState.video,
                            style=VIDEO_STYLE
                        ),
                        rx.card(
                            rx.vstack(
                                rx.hstack(
                                    confirm_button(text= "Marcar como visto", icono="circle-check-big", 
                                                    accion=[
                                                        AddFavourites.set_id_usuario(AuthState.user.id),
                                                        AddFavourites.set_id_capitulo(CapituloState.capitulo_id),          
                                                        AddFavourites.marcar_cap_como_visto()
                                                    ]
                                    ),
                                    confirm_button(text= "Añadir a favoritos",
                                                    accion=[
                                                        AddFavourites.set_id_usuario(AuthState.user.id),
                                                        AddFavourites.set_id_capitulo(CapituloState.capitulo_id),          
                                                        AddFavourites.marcar_como_favorito_cap()
                                                    ]
                                    ),
                                    rx.text(f"Duración: {CapituloState.duracion} minutos.")                                    
                                ),
                                rx.divider(),
                                rx.text(
                                    rx.text("Sinopsis:", weight="bold"),
                                    rx.text(CapituloState.sinopsis_capitulo, text_align="justify")
                                ),
                                width="100%",
                                max_width=MAX_WIDTH
                            ),
                        ),
                    ),
                ),
                width="100%",
                padding_bottom=Size.MAX_BIG.value,
                padding_x=Size.DEFAULT.value
            ),    
            footer(),
            width="100%"
        )
    )


