import reflex as rx
from videoflix.models import Pelicula, Capitulos, UsuarioCapitulo, UsuarioPelicula
from videoflix.state.states import AuthState
from sqlmodel import select

class FavoritosState(rx.State):
    '''Clase FavoritosState. Almacena los datos de las películas favoritas de un usuario
    args:
    favoritos: list[Pelicula] = [] litado de películas favoritas
    cap_favoritos: lista de capñitulos favoritos
    vistas: lista de películas vistas
    cap_vistos: lista de capítulos vistos
    user_id: id del usuario, se recoge a través del estado por el logado del usuario
    is_loaded: bool = False
    '''
    favoritos: list[Pelicula] = []
    cap_favoritos: list[Capitulos] = []
    vistas: list[Pelicula]= []
    cap_vistos: list[Capitulos] = []
    user_id: int = AuthState.user.id 

    @rx.event
    async def load_favoritos(self):
        #self.user_id = int(AuthState.user.id)
        auth = await self.get_state(AuthState)
        user_id = auth.user.id
        print(AuthState.user.id.to_string())
        with rx.session() as session:
            self.favoritos = session.exec(
                select(Pelicula)
                .join(UsuarioPelicula)
                .where(
                    (UsuarioPelicula.usuario_id == user_id) &
                    (UsuarioPelicula.favorito == True)
                )
            ).all()

    @rx.event
    async def load_vistos(self):
        auth = await self.get_state(AuthState)
        user_id = auth.user.id
        with rx.session() as session:
            self.vistas = session.exec(
                select(Pelicula)
                .join(UsuarioPelicula)
                .where(
                    (UsuarioPelicula.usuario_id == user_id) &
                    (UsuarioPelicula.visto == True)
                )
            ).all()
    
    @rx.event
    async def load_cap_favoritos(self):
        #self.user_id = int(AuthState.user.id)
        auth = await self.get_state(AuthState)
        user_id = auth.user.id
        print(AuthState.user.id.to_string())
        with rx.session() as session:
            self.cap_favoritos = session.exec(
                select(Capitulos)
                .join(UsuarioCapitulo)
                .where(
                    (UsuarioCapitulo.usuario_id == user_id) &
                    (UsuarioCapitulo.favorito == True)
                )
            ).all()

    @rx.event
    async def load_cap_vistos(self):
        #self.user_id = int(AuthState.user.id)
        auth = await self.get_state(AuthState)
        user_id = auth.user.id
        print(AuthState.user.id.to_string())
        with rx.session() as session:
            self.cap_vistos = session.exec(
                select(Capitulos)
                .join(UsuarioCapitulo)
                .where(
                    (UsuarioCapitulo.usuario_id == user_id) &
                    (UsuarioCapitulo.visto == True)
                )
            ).all()
            
    @rx.event
    def consultarfavoritos(self):
        '''función consultarfavoritos
        recibe una clase y retorna todos los resultados de esa clase'''
        resultados=[]
        print (self.id_usuario)
        
        with rx.session() as session:
            resultados = session.exec(
                select(Pelicula).join(UsuarioPelicula, UsuarioPelicula.pelicula_id == Pelicula.id).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.favorito == True)
                )
            ).all()
            return resultados

def consultarDB(clase):
    '''función consultarDB
    recibe una clase(Pelicula o Series)
    retorna todos los resultados de esa clase
    películas: listado con películas (o series)
    '''
    peliculas=[]
    
    with rx.session() as session:
        peliculas = session.exec(
            clase.select()
        ).all()
        return peliculas  
    
@rx.event
def consultarfavoritos(clase, id_usuario):
    '''función consultarfavoritos
    recibe una clase y retorna todos los resultados de esa clase'''
    resultados=[]
    print (id_usuario)
    id_usuario= int(id_usuario)
    with rx.session() as session:
        resultados = session.exec(
            select(clase).join(UsuarioPelicula, UsuarioPelicula.pelicula_id == Pelicula.id).where(
                (UsuarioPelicula.usuario_id == id_usuario) &
                (UsuarioPelicula.favorito == True)
            )
        ).all()
        return resultados

