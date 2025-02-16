'''archivo de gráficas'''
import reflex as rx
from videoflix.queries.consultar_estadisticas import UserStatistics

data = [
        {"name": "Películas", "minutos": UserStatistics.minutos_vistos_peliculas},
        {"name": "Series", "minutos": UserStatistics.minutos_vistos_series},
    ] 

colores = ["red", "green"] #en desuso

def grafica_total(data=data, color="accent"):
    '''función gráfica_total
    recibe unos datos en formato diccionaro e imprime una gráfica con los resultados'''
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="minutos",
            stroke=rx.color(color, 9),
            fill=rx.color(color, 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(),
        data=data,
        width="100%",
        height=250,
    )

def mostrar_minutos():
    '''función mostrar_minutos
    imprime en la web un mensaje con los minutos vistos por el usuario'''
    print("hola",UserStatistics.minutos_vistos)
    return rx.text(f"Minutos vistos: {UserStatistics.minutos_vistos_peliculas} + {UserStatistics.minutos_vistos_series}")