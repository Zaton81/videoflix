'''archivo models desde donde se crean los tablas de la base de datos'''
import reflex as rx
from typing import Optional, List
import sqlmodel



class User(rx.Model, table=True):
    '''
    Clase User. Almacena los datos del usuario en la taba usuario de la DB
    args:
    id: el identificador único de usuario (con Reflex se crea de manera automática)
    username: el Alias del usuario, debe ser también único
    nombre:
    el nombre del usuario
    apellidos: los apellidos del usuario
    email: el correo electrónico del usuario
    password: la contraseña del usuario
    '''
    __tablename__ = "usuarios"
    
    username: str = sqlmodel.Field(unique=True)
    nombre: str 
    email: str = sqlmodel.Field(unique=True)
    password: str
    admin: bool = False

    # Relaciones con otros modelos
    peliculas: List["UsuarioPelicula"] = sqlmodel.Relationship(back_populates="usuario")
    capitulos: List["UsuarioCapitulo"] = sqlmodel.Relationship(back_populates="usuario")
    

class Pelicula(rx.Model, table=True):
    '''Clase Pelicula. Almacena en la DB las películas
    args
    titulo: el tçitulo de la película
    year: el año de la película
    duracion: duración total en minutos de la película
    portada: almacena el nombre del archivo de la portada
    video: almacena el nombre del archivo del vídeo de la película o el código embebido del mismo
    sinopsis: sinopsis de la película
    '''
    __tablename__ = "peliculas"
    titulo: str
    year: int 
    duracion: int
    portada: Optional[str] = None
    video: str
    sinopsis: Optional[str] = None

    usuarios: List["UsuarioPelicula"] = sqlmodel.Relationship(back_populates="pelicula")

class Series(rx.Model, table=True):
    '''Clase Series. Almacena en la DB las series
    args
    titulo: el titulo de la serie
    year: el año de estreno
    temporadas: número de temporadas disponibles'''
    __tablename__ = "series"
    
    titulo: str
    year: int
    portada: Optional[str] = None
    sinopsis: Optional[str] = None
    num_temporadas: int

    capitulos: List["Capitulos"] = sqlmodel.Relationship(back_populates="serie")    

class Capitulos(rx.Model, table=True):
    '''clase Capitulos
    recoge los capítulos y los relaciona con las series
    args
    serie_id: la id de la serie a la que pertenece el capítulo
    tilulo capítulo: el título del capítulo
    num_capítulo: el número del capítulo
    num_temporada: la temporada a la que pertenece el capítulo
    sinopsis. la sinopsis del capítulo
    duración: la duración en minutos del capítulo
    vídeo: el código embebido del capítulo (o el nombre del archivo)'''
    __tablename__ = 'capitulos'

    serie_id: int = sqlmodel.Field(foreign_key="series.id")
    titulo_capitulo: str
    num_capitulo: int
    num_temporada: int
    sinopsis_capitulo: Optional[str] = None
    video: Optional[str] = None
    duracion: int

    serie: Series = sqlmodel.Relationship(back_populates="capitulos")
    usuarios: List["UsuarioCapitulo"] = sqlmodel.Relationship(back_populates="capitulo")
    

class UsuarioPelicula(rx.Model, table=True):
    '''clase UsuarioPelicula
    relaciona los usuarios con las películas vistas o favoritas
    usuario id: el id del usuario
    pelicula id_ la ide de la película
    visto: muestra si se ha visto o no la película
    favorito: muestra si la película se ha añadido a favoritos'''
    __tablename__ = 'usuario_peliculas'  

    usuario_id: int = sqlmodel.Field(foreign_key="usuarios.id")  
    pelicula_id: int = sqlmodel.Field(foreign_key="peliculas.id")
    visto: bool = False
    favorito: bool = False

    pelicula: Pelicula = sqlmodel.Relationship(back_populates="usuarios")
    usuario: User = sqlmodel.Relationship(back_populates="peliculas")

class UsuarioCapitulo(rx.Model, table=True): 
    __tablename__ = 'usuario_capitulos' 

    """Tabla intermedia para relacionar usuarios con capítulos"""
    __tablename__ = "usuario_capitulos"
    
    usuario_id: int = sqlmodel.Field(foreign_key="usuarios.id")  
    capitulo_id: int = sqlmodel.Field(foreign_key="capitulos.id")
    visto: bool = False
    favorito: bool = False

    usuario: User = sqlmodel.Relationship(back_populates="capitulos")
    capitulo: Capitulos = sqlmodel.Relationship(back_populates="usuarios")



