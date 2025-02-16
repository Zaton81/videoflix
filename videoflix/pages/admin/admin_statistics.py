import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import MAX_WIDTH, Size
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.state.states import AuthState
from videoflix.Components.graficas.graficas import grafica_total
from videoflix.queries.consultar_estadisticas import AdminStatistics

data = [
        {"name": "Películas", "minutos": AdminStatistics.minutos_vistos_peliculas},
        {"name": "Series", "minutos": AdminStatistics.minutos_vistos_series},
    ]

data2 = [
        {"name": "Películas", "minutos": AdminStatistics.minutos_vistos_peliculas2},
        {"name": "Series", "minutos": AdminStatistics.minutos_vistos_series2},
    ]
@rx.page(route=ADMIN_ESTADISTICAS, title=f"{TITTLE_USER} {AuthState.user.username}", on_load=AuthState.check_login_admin())
def admin_stadisticas() -> rx.Component:
    '''archivo admin_estadisticas
    retorna los componentes para la ventana de estadísticas del administrador
    desde la que el admin puede consultar y comparar los minutos vistos por el usuario'''
    return rx.box(
        header(),
        rx.heading(f"Hola, {AuthState.user.nombre}", margin_x="3em", padding_top=Size.VERY_BIG.value),
        rx.heading("Consulta los minutos visualizados por el usuario a través de su id", align="center", justify="center"),
        rx.center(
            
            rx.hstack(
                rx.vstack(
                    rx.card(
                        rx.vstack(
                            rx.text("Consultar las estadísticas del primer usuario"),
                            rx.input(
                                placeholder="Introduce la ID del usuario",
                                on_change=AdminStatistics.set_id_usuario
                            ),
                            rx.button(
                                "Consultar",
                                on_click= [lambda: 
                                        AdminStatistics.consultar_minutos_peliculas, 
                                        AdminStatistics.consultar_minutos_series, 
                                        AdminStatistics.mostrar_minutos_vistos,
                                        ]
                            )
                        ),
                        padding="20px",
                        margin="10px"
                    ),
                    rx.text(f"El usuario {AdminStatistics.id_usuario} ha visto un total de {AdminStatistics.minutos_vistos_peliculas} minutos en un total de {AdminStatistics.total_peliculas} películas."),
                    grafica_total(data=AdminStatistics.peliculas_vistas, color="red"),
                    rx.text(f"Ha visto un total de {AdminStatistics.minutos_vistos_series} minutos en un total de {AdminStatistics.total_series} series."),
                    grafica_total(data=AdminStatistics.series_vistas, color="green"),
                    rx.text(f"El total de minutos vistos es de {AdminStatistics.minutos_vistos} minutos."),
                    grafica_total(data, color="blue"),
                    width=MAX_WIDTH
                ),
                rx.divider(orientation="vertical", size="4", color_scheme="orange"),
                rx.vstack(
                    rx.card(
                        rx.vstack(
                            rx.text("Consultar las estadísticas del segundo usuario"),
                            rx.input(
                                placeholder="Introduce la ID del usuario",
                                on_change=AdminStatistics.set_id_usuario2
                            ),
                            rx.button(
                                "Consultar",
                                on_click= [lambda: 
                                        AdminStatistics.consultar_minutos_peliculas, 
                                        AdminStatistics.consultar_minutos_series, 
                                        AdminStatistics.mostrar_minutos_vistos,
                                        ]
                            )
                        ),
                        margin="10px",
                        padding="20px",
                    ),
                    rx.text(f"El usuario {AdminStatistics.id_usuario2} ha visto un total de {AdminStatistics.minutos_vistos_peliculas2} minutos en un total de {AdminStatistics.total_peliculas2} películas."),
                    grafica_total(data=AdminStatistics.peliculas_vistas2, color="orange"),
                    rx.text(f"Ha visto un total de {AdminStatistics.minutos_vistos_series2} minutos en un total de {AdminStatistics.total_series2} series."),
                    grafica_total(data=AdminStatistics.series_vistas2, color="yellow"),
                    rx.text(f"El total de minutos vistos es de {AdminStatistics.minutos_vistos2} minutos."),
                    grafica_total(data2, color="brown"),
                    width=MAX_WIDTH
                ),
            ),
            padding="20px",
            margin="10px",
            margin_bottom="40em",
            padding_bottom="10em",
            #padding_top="10em"
        ),
        footer(),
        width="100%",
        height="100vh",  
        display="flex",
        flex_direction="column",
        justify_content="space-between",
        flex="1",
    )