import reflex as rx
from typing import Any, cast

from password_generator.utils import generate_password


class GeneratorState(rx.State):
    password_length: str = ""
    generated_password: str = "Password will be displayed here"
    copied: bool = False
    error_message: str = ""
    MIN_LENGTH: int = 8

    def set_password_length(self, value: str):
        self.password_length = value

    def create_password(self):
        try:
            length = int(self.password_length)
            if length > 0:
                # Delegate to the shared utility for easier testing.
                self.generated_password = generate_password(length)
                # Reset copy/info flags
                self.copied = False
                self.error_message = ""
            else:
                self.generated_password = "Please enter a valid length"
                self.error_message = "Length must be greater than 0"
        except ValueError:
            self.generated_password = "Please enter a valid number"
            self.error_message = "Please enter a valid number"

    def generate_password_function(self, length: int) -> str:
        # Kept for backward compatibility; prefer using `generate_password`.
        return generate_password(length)

    def copy_password(self, _result: object | None = None):
        """Mark the password as copied; placeholder for clipboard support.

        A real clipboard copy would be done client-side (e.g. with
        navigator.clipboard.writeText). Implementing a full client-side
        call can be added later with a small JS helper event.
        """
        if (
            self.generated_password
            and "Password will be" not in self.generated_password
        ):
            self.copied = True
        else:
            self.copied = False


def generator_psw_box() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Enter the password length:",
            size="7",
            font_weight="bold",
            mb="2",
            as_="h2",
        ),
        rx.hstack(
            rx.input(
                placeholder="e.g., 12",
                value=GeneratorState.password_length,
                on_change=cast(Any, GeneratorState.set_password_length),
                width="60%",
                mb="4",
            ),
            rx.button(
                "Generate Password",
                on_click=cast(Any, GeneratorState.create_password),
                color_scheme="teal",
                # Disable when input is empty or obviously invalid.
                disabled=cast(Any, GeneratorState.password_length == ""),
                width="40%",
            ),
            width="100%",
        ),
        # Helper / error text
        rx.text(
            f"Recommended minimum length: {GeneratorState.MIN_LENGTH}",
            size="2",
            color="gray.600",
            mb="2",
        ),
        rx.text(GeneratorState.error_message, color="red.500", mb="2"),
        # Result area with copy button
        rx.hstack(
            rx.text(
                GeneratorState.generated_password,
                font_weight="bold",
                size="7",
                color_scheme="green",
            ),
            rx.button(
                "Copy",
                # Use Reflex helper to call navigator.clipboard.writeText on the client.
                # Provide `GeneratorState.copy_password` as callback to mark copied server-side.
                on_click=cast(
                    Any,
                    rx.event.set_clipboard(GeneratorState.generated_password),
                ),
                ml="4",
                color_scheme="gray",
            ),
            align_items="center",
            spacing="3",
        ),
        padding="4",
        size="3",
        align="center",
    )
