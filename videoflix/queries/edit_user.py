import reflex as rx
from videoflix.models import User
from sqlmodel import select

class Queries_user(rx.State):
    """Clase Queries_user    
    incluye la funciones signup y login para autenticarse y resistrarse en videoflix"""
    id: int = None
    username: str = None
    password: str = None
    nombre: str = None
    email: str = None

    admin: bool = False

    def signup(self):
        """Función signup
        recibe del formulario los datos de regostro: nombre, password, username, email y confirm_password
        coteja si la contraseña introducida las dos veces coincide. Si no, retorna una ventana de aviso
        coteja si el email o username ya están en la base de datos, en cuyo caso retorna una ventana de aviso
        en caso contrario, retorna una redirección a la web y una ventana confirmando el registro"""
        try:
            with rx.session() as session:
                if session.exec(select(User).where(User.username == self.username)).first() or session.exec(select(User).where(User.email == self.email)).first():
                    return rx.window_alert("El usuario o correo electrónico ya está en uso")
                else:
                    user = User(username=self.username,nombre=self.nombre, email=self.email, password=self.password, admin= bool(self.admin))
                    session.add(user)
                    session.expire_on_commit = False
                    session.commit()
                    Queries_user.resets()
                    return rx.window_alert("Usuario registrado correctamente") 
        except:
            return rx.window_alert("Algo ha fallado. Inténtalo más tarde.")
    def edit(self):
        '''función edit
        recibe del formulario los datos del usuario y efita el mismo a través de la id '''
        try:
            with rx.session() as session:
                print(self.id, self.nombre, self.email, self.password, self.username, self.admin)
                if self.id is None or self.id =="":
                    return rx.window_alert("Debes introducir la id asegúrate de que sean números.")
                elif session.exec(select(User).where(User.id == self.id) ).first():
                    user= session.exec(select(User).where(User.id == self.id) ).first()
                    if self.nombre not in [None, ""]:
                        user.nombre= self.nombre
                    if self.email is not None:
                        if session.exec(select(User).where(User.email == self.email)).first():
                            return rx.window_alert("El correo electrónico ya está en uso")
                        else:
                            user.email= self.email
                    if self.password not in [None, ""]:
                        user.password= self.password
                    if self.username not in [None, ""]:
                        if session.exec(select(User).where(User.username == self.username)).first():
                            return rx.window_alert("El usuario ya está en uso")
                        else:
                            user.username = self.username
                    if self.admin != "True":
                        user.admin = False
                    else:
                        self.admin = True
                    nombre= self.nombre 
                    session.add(user)
                    session.commit()
                    Queries_user.resets()
                    return  rx.window_alert(f"Usuario {nombre} modificado correctamente.")
                else:
                    return rx.window_alert(f"No hay ningun usuario en la base de datos con la id {self.id}.")
                
            
        except:
            Queries_user.resets()
            return rx.window_alert("Algo ha fallado, no hemos podido añadir al usuario a la base de datos.")
    
    def delete_user(self):
        '''mediante delete_user de elimina el usuario de la base de datos'''
        with rx.session() as session:
            if self.id is None or self.id =="":
                return rx.window_alert("Debes introducir la id asegúrate de que sean números.")
            elif session.exec(select(User).where(User.id == self.id) ).first():
                user = session.exec(User.select().where(User.id == self.id)).first()
                session.delete(user)
                session.commit()
                Queries_user.resets()
                return rx.window_alert(f"Usuario {self.id} eliminado correctamente.")
            else:
                Queries_user.resets()
                return rx.window_alert(f"No hay ningun usuario en la base de datos con la id {self.id}.")
        
    
    def resets(self):
        self.nombre = None
        self.email = None
        self.password = None
        self.username = None
        self.admin = None
        self.id = None