import reflex as rx
from videoflix.models import  Pelicula, UsuarioPelicula
from sqlmodel import select


class Film_queries(rx.State):
    '''clase Film_queries
    desde ella se accede a la DB y se añaden, editan y eliminan películas
    También se recuperan los datos de la DB
    id: id de la película
    titulo: título de la película
    year: año de estreno
    duracion: duración en minutos
    portada: nombre del archivo de la portada
    video: link o código del vídeo
    sinopsis: sinopsis de la películo
    user_id:id de la película
    peliculas : listado de películas
    film_data: diccionario con los datos de la película'''
    id: int = None
    titulo: str = None
    year: int = None
    duracion: int = None
    portada: str = None
    video: str = None
    sinopsis: str = None
    user_id:int = None
    peliculas :list =[]
    img: list[str] =[]
    film_data: dict = {}


    def get_id(self):
        '''función get_id
        recibe el id de una película y lo guarda en la variable id'''
        print(self.id)
        return self.id

    def add_film(self):
        '''función add_film
        recibe los datos de un formulario y añade la película a la DB
        En caso de que algún dato sea incorrecto, retorna un mensaje de información'''
        with rx.session() as session:
            #try:
                print(self.titulo, self.year, self.duracion, self.video, self.sinopsis ,self.portada) 
                pelicula = Pelicula(titulo=self.titulo, year=self.year, duracion=self.duracion, video=self.video, 
                                    portada=self.portada, sinopsis=self.sinopsis) # portada=self.portada, sinopsis=self.sinopsis
                session.add(pelicula)
                session.expire_on_commit = False
                session.commit()
                titulo=self.titulo
                Film_queries.resets(self)
                return rx.window_alert(f"Película {titulo} añadida correctamente.")
            #except:
            #    return rx.window_alert("Algo ha fallado. Inténtelo de nuevo.")    

    def edit_film(self):
        '''función edit film
        recibe los fatos de un formulario y modifica los datos de una película existente retornando un mensaje de confirmación.
        En el caso de que la película no se encuentre, retorna un mensaje informando de ello.
        '''
        print(self.titulo, self.year, self.duracion, self.video, self.sinopsis ,self.portada)
        if self.id==None:
            return rx.window_alert("Introduce el título de la película que quieras modificar.")
        else:
            with rx.session() as session:
                if not session.exec(select(Pelicula).where(Pelicula.id == self.id) ).first():
                    return rx.window_alert("La película no se encuentra en la base de datos. Verifica el título.")
                else:
                    pelicula=session.exec(select(Pelicula).where(Pelicula.id == self.id) ).first()
                    print(pelicula)
                    if self.titulo not in [None, ""]:
                        pelicula.titulo=self.titulo
                    if self.year not in [None, ""]:
                        pelicula.year=self.year                          
                    if self.duracion not in [None, ""]:
                        pelicula.duracion=self.duracion        
                    if self.portada not in [None, ""]:
                        pelicula.portada=self.portada
                    if self.sinopsis not in [None, ""]:
                        pelicula.sinopsis=self.sinopsis              
                    if self.video not in [None, ""]:
                        pelicula.video=self.video
            session.add(pelicula)
            titulo=self.titulo
            session.commit()
            Film_queries.resets(self)
            
            return  rx.window_alert(f"Película {titulo} modificada correctamente.")
    @rx.event
    async def handle_upload_add(self, files: list[rx.UploadFile] = None):
        '''función handle_upload_add
        carga la imagen, recoge el nombre de la misma y la recoge para guardarla en la base de datos.
        Args:
        files: los archivos a subir.
        '''
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
            return Film_queries.add_film() 
        
    async def handle_upload_edit(self, files: list[rx.UploadFile] = None):
        """método handle_upload
        carga la imagen, recoge el nombre de la misma y la recoge para guardarla en la base de datos.
        Args:
        files: los archivos a subir.
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
            return Film_queries.edit_film() 
        
    @rx.event
    async def handle_upload(self, files: list [rx.UploadFile]= None, tipo: str = "editar"):
        """Handle the upload of file(s).
        Args:
        files: The uploaded files.
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
            except:
                pass             
        if tipo=="añadir":
            return  self.add_film()
        else:
            return  self.edit_film()   

    def get_film(self):
        '''función get_film
        extrae los datos de la película de la base de datos a través del id
        usado en la página film_page'''
        film_id = self.router.page.params["pelicula"]
        print(film_id)
        with rx.session() as session:
            film = session.exec(Pelicula.select().where(Pelicula.id == film_id)).first()
            self.film_data = film
            self.id = film.id
            self.titulo = film.titulo
            self.year = film.year
            self.duracion = film.duracion
            self.portada = film.portada
            self.video = film.video
            self.sinopsis = film.sinopsis
            print(self.film_data)

    def consultar_peliculas():
        with rx.session() as session:
            peliculas = session.exec(
                Pelicula.select()
            ).all()
            print(peliculas)
            return peliculas     

    def consultar_vistos(self):
        vistos= []
        print(id)
        with rx.session() as session:
            try:
                vistos= session.exec(
                    select(UsuarioPelicula).where((UsuarioPelicula.usuario_id==self.user_id)&(UsuarioPelicula.visto==True)).all()
                                    )
                print(vistos)
                return rx.text("hola")
            except:
                return rx.text("adios")
    
    def consultar_peliculas(self): 
        peliculas=[]
        '''consultar películas
        si se proporciona un título, devuelve esa película, de lo contrario, devuelve una lista con todas las películas'''
        with rx.session() as session: 
         

            peliculas = session.exec( Pelicula.select() ).all() 
            
            return peliculas
        
    def delete_film(self):
        '''función delete_film
        recibe el id de una película y la elimina de la DB
        En caso de que el id no se encuentre, retorna un mensaje de información'''
        if self.id==None:
            return rx.window_alert("Introduce el id de la película que quieras eliminar.")
        else:
            try:
                with rx.session() as session:
                    if not session.exec(select(Pelicula).where(Pelicula.id == self.id) ).first():
                        return rx.window_alert("La película no se encuentra en la base de datos. Verifica el id.")
                    else:
                        pelicula=session.exec(select(Pelicula).where(Pelicula.id == self.id) ).first()
                        session.delete(pelicula)
                        session.commit()
                        titulo=pelicula.titulo
                        Film_queries.resets(self)
                        return  rx.window_alert(f"Película {titulo} eliminada correctamente.")
            except:
                self.resets()
                return rx.window_alert("Algo ha fallado, inténtalo de nuevo mas tarde."), 
    
    def resets(self):
        '''función resets
        reinicia los valores de las variables de la clase'''
        self.titulo = None
        self.year = None
        self.duracion = None
        self.portada = None
        self.video = None
        self.sinopsis = None
        self.id = None
    
    def consultar_peliculas():
        '''función consultar_peliculas
        retorna una lista con todas las películas de la DB'''
        with rx.session() as session:
            peliculas = session.exec(
                Pelicula.select()
            ).all()
            print(peliculas)
            return peliculas
        
def listar_peliculas():
    peliculas=Film_queries.consultar_peliculas()
    for pelicula in peliculas:
        rx.text(pelicula.titulo)
    
    

    


class FilmState(rx.State):
    '''clase FilmState
    racibe el parametro de la pelicula  a través de la ruta y retorna los datos de la misma'''
    film_data: dict = {}
    id: int = None
    titulo: str = None
    year: int = None
    duracion: int = None
    portada: str = None
    video: str = None
    sinopsis: str = None
    peliculas: list =[]

    def get_film(self):
        '''función get_film
        extrae los datos de la película de la base de datos'''
        film_id = self.router.page.params["pelicula"]
        print(film_id)
        with rx.session() as session:
            film = session.exec(Pelicula.select().where(Pelicula.id == film_id)).first()
            self.film_data = film
            self.id = film.id
            self.titulo = film.titulo
            self.year = film.year
            self.duracion = film.duracion
            self.portada = film.portada
            self.video = film.video
            self.sinopsis = film.sinopsis
            print(self.film_data)

    def consultar_peliculas():
        with rx.session() as session:
            peliculas = session.exec(
                Pelicula.select()
            ).all()
            print(peliculas)
            return peliculas



