import reflex as rx
from videoflix.models import Capitulos, Series
from sqlmodel import select
from sqlalchemy import func, select
from videoflix.state.states import AuthState

class Series_queries(rx.State):
    '''clase Series_queries
    desde ella se accede a la DB y se añaden, editan y eliminan series
    También se recuperan los datos de la DB
    titulo: el título de la serie
    year: año de estreno de la serie
    portada: nombre de la imagen de portada de la serie
    sinopsis: sinopsis de la serie
    num_temporadas: número de temporadas de la serie
    nuevo_titulo: el nuevo título si se modifica la serie
    id: id de la serie en la base de datos
    series : listado de series
    img: list[str] =[] imagen (en desuso)
    serie_data: diccionario con los datos de la serie
    temporadas: listado de temporadas de la serie
    capitulos_temporada: lista de capitulos por temporada
    tem_disponibles: el número de temporadas de la serie que están disponibles
    '''
    titulo: str = None
    year: int = None
    portada: str = None
    sinopsis: str = None
    num_temporadas: int = None
    nuevo_titulo: str = None
    id: str = None
    series :list =[]
    img: list[str] =[]
    serie_data: dict = {}
    temporadas: list = None
    capitulos_temporada: list[Capitulos] = []
    tem_disponibles: int = 0
    
    @rx.event
    async def add_serie(self): #files: list[rx.UploadFile]
        '''función add_film
        recibe los datos de un formulario y añade la serie a la DB
        En caso de que algún dato sea incorrecto, retorna un mensaje de información'''

        

        with rx.session() as session:
            try:
                print(self.titulo, print(self.portada))
                serie=Series(titulo=self.titulo, year= self.year, portada= self.portada, sinopsis= self.sinopsis, num_temporadas= self.num_temporadas)
                print(serie)
                session.add(serie)
                session.expire_on_commit = False
                session.commit()
                titulo=self.titulo
                Series_queries.resets(self)
                return rx.window_alert(f"Serie {titulo} añadida correctamente.")
            except:
                return rx.window_alert("Algo ha fallado. Inténtelo de nuevo.")
    
    def edit_serie(self):
        '''función add_film
        recibe los datos de un formulario y modifica la serie en la DB
        En caso de que algún dato sea incorrecto, retorna un mensaje de información
        Si por contra no encuentra la serie porque no se ha añadido la id, manda los datos a la función add_serie
        Si no encuentra el id, lanza un mensaje de error'''
        if self.id is None or self.id =="":
            Series_queries.resets(self)
            return rx.window_alert("Introduce la id de la serie que quieras modificar.")
        else:
            try:
                with rx.session() as session:
                    if session.exec(select(Series).where(Series.id == self.id) ).first():
                        serie=session.exec(select(Series).where(Series.id == self.id) ).first()
                        if self.titulo is not None:
                            serie.titulo= self.titulo
                        if self.year is not None:
                            serie.year = self.year
                        if self.portada is not None:
                            serie.portada = self.portada
                        if self.num_temporadas is not None:
                            serie.num_temporadas = self.num_temporadas
                        if self.sinopsis is not None:
                            serie.sinopsis = self.sinopsis
                        session.add(serie)
                        session.commit()
                        titulo=self.titulo
                        Series_queries.resets(self)
                        
                        return  rx.window_alert(f"Serie {titulo} modificada correctamente.")
                    else:
                        Series_queries.resets(self)
                        return rx.window_alert(f"No hay ninguna serie en la base de datos con esa id.")

            except:
                Series_queries.resets(self)
                return rx.window_alert("Algo ha fallado, inténtalo de nuevo mas tarde."), self.resets()
    
    @rx.event
    async def get_series(self, files: list [rx.UploadFile],):
        await self.handle_upload(files)
        return self.add_serie()
            
    @rx.event
    def delete_serie(self):
        '''delete_series
        recibe la id de la serie y la elimina de la base de datos'''
        print(self.id)
        try:
            with rx.session() as session:
                    capitulos=session.exec(
                        Capitulos.select().where(
                            Capitulos.serie_id == self.id
                        )
                    ).all()
                    serie = session.exec(
                        Series.select().where(
                            Series.id == self.id
                        )
                    ).first()
                    print(serie)
                    for capitulo in capitulos:
                        session.delete(capitulo)
                    session.delete(serie)
                    session.commit()
                    
                    Series_queries.resets(self)
                    return rx.window_alert(f"Serie {self.titulo} eliminada correctamente")
        except:
            return rx.window_alert(f"La serie no se ha podido eliminar.")
        
    @rx.event
    async def handle_upload_add(self, files: list[rx.UploadFile] = None):
        """método handle_upload
        carga la imagen, recoge el nombre de la misma y la recoge para guardarla en la base de datos.
        Args:
        files: los archivos a subir.
        tipo: si es añadir o editar.
        """
        if files is not None:
            try:    
                for file in files:
                    upload_data = await file.read()
                    
                    outfile = rx.get_upload_dir() / file.filename
                    # Save the file.
                    with outfile.open("wb") as file_object:
                        file_object.write(upload_data)

                    # Update the img var.
                    self.img.append(file.filename)
                    print(file.filename) 
                    self.portada=file.filename
                    #print(tipo)
            except:
                pass             
            return Series_queries.add_serie() 
    @rx.event
    async def handle_upload_edit(self, files: list[rx.UploadFile] = None):
        """método handle_upload
        carga la imagen, recoge el nombre de la misma y la recoge para guardarla en la base de datos.
        Args:
        files: los archivos a subir.
        tipo: si es añadir o editar.
        """
        if files is not None:
            try:    
                for file in files:
                    upload_data = await file.read()
                    
                    outfile = rx.get_upload_dir() / file.filename
                    # Save the file.
                    with outfile.open("wb") as file_object:
                        file_object.write(upload_data)

                    # Update the img var.
                    self.img.append(file.filename)
                    print(file.filename) 
                    self.portada=file.filename
                    #print(tipo)
            except:
                pass             
            return Series_queries.edit_serie() 
    @rx.event
    def get_serie(self):
        print(self.id)
        with rx.session() as session:
            serie = session.exec(Series.select().where(Series.id == Series_queries.id)).first()
            self.titulo = serie.titulo
            self.year = serie.year
            self.portada = serie.portada
            self.sinopsis = serie.sinopsis
            self.num_temporadas = serie.num_temporadas
            self.id = serie.id
            print(serie)

    async def  get_serie2(self):
        '''función get_serie2
        extrae los datos de la película de la base de datos
        a diferencia de la anterior, la id la recoge de los parámetros de la ruta de la web'''
        serie_id = self.router.page.params["serie"]
        #print(film_id)
        with rx.session() as session:
            serie = session.exec(Series.select().where(Series.id == serie_id)).first()
            self.serie_data = serie
            self.id = serie.id
            self.titulo = serie.titulo
            self.year = serie.year
            self.portada = serie.portada
            self.num_temporadas = serie.num_temporadas
            self.sinopsis = serie.sinopsis
            #contamos el número de temporadas disponibles
            temporadas = session.exec( select(func.count(func.distinct(Capitulos.num_temporada)))
            .where(Capitulos.serie_id == serie_id)
        ).scalar()
            self.tem_disponibles = temporadas
            #contamos el número de capítulos por temporada
            self.set_temporadas()
            

    def set_temporadas(self) -> list:
        '''crea una lista con el número de temporadas de la serie para poder iterar sobre ella'''
        self.temporadas = list(range(1, self.tem_disponibles + 1))
        num_temporadas = list(range(1, self.tem_disponibles + 1))
        return num_temporadas 

        
    def resets(self):
        '''resets
        reinicia los datos de la clase'''
        self.titulo = None
        self.year = None
        self.portada = None
        self.sinopsis = None
        self.num_temporadas = None
        self.nuevo_titulo = None
        self.id = None
        self.series = []

