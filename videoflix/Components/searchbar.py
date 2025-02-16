import reflex as rx
from videoflix.models import Pelicula, Series, Capitulos
from videoflix.styles.colors import Color

def searchbar() -> rx.Component:
    '''función searchbar
    retorna un input o barra buscadora donde buscar en la base de datos'''
    return rx.box(
        rx.input(
            placeholder="Search",
            background_color=Color.PURPLE.value,
            _placeholder={"color": "white"},
            on_change=SearchState.search_content,
            value=SearchState.search_query,
        ),
        rx.icon(
            tag="search",
            position="absolute",
            right="0.75rem",
            top="0.5rem",
            color="#9CA3AF",
            width="1rem",
            height="1rem",
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Resultados de búsqueda"),
                rx.vstack(
                    rx.heading("Películas", size="3"),
                    rx.foreach(
                        SearchState.peliculas,
                        lambda p: rx.link(
                            rx.text(p['titulo']) ,
                            href=f"/films/{p['id']}"
                            ),
                    ),
                    rx.heading("Series", size="3"),
                    rx.foreach(
                        SearchState.series,
                        lambda s: rx.link(
                            rx.text(s['titulo']),
                            href=f"/series/{s['id']}"
                        ),
                    ),
                    rx.heading("Capítulos", size="3"),
                    rx.foreach(
                        SearchState.capitulos,
                        lambda c: rx.link(
                            rx.text(c['titulo']),
                            href=f"/series/{c['serie_id']}/{c['num_temporada']}/{c['id']}"
                        )
                            
                        
                    ),
                    spacing="4",
                ),
                rx.dialog.close(
                    rx.button("Cerrar", size="3"),
                    on_click=SearchState.toggle_dialog,
                    
                ),
                max_width="450px",
            ),
            open=SearchState.dialog_open,
            on_open_change=SearchState.toggle_dialog,
        ),
        position="relative",
    )
    

class SearchState(rx.State):
    '''clase SearchState
    a través de la función searchabar (o cualquier otra que usemos en un futuro) realiza búsquedas en la base de datos
    search_query: el texto introducido en el input
    peliculas: listado de películas encontradas
    series; lista de series encontradas
    capítulos:lista de capítulos encontrados
    dialog_open estado booleano con el que manejar la ventana'''
    search_query: str = ""
    peliculas: list[dict] = []  
    series: list[dict] = []
    capitulos: list[dict] = []
    dialog_open: bool = False  

    @rx.event
    async def search_content(self, value: str):
        self.search_query = value
        self.dialog_open = len(value) >= 2
        if len(value) >= 2:
            with rx.session() as session:
                # Convertir los resultados a diccionarios
                self.peliculas = [
                    {"titulo": p.titulo,
                    "id": p.id} 
                    for p in session.exec(
                        Pelicula.select().where(
                            Pelicula.titulo.contains(value)
                        )
                    ).all()
                ]
                
                self.series = [
                    {"titulo": s.titulo,
                    "id": s.id}
                    for s in session.exec(
                        Series.select().where(
                            Series.titulo.contains(value)
                        )
                    ).all()
                ]
                
                self.capitulos = [
                    {"titulo": c.titulo_capitulo,
                    "num_temporada": c.num_temporada,
                    "serie_id":c.serie_id,
                    "id": c.id}
                    for c in session.exec(
                        Capitulos.select().where(
                            Capitulos.titulo_capitulo.contains(value)
                        )
                    ).all()
                ]
                print (self.peliculas)
                print (self.capitulos)
                print (self.series)
    
    @rx.event
    async def toggle_dialog(self):
        self.dialog_open = not self.dialog_open