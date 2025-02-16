import reflex as rx
from videoflix.models import UsuarioPelicula, UsuarioCapitulo
from sqlmodel import select
class AddFavourites(rx.State):
    '''clase AddFavourites
    marca como visto o favorito una película a un usuario
    args: 
    id_usuario: la id del usuario
    id_película: la id de la película
    visto: si está o no visto
    favorito: si está añadida a la lista de favoritos'''
    id_usuario: int = None
    id_pelicula: int = None
    id_capitulo: int = None
    vista: bool = None
    favorito: bool = None

    def consultar_visto(self):
        ''' función consultar visto
        a través del id de usuario y de la película, confirma si está vista o no'''
        with rx.session() as session:
            if session.exec(
                select(UsuarioPelicula).where(
                    UsuarioPelicula.usuario_id== self.id_usuario 
                    and UsuarioPelicula.pelicula_id == self.id_pelicula)
                ).first():
                visualizado=session.exec(
                    select(UsuarioPelicula).where(
                        UsuarioPelicula.usuario_id== self.id_usuario 
                        and UsuarioPelicula.pelicula_id == self.id_pelicula)
                ).first()
                if visualizado.visto == True:
                    self.vista=True
                    return self.vista
                else:
                    self.vista= False
                    return self.vista
            else:
                self.vista= False
                return self.vista
    
    @rx.event
    async def marcar_como_favorito(self):
        '''función marcar_como_favorito
        verifica si un usuario ha marcado como favorita una película y si no es así, la marca como favorita
        retorna un mensaje de confirmación, bien añadiendo a la película a favoritos o 
        informando que ya está marcado como tal'''
        with rx.session() as session:
            
            favor = session.exec(
                select(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.pelicula_id == self.id_pelicula)
                )
            ).first()
        
            
            if favor:
                print(favor)
                
                if not favor.favorito:
                    favor.favorito = True
                    session.add(favor)
                    session.commit()
                    self.favorito = True
                    return rx.window_alert(f"Película añadida a los favoritos.")
                else:
                    self.favorito = True
                    return rx.window_alert("Esta película ya ha sido marcada como favorita.")
            else:
                nuevo_favorito = UsuarioPelicula(
                    usuario_id=self.id_usuario,
                    pelicula_id=self.id_pelicula,
                    visto=False,
                    favorito=True  #
                )
                session.add(nuevo_favorito)
                session.commit()
                self.vista = True
                return rx.window_alert(f"Película añadida a los favoritos.")

    @rx.event
    async def marcar_como_favorito_cap(self):
        '''función marcar_como_favorito
        verifica si un usuario ha marcado un capítulo y si no es así, la marca como favorito
        retorna un mensaje de confirmación, bien añadiendo al capítulo a favoritos o 
        informando que ya está marcado como tal'''

        with rx.session() as session:
            
            favor = session.exec(
                select(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.capitulo_id == self.id_capitulo)
                )
            ).first()
        
            
            if favor:
                
                if not favor.favorito:
                    favor.favorito = True
                    session.add(favor)
                    session.commit()
                    self.favorito = True
                    return rx.window_alert(f"Capitulo añadido a los favoritos.")
                else:
                    self.favorito = True
                    return rx.window_alert("Este capítulo ya ha sido marcado como favorito.")
            else:
                nuevo_favorito = UsuarioCapitulo(
                    usuario_id=self.id_usuario,
                    capitulo_id=self.id_capitulo,
                    visto=False,
                    favorito=True  # Puedes ajustar esto según sea necesario
                )
                session.add(nuevo_favorito)
                session.commit()
                self.vista = True
                return rx.window_alert(f"Capitulo añadido a los favoritos.")
            
    @rx.event
    async def marcar_como_vista(self):
        '''función marcar_como_vista
        verifica si un usuario ha visto una película y si no es así, la marca como vista
        retorna un mensaje de confirmación, bien marcando  la película como vista o informando de que ya ha sido
        vista'''
        with rx.session() as session:
            visualizado = session.exec(
                select(UsuarioPelicula).where(
                    (UsuarioPelicula.usuario_id == self.id_usuario) &
                    (UsuarioPelicula.pelicula_id == self.id_pelicula)
                )
            ).first()
            
            
            if visualizado:
                
                print(visualizado)
                if not visualizado.visto:
                    visualizado.visto = True
                    session.add(visualizado)
                    session.commit()
                    self.vista = True
                    return rx.window_alert(f"Película marcada como vista para el usuario {self.id_usuario}.")
                else:
                    self.vista = True
                    return rx.window_alert("Esta película ya ha sido vista.")
            else:
                nuevo_visualizado = UsuarioPelicula(
                    usuario_id=self.id_usuario,
                    pelicula_id=self.id_pelicula,
                    visto=True,
                    favorito=False  # Puedes ajustar esto según sea necesario
                )
                session.add(nuevo_visualizado)
                session.commit()
                self.vista = True
                return rx.window_alert(f"Película marcada como vista para el usuario {self.id_usuario}.")

    @rx.event
    async def marcar_cap_como_visto(self):
        '''función marcar_cap_como_visto
        verifica si un usuario ha visto un capítulo y si no es así, lo marca como visto
        reorna un mensaje confirmando que se ha marcado como vista o indicandoq ue ya ha sido vista anteriormente'''
        with rx.session() as session:
            visualizado = session.exec(
                select(UsuarioCapitulo).where(
                    (UsuarioCapitulo.usuario_id == self.id_usuario) &
                    (UsuarioCapitulo.capitulo_id == self.id_capitulo)
                )
            ).first()
            
            
            if visualizado:
                print(visualizado)
                
                if not visualizado.visto:
                    visualizado.visto = True
                    session.add(visualizado)
                    session.commit()
                    self.vista = True
                    return rx.window_alert(f"Capítulo marcada como vista para el usuario {self.id_usuario}.")
                else:
                    self.vista = True
                    return rx.window_alert("Este capítulo ya ha sido visto.")
            else:
                nuevo_visualizado = UsuarioCapitulo(
                    usuario_id=self.id_usuario,
                    pelicula_id=self.id_pelicula,
                    visto=True,
                    favorito=False  
                )
                session.add(nuevo_visualizado)
                session.commit()
                self.vista = True
                return rx.window_alert(f"Capítulo marcado como visto para el usuario {self.id_usuario}.")