class CapituloState(rx.State):

    '''clase CapituloState
    recibe el id de la serie y el número de la temporada y retorna los capítulos de la misma
    serie_id: la id de la serie
    temporada: temporada de la serie
    capitulos: lista de capitulos
    titulo_capitulo: titulo de capitulos
    num_capitulo: el número del capítulo (distinto de la id)
    sinopsis_capitulo: sinopsis del capítulo
    video: código o link del capítulo
    duracion: dutación en minutos del capítulo
    num_temporada: número de temporada al que pertenece el capítulo
    capitulo_id: id del capítulo
    temporadas: lista de temporadas de la serio
    capitulos_por_temporada: diccionario con los capítulos por temporada de la serie
    '''
    serie_id: int = None
    temporada: int = None
    capitulos: list[Capitulos] = []
    titulo_capitulo: str = None
    num_capitulo: int = None
    sinopsis_capitulo: str = None
    video: str = None
    duracion: int = None
    num_temporada: int = None
    capitulo_id: int = None
    temporadas: list = []
    capitulos_por_temporada: dict = {}  

    def on_load(self):
        """Carga inicial de datos"""
        self.cargar_capitulos()
    
    @rx.event
    async def get_capitulos2(self):
        '''función get_capitulos
        extrae los capítulos de la base de datos'''
        self.serie_id = self.router.page.params["serie"]
        self.temporada = self.router.page.params["temp"]
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            capitulos = session.exec(
                Capitulos.select().where(Capitulos.serie_id == self.serie_id, Capitulos.num_temporada == self.temporada)
            ).all()
            self.capitulos = capitulos
    
    @rx.event
    async def get_capitulo(self):
        '''función get_capitulo
        extrae los datos del capítulo de la base de datos'''
        self.serie_id = self.router.page.params["serie"]
        self.temporada = self.router.page.params["temp"]
        self.capitulo_id = self.router.page.params["cap"]
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            capitulo = session.exec(
                Capitulos.select().where(Capitulos.serie_id == self.serie_id, Capitulos.id == self.capitulo_id)
            ).first()
            self.titulo_capitulo = capitulo.titulo_capitulo
            self.num_capitulo = capitulo.num_capitulo
            self.sinopsis_capitulo = capitulo.sinopsis_capitulo
            self.video = capitulo.video
            self.duracion = capitulo.duracion
            self.num_temporada = capitulo.num_temporada
            self.capitulo_id = capitulo.id
        


    @rx.event
    async def cargar_capitulos(self):
        serie_id = self.router.page.params["serie"]
        with rx.session() as session:
            for temporada in self.temporadas:
                caps = session.exec(
                    Capitulos.select().where(
                        Capitulos.serie_id == serie_id,
                        Capitulos.num_temporada == temporada
                    )
                ).all()
                self.capitulos_por_temporada[temporada] = caps
            print (self.capitulos_por_temporada)


    @rx.event    
    async def enviar_capitulo(self, temporada:int ) -> list:
        '''función enviar_capitulo
        recibe el id del capítulo y lo envía a la página del capítulo'''
        serie_id= Series_queries.id
        
    
        with rx.session() as session:
            capitulos = session.exec(
                Capitulos.select().where(Capitulos.serie_id == serie_id, Capitulos.num_temporada == temporada)
            ).all()
        self.capitulos = capitulos

        return capitulos

    def get_serie_id(self):

        self.serie_id = self.router.page.params["serie"]
        
    def get_temporadas(self):
        '''función get_temporadas'''
        serie_id = self.router.page.params["serie"]
        with rx.session() as session:
            #contamos el número de temporadas disponibles
            temporadas = session.exec( select(func.count(func.distinct(Capitulos.num_temporada)))
            .where(Capitulos.serie_id == serie_id)
        ).scalar()
            
            #contamos el número de capítulos por temporada
            self.temporadas = list(range(1, temporadas + 1))

            temporadas = session.exec(
                select(Capitulos.num_temporada.distinct())
                .where(Capitulos.serie_id == serie_id)
            ).all()
            
            self.temporadas = [t[0] for t in temporadas]  # Extraer los números de temporada
    @rx.event
    async def get_capitulos(self, temporada: int):
        '''función get_capitulos
        extrae los capítulos de la base de datos'''
        self.serie_id = self.router.page.params["serie"]
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            capitulos = session.exec(
                Capitulos.select().where(Capitulos.serie_id == self.serie_id, Capitulos.num_temporada == temporada)
            ).all()
            self.capitulos = capitulos


