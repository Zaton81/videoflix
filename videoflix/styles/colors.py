'''archivo en el que se incluyen los colores genéricos de la web'''
#Nota aunque en un primer momento se ha querido realizar con colores (de hecho en los styles del archivo styles los dejo comentados, finalmente se ha decidido dejarlo en blanco y negro)
from enum import Enum
import reflex as rx

class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#9a0457"
    BACKGROUND = "#04589b"
    CONTENT = "#171F26",
    PURPLE = "#9146ff",
    BUTTON = "cyan"



class TextColor(Enum):
    BODY = "#b4d7fd"

#En el caso del footer y header, se ha dotado de un colo distinto, para lo que creamos la variables siguientes:

HEADER_COLOR= rx.color("accent", 3)
FOOTER_COLOR = rx.color("cyan", 3)

