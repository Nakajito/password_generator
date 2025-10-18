import reflex as rx


def generator_psw_box() -> rx.Component:
    return rx.box(
        rx.text("Enter the password length:", size="5", font_weight="bold", mb="2"),
        rx.input(
            id="password_length",
            placeholder="e.g., 12",
            is_read_only=False,
            width="20%",
            mb="4",
        ),
        rx.button(
            "Create Password",
            id="create_button",
            color_scheme="teal",
            width="30%",
        ),
        rx.text("Password will be displayed here", font_weight="bold", size="7"),
        padding="4",
        width="60%",
    )
