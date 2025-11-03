import reflex as rx


def title_component() -> rx.Component:
    """A title component for the password generator app."""
    return rx.box(
        rx.vstack(
            # Main title
            rx.heading(
                "Secure Password Generator",
                align="center",
                size="9",
                as_="h1",
                color="#11224E",
                font_weight="800",
                style={
                    "letter_spacing": "-0.02em",
                },
            ),
            # Subtitle with icon
            rx.hstack(
                rx.icon("shield_check", size=24, color="#F87B1B"),
                rx.text(
                    "Generate Strong & Secure Passwords Instantly",
                    size="4",
                    color="#11224E",
                    font_weight="500",
                ),
                rx.icon("shield_check", size=24, color="#F87B1B"),
                align_items="center",
                justify="center",
                spacing="3",
            ),
            spacing="3",
            align_items="center",
            mb="8",
        ),
        padding_top="40px",
        width="100%",
    )
