'''archivo consultar_estadisticas
recoge las clases mediante las que un usuario o un administrador consulta en la base de datos 
los minutos de una película o serie'''
import reflex as rx
from sqlalchemy import select, func
from videoflix.models import UsuarioPelicula, UsuarioCapitulo, Pelicula, Capitulos
from videoflix.state.states import AuthState

class UserStatistics(rx.State):
    '''clase UserStatistics
    recoge las estadísticas de un usuario
    id_usuario: la id del usuario
    minutos_vistos_peliculas: el total de minutos vistos en películas por el usuario
    minutos_vistos_series: el total de minutos vistos en series por el usuario
    minutos_vistos: total de minutos vistos
    dict_minutos: minutos vistos por película o capítulo
    peliculas_vistas: listadi de peliculas vistas
    series_vistas: listado se capítulos vistos
    total_peliculas: total de películas vistas
    total_series: total de series vistas
    '''
    id_usuario: int = None
    minutos_vistos_peliculas: int = 0
    minutos_vistos_series: int = 0
    minutos_vistos: int = 0
    dict_minutos: dict = {}
    peliculas_vistas: list = []
    series_vistas: list = []
    total_peliculas: int = 0
    total_series: int = 0

    @rx.event
    async def consultar_minutos_peliculas(self):
        '''Función consultar_minutos_vistos
        Consulta los minutos vistos por un usuario específico y actualiza el estado'''
        auth = await self.get_state(AuthState)
        print(auth.user.id)
        self.id_usuario = auth.user.id
        
        with rx.session() as session:
            # Consultar minutos vistos en películas
            self.minutos_vistos_peliculas = session.exec(
                select(func.sum(Pelicula.duracion)).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.visto == True)
                )
            ).scalar() or 0
            print(f"Minutos películas: {self.minutos_vistos_peliculas}")    

                        # Consultar títulos y duraciones de las películas vistas
            peliculas = session.exec(
                select(Pelicula.titulo, Pelicula.duracion).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.visto == True)
                )
            ).all()
            
            # Construir la lista de diccionarios
            self.peliculas_vistas = [{"name": pelicula.titulo, "minutos": pelicula.duracion} for pelicula in peliculas]
            self.total_peliculas = len(self.peliculas_vistas)
            print(f"Películas vistas: {self.peliculas_vistas}")

    @rx.event
    async def consultar_minutos_series(self):
        '''Función consultar_minutos_vistos
        Consulta los minutos vistos por un usuario específico y actualiza el estado'''

        auth = await self.get_state(AuthState)
        print(auth.user.id)
        self.id_usuario = auth.user.id
        
        with rx.session() as session:
            # Consultar minutos vistos en series

            # Consultar minutos vistos en capítulos
            self.minutos_vistos_series = session.exec(
                select(func.sum(Capitulos.duracion)).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.visto == True)
                )
            ).scalar() or 0
            print(self.minutos_vistos_series)    
            
            # Sumar los minutos vistos en películas y capítulos
            print(f"Minutos series: {self.minutos_vistos_series}")

                        # Consultar títulos y duraciones de las películas vistas
            series = session.exec(
                select(Capitulos.titulo_capitulo, Capitulos.duracion).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.visto == True)
                )
            ).all()
            
            # Construir la lista de diccionarios
            self.series_vistas = [{"name": serie.titulo_capitulo, "minutos": serie.duracion} for serie in series]
            self.total_series= len(self.series_vistas)
            print(f"Películas vistas: {self.peliculas_vistas}")

            return 

    @rx.event
    async def mostrar_minutos_vistos(self) -> rx.Component:
        '''Función mostrar_minutos_vistos
        Devuelve un componente que muestra los minutos vistos por el usuario'''
        auth = await self.get_state(AuthState)
        print(auth.user.id)
        self.id_usuario = auth.user.id
        UserStatistics.consultar_minutos_peliculas()
        UserStatistics.consultar_minutos_series()
        self.minutos_vistos = self.minutos_vistos_peliculas + self.minutos_vistos_series
        self.dict_minutos = {"Peliculas": self.minutos_vistos_peliculas, "Series": self.minutos_vistos_series}
        print(f"Minutos totales: {self.minutos_vistos}")
    
    def reset_atributos(self):
        '''función reset
        resetea todos los atributos de la clase UserStatistics'''
        self.id_usuario: int = None
        self.minutos_vistos_peliculas: int = 0
        self.minutos_vistos_series: int = 0
        self.minutos_vistos: int = 0
        self.dict_minutos: dict = {}
        self.peliculas_vistas: list = []
        self.series_vistas: list = []
        self.total_peliculas: int = 0
        self.total_series: int = 0
        self.id_admin: int = 0
        self.id_admin2: int = 0
        self.admin : bool = False

