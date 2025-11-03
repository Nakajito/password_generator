import reflex as rx
from typing import Any, cast

from password_generator.utils import generate_password


class GeneratorState(rx.State):
    password_length: str = ""
    generated_password: str = "Password will be displayed here"
    copied: bool = False
    error_message: str = ""
    MIN_LENGTH: int = 8
    password_strength: str = ""
    strength_color: str = "gray"

    def set_password_length(self, value: str):
        self.password_length = value

    def calculate_strength(self, length: int) -> tuple[str, str]:
        """Calculate password strength based on length."""
        if length < 8:
            return "Weak", "red"
        elif length < 12:
            return "Medium", "orange"
        elif length < 16:
            return "Strong", "blue"
        else:
            return "Very Strong", "green"

    def create_password(self):
        try:
            length = int(self.password_length)
            if length > 0:
                # Delegate to the shared utility for easier testing.
                self.generated_password = generate_password(length)
                # Calculate strength
                self.password_strength, self.strength_color = self.calculate_strength(
                    length
                )
                # Reset copy/info flags
                self.copied = False
                self.error_message = ""
            else:
                self.generated_password = "Please enter a valid length"
                self.error_message = "Length must be greater than 0"
                self.password_strength = ""
        except ValueError:
            self.generated_password = "Please enter a valid number"
            self.error_message = "Please enter a valid number"
            self.password_strength = ""

    def generate_password_function(self, length: int) -> str:
        # Kept for backward compatibility; prefer using `generate_password`.
        return generate_password(length)

    def copy_password(self):
        """Mark the password as copied."""
        if (
            self.generated_password
            and "Password will be" not in self.generated_password
        ):
            self.copied = True
        else:
            self.copied = False


