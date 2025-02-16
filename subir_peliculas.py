'''Archivo utilizado para subir películas a la base de datos a partir de un archivo CSV'''

import pandas as pd
import reflex as rx

from videoflix.models import Pelicula

# Leer el archivo CSV
df = pd.read_csv("05_05_imdb_elenco.csv")

# Ordenar el DataFrame por la columna "year" en orden descendente
df_ordenado = df.sort_values(by="year", ascending=False)

# Recuperar solo las filas con títulos distintos
df_titulos_distintos = df_ordenado.drop_duplicates(subset=["title"])

# Mostrar las primeras filas del DataFrame con títulos distintos
print(df_titulos_distintos.head())

with rx.session() as session:
    for pelicula, columna in df_titulos_distintos.head(30).iterrows():

        pelicula_= Pelicula(
            titulo=columna.title,
            year=columna.year,
            duracion= 125,
            portada="portada.jpg",
            sinopsis='''En un pequeño pueblo costero de España, Clara, una talentosa pintora con una vida aparentemente tranquila, descubre una antigua carta escondida en el ático de su casa. La carta, fechada en 1915, está dirigida a una mujer llamada Isabel y habla de un amor prohibido y un tesoro escondido que podría cambiar el destino del pueblo.
                Intrigada por el misterio, Clara decide investigar y descubre que Isabel era una de sus antepasadas. A medida que desentraña el pasado, Clara se encuentra atrapada en una serie de eventos que la llevan a vivir momentos del pasado como si fueran el presente. Estos viajes temporales la enfrentan a secretos familiares, viejas rivalidades y una conspiración que ha perdurado a través de generaciones.
                Con la ayuda de Marcos, un historiador local, y de una serie de visiones y pistas del pasado, Clara debe encontrar el tesoro antes de que caiga en las manos equivocadas. En el proceso, descubre que el verdadero tesoro no es lo que esperaba, sino algo mucho más valioso: el amor y la unión de su familia.''',
            video='''<iframe width="560" height="315" src="https://www.youtube.com/embed/wo_EIFELKcI?si=e_pStze5eza9a2_B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'''
        )
        session.add(pelicula_)
    session.commit()