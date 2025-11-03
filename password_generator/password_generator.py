import reflex as rx
from password_generator.components.title import title_component
from password_generator.components.description import description_component
from password_generator.components.generator_psw_box import generator_psw_box
from password_generator.layout.footer import footer_component

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.container(
            title_component(),
            description_component(),
            generator_psw_box(),
            footer_component(),
            size="4",
        ),
        # Background with solid color
        style={
            "min_height": "100vh",
            "background": "#EEEEEE",
        },
    )


app = rx.App()
app.add_page(
    index,
    title="Secure Password Generator | Create Strong Passwords",
    description="Generate secure and random passwords instantly with our free password generator tool. Create strong passwords with custom length and character combinations.",
)
