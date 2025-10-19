import reflex as rx


def title_component() -> rx.Component:
    """A title component for the password generator app."""
    return rx.container(
        rx.heading(
            "Secure Password Generator in Python 🔐",
            align="center",
            size="8",
            as_="h1",
            mb="3",
        )
    )
