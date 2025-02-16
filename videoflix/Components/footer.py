import reflex as rx
from datetime import datetime
from videoflix.styles.styles import HEADER_STYLE, Size
from videoflix.styles.constants import tokio, linkedin, facebook, twitter, instagram
from videoflix.styles.colors import FOOTER_COLOR
def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)



def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href, is_external=True)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", instagram),
        social_link("twitter", twitter),
        social_link("facebook", facebook),
        social_link("linkedin", linkedin),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/logoSin.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        f"© {datetime.now().year} Videoflix.Todos los derechos reservados. Web construida por Jorge Zatón Pérez como proyecto final del curso de Python de ",
                            rx.link(
                                "Tokio School.",
                                href=tokio,
                                is_external=True,
                                color_scheme="orange"
                    ),
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
            eight="100%",
        ),
        width="100%",
        padding_x = Size.SMALL.value,
        padding_bottom= Size.DEFAULT.value,
        #margin_x="2em",
        #margin_top="2em",
        style=HEADER_STYLE,
        bottom="0",
        z_index= "1000",
        position="fixed",
        bg=FOOTER_COLOR
    )