class AdminStatistics(rx.State):
    id_usuario: int = None
    id_usuario2: int = None
    minutos_vistos_peliculas: int = 0
    minutos_vistos_peliculas2: int = 0
    minutos_vistos_series: int = 0
    minutos_vistos_series2: int = 0
    minutos_vistos: int = 0
    minutos_vistos2: int = 0
    dict_minutos: dict = {}    
    dict_minutos2: dict = {}
    peliculas_vistas2: list = []
    peliculas_vistas: list = []
    series_vistas: list = []
    series_vistas2: list = []
    total_peliculas: int = 0
    total_series: int = 0
    total_peliculas2: int = 0
    total_series2: int = 0

    @rx.event
    async def consultar_minutos_peliculas(self):
        '''Función consultar_minutos_vistos
        Consulta los minutos vistos por un usuario específico y actualiza el estado'''        
        
        with rx.session() as session:
            # Consultar minutos vistos en películas
            self.minutos_vistos_peliculas = session.exec(
                select(func.sum(Pelicula.duracion)).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.visto == True)
                )
            ).scalar() or 0
            print(f"Minutos películas: {self.minutos_vistos_peliculas}")    

                        # Consultar títulos y duraciones de las películas vistas
            peliculas = session.exec(
                select(Pelicula.titulo, Pelicula.duracion).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.visto == True)
                )
            ).all()

            self.minutos_vistos_peliculas2 = session.exec(
                select(func.sum(Pelicula.duracion)).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario2) &
                    (UsuarioPelicula.visto == True)
                )
            ).scalar() or 0
            print(f"Minutos películas: {self.minutos_vistos_peliculas2}")    

                        # Consultar títulos y duraciones de las películas vistas
            peliculas2 = session.exec(
                select(Pelicula.titulo, Pelicula.duracion).join(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario2) &
                    (UsuarioPelicula.visto == True)
                )
            ).all()
            
            # Construir la lista de diccionarios
            self.peliculas_vistas = [{"name": pelicula.titulo, "minutos": pelicula.duracion} for pelicula in peliculas]
            self.peliculas_vistas2 = [{"name": pelicula.titulo, "minutos": pelicula.duracion} for pelicula in peliculas2]
            self.total_peliculas = len(self.peliculas_vistas)
            self.total_peliculas2 = len(self.peliculas_vistas2)
            print(f"Películas vistas: {self.peliculas_vistas}")
            
            
            
        
    @rx.event
    async def consultar_minutos_series(self):
        '''Función consultar_minutos_vistos
        Consulta los minutos vistos por un usuario específico y actualiza el estado'''
        
        with rx.session() as session:
            # Consultar minutos vistos en series

            # Consultar minutos vistos en capítulos
            self.minutos_vistos_series = session.exec(
                select(func.sum(Capitulos.duracion)).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.visto == True)
                )
            ).scalar() or 0
            print(self.minutos_vistos_series)    
            
            # Sumar los minutos vistos en películas y capítulos
            print(f"Minutos series: {self.minutos_vistos_series}")

                        # Consultar títulos y duraciones de las películas vistas
            series = session.exec(
                select(Capitulos.titulo_capitulo, Capitulos.duracion).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.visto == True)
                )
            ).all()
            
            # Construir la lista de diccionarios
            self.series_vistas = [{"name": serie.titulo_capitulo, "minutos": serie.duracion} for serie in series]
            self.total_series= len(self.series_vistas)
            print(f"Películas vistas: {self.peliculas_vistas}")

            self.minutos_vistos_series2 = session.exec(
                select(func.sum(Capitulos.duracion)).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario2) &
                    (UsuarioCapitulo.visto == True)
                )
            ).scalar() or 0
            print(self.minutos_vistos_series2)    
            
            # Sumar los minutos vistos en películas y capítulos
            print(f"Minutos series: {self.minutos_vistos_series2}")

                        # Consultar títulos y duraciones de las películas vistas
            series2 = session.exec(
                select(Capitulos.titulo_capitulo, Capitulos.duracion).join(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario2) &
                    (UsuarioCapitulo.visto == True)
                )
            ).all()
            
            # Construir la lista de diccionarios
            self.series_vistas2 = [{"name": serie.titulo_capitulo, "minutos": serie.duracion} for serie in series2]
            self.total_series2= len(self.series_vistas2)
            print(f"Películas vistas: {self.peliculas_vistas2}")

            return 
        
    @rx.event
    async def mostrar_minutos_vistos(self) -> rx.Component:
        '''Función mostrar_minutos_vistos
        Devuelve un componente que muestra los minutos vistos por el usuario'''


        self.minutos_vistos = self.minutos_vistos_peliculas + self.minutos_vistos_series
        self.dict_minutos = {"Peliculas": self.minutos_vistos_peliculas, "Series": self.minutos_vistos_series}
        self.minutos_vistos2 = self.minutos_vistos_peliculas2 + self.minutos_vistos_series2
        self.dict_minutos2 = {"Peliculas": self.minutos_vistos_peliculas2, "Series": self.minutos_vistos_series2}
        print(f"Minutos totales: {self.minutos_vistos}")
    
    def reset_atributos(self):
        '''función reset
        resetea todos los atributos de la clase UserStatistics'''
        self.id_usuario: int = None
        self.minutos_vistos_peliculas: int = 0
        self.minutos_vistos_series: int = 0
        self.minutos_vistos: int = 0
        self.dict_minutos: dict = {}
        self.peliculas_vistas: list = []
        self.series_vistas: list = []
        self.total_peliculas: int = 0
        self.total_series: int = 0
        self.id_admin: int = 0
        self.id_admin2: int = 0
        self.admin : bool = False