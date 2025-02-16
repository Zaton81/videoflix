import reflex as rx
from videoflix.Components.buttons import *
from videoflix.queries.edit_user import Queries_user
from videoflix.styles.styles import MAX_WIDTH

def form_add_user() -> rx.Component:
    ''' función form_add_user
    formulario mediante un administrador añade usuarios a la base de datos'''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Añadir usuario", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Añade un nuevo usuario",
            ),
            rx.alert_dialog.description(
                "rellena los datos del nuevo usuario",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Nombre", name="nombre",
                        on_blur=Queries_user.set_nombre
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                        on_blur=Queries_user.set_email
                    ),
                    rx.input(
                        placeholder="password",
                        name="password",
                        on_blur=Queries_user.set_password
                    ),
                    rx.input(
                        placeholder="username",
                        name="alias",
                        on_blur=Queries_user.set_username
                    ),
                    rx.input(
                        placeholder="admin",
                        name="True or False",
                        on_blur=Queries_user.set_admin
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Añadir usuario", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=Queries_user.signup(),
                reset_on_submit=False,
            ),
            max_width=MAX_WIDTH,
        ),
    )

def form_edit_user() ->rx.Component:
    ''' función form_edit_user
    formulario mediante un administrador edita usuarios de la base de datos'''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Editar usuario", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Edita un usuario",
            ),
            rx.alert_dialog.description(
                "rellena la id y solo los datos a modificar",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Id", name="id",
                        on_blur=Queries_user.set_id
                    ),
                    rx.input(
                        placeholder="Nombre", name="nombre",
                        on_blur=Queries_user.set_nombre
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                        on_blur=Queries_user.set_email
                    ),
                    rx.input(
                        placeholder="password",
                        name="password",
                        on_blur=Queries_user.set_password
                    ),
                    rx.input(
                        placeholder="username",
                        name="alias",
                        on_blur=Queries_user.set_username
                    ),
                    rx.input(
                        placeholder="admin",
                        name="True or False",
                        on_blur=Queries_user.set_admin
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Modificar usuario", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=Queries_user.edit(),
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

def form_delete_user() -> rx.Component:
    ''' función form delete user
    a través de la ID, elimina a un usuario de la base de datos '''
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("minus", size=26),
                rx.text("Eliminar usuario", size="4"),
                width="100%"
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Elimina un usuario",
            ),
            rx.alert_dialog.description(
                "Inserta la ID del usuario que quieres eliminar",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Id", name="id",
                        on_blur=Queries_user.set_id
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Eliminar usuario", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=Queries_user.delete_user(),
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
