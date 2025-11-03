import reflex as rx

import datetime


def footer_component() -> rx.Component:
    """A footer component for the password generator app."""
    return rx.box(
        rx.vstack(
            # Divider line
            rx.box(
                height="2px",
                width="100%",
                bg="#CBD99B",
                mb="6",
            ),
            # Footer content
            rx.vstack(
                # Main footer text with icon
                rx.hstack(
                    rx.icon("shield_check", size=20, color="#F87B1B"),
                    rx.text(
                        f"© {datetime.datetime.now().year} Secure Password Generator",
                        font_weight="600",
                        size="3",
                        color="#11224E",
                    ),
                    align_items="center",
                    spacing="2",
                    justify="center",
                ),
                # Subtitle
                rx.text(
                    "Built with Python & Reflex • Open Source",
                    size="2",
                    color="#11224E",
                    opacity="0.6",
                    text_align="center",
                ),
                # Security note
                rx.hstack(
                    rx.icon("lock", size=14, color="#CBD99B"),
                    rx.text(
                        "Your passwords are generated locally and never stored",
                        size="1",
                        color="#11224E",
                        opacity="0.5",
                        font_style="italic",
                    ),
                    align_items="center",
                    spacing="1",
                    justify="center",
                ),
                spacing="2",
                align_items="center",
            ),
            spacing="4",
            width="100%",
        ),
        padding="32px 20px",
        margin_top="60px",
        width="100%",
    )
