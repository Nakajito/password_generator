import reflex as rx
from password_generator.components.title import title_component
from password_generator.components.description import description_component
from password_generator.components.generator_psw_box import generator_psw_box

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        title_component(), description_component(), generator_psw_box(), padding="8"
    )


app = rx.App()
app.add_page(index)
