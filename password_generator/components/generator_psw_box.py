import reflex as rx


class GeneratorState(rx.State):
    password_length: str = ""
    generated_password: str = "Password will be displayed here"

    def set_password_length(self, value: str):
        self.password_length = value

    def create_password(self):
        try:
            length = int(self.password_length)
            if length > 0:
                # Aquí puedes llamar a tu función de generación de contraseña
                self.generated_password = self.generate_password_function(length)
            else:
                self.generated_password = "Please enter a valid length"
        except ValueError:
            self.generated_password = "Please enter a valid number"

    def generate_password_function(self, length: int) -> str:
        # Tu lógica para generar la contraseña aquí
        import random
        import string

        characters = string.ascii_letters + string.digits + "!@#$%&*"
        password = "".join(random.choice(characters) for _ in range(length))
        return password


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
                on_change=GeneratorState.set_password_length,
                width="60%",
                mb="4",
            ),
            rx.button(
                "Generate Password",
                on_click=GeneratorState.create_password,
                color_scheme="teal",
                width="40%",
            ),
            width="100%",
        ),
        rx.text(
            GeneratorState.generated_password,
            font_weight="bold",
            size="7",
            color_scheme="green",
        ),
        padding="4",
        size="3",
        align="center",
    )