def generator_psw_box() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Title with icon
            rx.hstack(
                rx.icon("key_round", size=32, color="#F87B1B"),
                rx.heading(
                    "Generate Your Password",
                    size="8",
                    font_weight="bold",
                    as_="h2",
                    color="#11224E",
                ),
                align_items="center",
                spacing="3",
                mb="6",
                justify="center",
            ),
            # Input section with improved design
            rx.vstack(
                rx.text(
                    "Password Length:",
                    font_weight="600",
                    size="4",
                    color="#11224E",
                    mb="2",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="e.g., 16",
                        value=GeneratorState.password_length,
                        on_change=cast(Any, GeneratorState.set_password_length),
                        size="3",
                        radius="large",
                        style={
                            "flex": "1",
                            "font_size": "18px",
                            "border": "2px solid",
                            "border_color": "#CBD99B",
                            "_focus": {
                                "border_color": "#F87B1B",
                                "box_shadow": "0 0 0 3px rgba(248, 123, 27, 0.1)",
                            },
                        },
                    ),
                    rx.button(
                        rx.icon("sparkles", size=20),
                        "Generate",
                        on_click=cast(Any, GeneratorState.create_password),
                        disabled=cast(Any, GeneratorState.password_length == ""),
                        size="3",
                        radius="large",
                        style={
                            "background": "#F87B1B",
                            "color": "white",
                            "font_weight": "600",
                            "padding": "0 24px",
                            "cursor": "pointer",
                            "_hover": {
                                "background": "#11224E",
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 10px 20px rgba(248, 123, 27, 0.4)",
                            },
                            "_disabled": {
                                "opacity": "0.5",
                                "cursor": "not-allowed",
                            },
                            "transition": "all 0.3s ease",
                        },
                    ),
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                mb="3",
            ),
            # Helper text with icon
            rx.hstack(
                rx.icon("info", size=16, color="#11224E"),
                rx.text(
                    f"Recommended minimum length: {GeneratorState.MIN_LENGTH} characters",
                    size="2",
                    color="#11224E",
                    opacity="0.7",
                ),
                align_items="center",
                spacing="2",
                mb="2",
            ),
            # Error message with better styling
            rx.cond(
                GeneratorState.error_message != "",
                rx.hstack(
                    rx.icon("circle_alert", size=16, color="#F87B1B"),
                    rx.text(
                        GeneratorState.error_message,
                        color="#F87B1B",
                        font_weight="500",
                    ),
                    align_items="center",
                    spacing="2",
                    padding="8px 12px",
                    bg="rgba(248, 123, 27, 0.1)",
                    border_radius="8px",
                    border="1px solid",
                    border_color="#F87B1B",
                    mb="4",
                ),
            ),
            # Password strength indicator
            rx.cond(
                GeneratorState.password_strength != "",
                rx.vstack(
                    rx.hstack(
                        rx.text("Strength:", font_weight="600", size="3"),
                        rx.match(
                            GeneratorState.strength_color,
                            (
                                "red",
                                rx.badge(
                                    GeneratorState.password_strength,
                                    color_scheme="red",
                                    size="2",
                                    radius="full",
                                ),
                            ),
                            (
                                "orange",
                                rx.badge(
                                    GeneratorState.password_strength,
                                    color_scheme="orange",
                                    size="2",
                                    radius="full",
                                ),
                            ),
                            (
                                "blue",
                                rx.badge(
                                    GeneratorState.password_strength,
                                    color_scheme="blue",
                                    size="2",
                                    radius="full",
                                ),
                            ),
                            (
                                "green",
                                rx.badge(
                                    GeneratorState.password_strength,
                                    color_scheme="green",
                                    size="2",
                                    radius="full",
                                ),
                            ),
                            rx.badge(
                                GeneratorState.password_strength,
                                color_scheme="gray",
                                size="2",
                                radius="full",
                            ),
                        ),
                        spacing="2",
                        align_items="center",
                    ),
                    width="100%",
                    mb="4",
                ),
            ),
            # Generated password display with modern card design
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("lock", size=20, color="#F87B1B"),
                        rx.text(
                            "Your Generated Password",
                            font_weight="600",
                            size="3",
                            color="#11224E",
                        ),
                        align_items="center",
                        spacing="2",
                        mb="3",
                    ),
                    # Password text area
                    rx.box(
                        rx.text(
                            GeneratorState.generated_password,
                            font_family="monospace",
                            font_weight="bold",
                            size="6",
                            color="#11224E",
                            word_break="break-all",
                            line_height="1.6",
                        ),
                        padding="16px",
                        bg="#EEEEEE",
                        border_radius="12px",
                        border="2px dashed",
                        border_color="#CBD99B",
                        width="100%",
                        mb="3",
                    ),
                    # Copy button with feedback
                    rx.cond(
                        GeneratorState.copied,
                        rx.button(
                            rx.icon("check", size=18),
                            "Copied!",
                            size="3",
                            radius="large",
                            width="100%",
                            style={
                                "background": "#CBD99B",
                                "color": "#11224E",
                                "font_weight": "600",
                                "cursor": "default",
                            },
                        ),
                        rx.button(
                            rx.icon("copy", size=18),
                            "Copy to Clipboard",
                            on_click=[
                                cast(
                                    Any,
                                    rx.set_clipboard(GeneratorState.generated_password),
                                ),
                                cast(Any, GeneratorState.copy_password),
                            ],
                            size="3",
                            radius="large",
                            width="100%",
                            style={
                                "background": "#F87B1B",
                                "color": "white",
                                "font_weight": "600",
                                "_hover": {
                                    "background": "#11224E",
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 4px 12px rgba(248, 123, 27, 0.3)",
                                },
                                "transition": "all 0.2s ease",
                            },
                        ),
                    ),
                    width="100%",
                    spacing="2",
                ),
                padding="24px",
                bg="white",
                border_radius="16px",
                border="1px solid",
                border_color="#EEEEEE",
                box_shadow="0 4px 6px rgba(17, 34, 78, 0.1)",
                width="100%",
            ),
            spacing="4",
            width="100%",
            max_width="600px",
        ),
        padding="32px",
        bg="white",
        border_radius="24px",
        box_shadow="0 20px 50px rgba(17, 34, 78, 0.15)",
        border="1px solid",
        border_color="#EEEEEE",
        width="100%",
        max_width="700px",
        margin="0 auto",
    )
