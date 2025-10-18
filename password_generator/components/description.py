import reflex as rx


def description_component() -> rx.Component:
    """A description component for the password generator app."""
    return rx.container(
        rx.text(
            "This is a simple and effective program developed in Python designed to generate secure and random passwords. Its main function is to ask the user for the desired password length and, based on that, create a robust combination of characters."
        ),
        rx.text("Key Features:"),
        rx.list(
            rx.list_item(
                rx.icon("circle_check_big", color="green", mr="2"),
                "Random Generation",
            ),
            rx.text(
                "Creates passwords using a mix of letters (upper and lower case), numbers, and special characters to maximize security."
            ),
            rx.list_item(
                rx.icon("circle_check_big", color="green", mr="2"),
                "Length Recommendation",
            ),
            rx.text(
                "The program suggests a minimum length of 8 characters to ensure a good level of password strength."
            ),
            rx.list_item(
                rx.icon("circle_check_big", color="green", mr="2"),
                "Error Handling",
            ),
            rx.text(
                "Includes robust validations to handle invalid user input, such as: Non-numeric values and Negative numbers or zero."
            ),
        ),
    )
