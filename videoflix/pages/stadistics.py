import reflex as rx
from videoflix.styles.constants import *
from videoflix.styles.styles import Size
from videoflix.Components.footer import footer
from videoflix.Components.navbar import navbar_user as header
from videoflix.Components.logo import logo_central
from videoflix.state.states import AuthState 
from videoflix.queries.filmQueries import Film_queries
from videoflix.Components.graficas.graficas import grafica_total, mostrar_minutos
from videoflix.queries.consultar_estadisticas import UserStatistics

@rx.page(route=ESTADISTICAS, title=f"{ESTADISTICAS_DESCRIPCION} {AuthState.user.username}", 
        on_load=[AuthState.check_login(),
                Film_queries.set_user_id(AuthState.user.id),
                UserStatistics.consultar_minutos_peliculas,
                UserStatistics.consultar_minutos_series,
                UserStatistics.mostrar_minutos_vistos])  
def estadisticas() ->rx.Component:
    '''fnción estadisticas.
    recupera las estadísticas de un usuario'''
    
    return rx.box(
        header(),
        rx.hstack(
            logo_central("400px"),
            rx.heading(f"Hola, {AuthState.user.nombre}, estas son tus estadísticas:", size="6",
                    padding_top="300px",
                    bottom="0"),
            padding_top=Size.MAX_BIG.value
        ),
        rx.center(
            rx.vstack(
                rx.divider(),
                rx.text(f"Has visto un total de {UserStatistics.minutos_vistos_peliculas} minutos en un total de {UserStatistics.total_peliculas} películas."),
                grafica_total(data=UserStatistics.peliculas_vistas, color="red"),
                mostrar_minutos(),               
                rx.divider(),
                rx.text(f"Has visto un total de {UserStatistics.minutos_vistos_series} minutos en un total de {UserStatistics.total_series} series."),
                grafica_total(data=UserStatistics.series_vistas, color="green"),
                rx.divider(),
                rx.text(f"El total de minutos vistos es de {UserStatistics.minutos_vistos} minutos."),
                grafica_total(),
                rx.divider(),
                padding_bottom=Size.MAX_BIG.value,
                width="600px"
            ),

        ),
        footer(),
        width="100%"
    )

