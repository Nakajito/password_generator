import reflex as rx

import datetime


def footer_component() -> rx.Component:
    """A footer component for the password generator app."""
    return rx.container(
        rx.text(
            f"© {datetime.datetime.now().year} Secure Password Generator. ",
            align="center",
            color="gray",
            size="2",
        ),
    )
