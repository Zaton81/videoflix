"""The authentication state."""
import reflex as rx
from sqlmodel import select
from videoflix.models import User 
from videoflix.styles.constants import LOGIN, USER, ADMIN
from typing import Optional


class AuthState(rx.State):
    """Clase AuthState
    incluye las funciones signup y login para autenticarse y resistrarse en videoflix
    así como verifica los estados de logado
    username: alias del usuario
    password: contraseña del usuario
    nombre: nobre del usuario
    email: correo electrónico
    confirm_password: calidación de contraseá
    user: Optional[User] 
    admin: booleano que determina si un usuario es administrador
    accepted_terms: boleano que verifica si se han aceptado los términos y condiciones
    """
    username: str
    password: str
    nombre: str
    email: str
    confirm_password: str
    user: Optional[User] = None
    admin: bool = False
    accepted_terms: bool = False

    def clear_inputs(self):
        '''función clear inputs, sirve para limpiar los imputs una vez registrado el usuario''' 
        return [
            rx.set_value("nombre", ""),
            rx.set_value("username", ""),
            rx.set_value("email", ""),
            rx.set_value("password", ""),
            rx.set_value("confirm_password", "")
        ]


    def signup(self):
        """Función signup
        recibe del formulario los datos de regostro: nombre, password, username, email y confirm_password
        coteja si la contraseña introducida las dos veces coincide. Si no, retorna una ventana de aviso
        coteja si el email o username ya están en la base de datos, en cuyo caso retorna una ventana de aviso
        en caso contrario, retorna una redirección a la web y una ventana confirmando el registro"""
        if not self.accepted_terms:
            return rx.window_alert("Debes aceptar los términos y condiciones")
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("las contraseñas no coinciden")
            if session.exec(select(User).where(User.username == self.username)).first() or session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("El usuario o correo electrónico ya está en uso")
            self.user = User(username=self.username,nombre=self.nombre, email=self.email, password=self.password, admin= bool(self.admin))
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            AuthState.clear_inputs()
            return [AuthState.clear_inputs(), rx.window_alert("Usuario registrado correctamente")] 

    async def  login(self):
        """función login
        recibe a través de un formulario los fdatos de inicio de sesión email y contraseña.
        Se coinciden, redirige a la página de usuario, de lo contrario envía un aviso de erros"""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            if user and user.password == self.password:
                self.user = user
                print(user.username)
                alias=user.username
                
                
                return rx.redirect(f"/user/{alias}")
            else:
                return rx.window_alert("email o contraseña incorrecta.")
    async def  login_admin(self):
        """función login_admin
        recibe a través de un formulario los fdatos de inicio de sesión email y contraseña.
        Se coinciden, y se trata de un administrador, redirige a la web de administraciónde lo contrario, a la web de usuario"""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            if user and user.password == self.password:
                self.user = user
                print(user.username)
                alias=user.username
                if user.admin ==True:
                    return rx.redirect (ADMIN)
                else:
                    return rx.redirect(f"/user/{alias}")
            else:
                return rx.window_alert("email o contraseña incorrecta.")
    
    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        '''función check_login
        verifica si un usuario está logado, en caso contrario, redirige a la página de login'''
        if not self.logged_in:
            return rx.redirect(LOGIN)
        
    def check_login_admin(self):
        """Comprueba el logado de administración. En caso de que el usuario no sea administrador, 
        realiza un retorno a la página de usuario."""
        if not self.logged_in:
            return rx.redirect(LOGIN)
        elif self.user.admin ==False:
            return rx.redirect(USER)

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
            
