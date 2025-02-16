import reflex as rx
from videoflix.models import Capitulos
from sqlmodel import select

class Chapter_queries(rx.State):
    '''clase Chapter_queries
    desde ella se accede a la DB y se añaden, editan y eliminan capítulos de series
    También se recuperan los datos de la DB
    serie_id: id de la serie a la que pertenece el capítulo
    titulo_capitulo: el título del capítulo
    num_capitulo: número del capítulo
    num_temporada: número de la temporada a la que pertenece el capítulo
    sinopsis_capitulo: sinopsis del capítulo
    duracion: duración en minutos del capitulo
    video: link o código del vídeo del capítulo
    id: id del capítulo
    capitulos : lista de capítulos
    '''
    serie_id: int = None
    titulo_capitulo: str = None
    num_capitulo: int = None
    num_temporada: int = None
    sinopsis_capitulo: str = None
    duracion: int = None
    video: str = None
    id: str = None
    capitulos :list =[]
    img: list[str] =[]

    @rx.event
    async def add_chapter(self): #files: list[rx.UploadFile]
        '''función add_film
        recibe los datos de un formulario y añade la serie a la DB
        En caso de que algún dato sea incorrecto, retorna un mensaje de información'''

        with rx.session() as session:
            try:
                print(self.titulo_capitulo)
                capitulo=Capitulos(titulo_capitulo=self.titulo_capitulo, num_temporada= self.num_temporada, num_capitulo= self.num_capitulo, 
                                duracion= self.duracion, video= self.video, sinopsis_capitulo= self.sinopsis_capitulo, serie_id= self.serie_id)
                print(capitulo)
                session.add(capitulo)
                session.expire_on_commit = False
                session.commit()
                titulo=self.titulo_capitulo
                Chapter_queries.resets(self)
                return rx.window_alert(f"Capitulo {titulo} añadida correctamente.")
            except:
                return rx.window_alert("Algo ha fallado. Inténtelo de nuevo.")
    
    def edit_chapter(self):
        '''función add_film
        recibe los datos de un formulario y modifica la serie en la DB
        En caso de que algún dato sea incorrecto, retorna un mensaje de información
        Si por contra no encuentra la serie porque no se ha añadido la id, manda los datos a la función add_serie
        Si no encuentra el id, lanza un mensaje de error'''
        if self.id is None or self.id =="":
            Chapter_queries.resets(self)
            return rx.window_alert("Introduce la id de la serie que quieras modificar.")
        else:
            try:
                with rx.session() as session:
                    if session.exec(select(Capitulos).where(Capitulos.id == self.id) ).first():
                        capitulo=session.exec(select(Capitulos).where(Capitulos.id == self.id) ).first()
                        if self.titulo_capitulo not in [None, ""]:
                            capitulo.titulo_capitulo=self.titulo_capitulo
                        if self.num_temporada not in [None, ""]:
                            capitulo.num_temporada=self.num_temporada
                        if self.num_capitulo not in [None, ""]:
                            capitulo.num_capitulo=self.num_capitulo
                        if self.duracion not in [None, ""]:
                            capitulo.duracion=self.duracion
                        if self.video not in [None, ""]:
                            capitulo.video=self.video
                        if self.sinopsis_capitulo not in [None, ""]:
                            capitulo.sinopsis_capitulo=self.sinopsis_capitulo
                        if self.serie_id not in [None, ""]:
                            capitulo.serie_id=self.serie_id
                        session.add(capitulo)
                        session.commit()
                        titulo=self.titulo_capitulo
                        Chapter_queries.resets(self)
                        
                        return  rx.window_alert(f"Capitulo {titulo} modificada correctamente.")
                    else:
                        Chapter_queries.resets(self)
                        return rx.window_alert(f"No hay ninguna serie en la base de datos con esa id.")

            except:
                Chapter_queries.resets(self)
                return rx.window_alert("Algo ha fallado, inténtalo de nuevo mas tarde."), self.resets()
    
    @rx.event
    def delete_serie(self):
        '''delete_series
        recibe la id de la serie y la elimina de la base de datos'''
        print(self.id)
        try:
            with rx.session() as session:
                    capitulo = session.exec(
                        Capitulos.select().where(
                            Capitulos.id == self.id
                        )
                    ).first()
                    print(capitulo)
                    session.delete(capitulo)
                    session.commit()
                    
                    Chapter_queries.resets(self)
                    return rx.window_alert(f"Serie {self.titulo_capitulo} eliminada correctamente")
        except:
            return rx.window_alert(f"La serie no se ha podido eliminar.")
        
    def resets(self):
        '''resets
        reinicia los datos de la clase'''
        self.serie_id = None
        self.titulo_capitulo = None
        self.num_capitulo = None
        self.num_temporada = None
        self.sinopsis_capitulo = None
        self.duracion = None
        self.video = None
        self.id = None
        





