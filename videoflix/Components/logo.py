import reflex as rx
from videoflix.styles.styles import Size

def logo_central(max_width="600px", height="50%") ->rx.Component:
                '''función logo
                recibe los parámetros
                max_width: el tamaño ancho
                height; la altura
                devuelve una imagen de la web'''
                return rx.image(
                    src="/logo.svg",
                    max_width=max_width,
                    border_radius=Size.VERY_BIG.value,
                    height=height,
                    padding = Size.SMALL.value
                ),