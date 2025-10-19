import reflex as rx


def description_component() -> rx.Component:
    """A description component for the password generator app."""
    return rx.vstack(
        rx.text(
            "This is a simple and effective program developed in Python designed to generate secure and random passwords. Its main function is to ask the user for the desired password length and, based on that, create a robust combination of characters.",
            mb="4",
        ),
        rx.text("Key Features:", font_weight="bold", size="5", mb="3"),
        rx.vstack(
            # Feature 1
            rx.hstack(
                rx.icon("circle_check_big", color="green", size=16),
                rx.text("Random Generation", font_weight="bold"),
                align_items="center",
                spacing="2",
            ),
            rx.text(
                "Creates passwords using a mix of letters (upper and lower case), numbers, and special characters to maximize security.",
                ml="6",
                mb="4",
                color="gray.600",
            ),
            # Feature 2
            rx.hstack(
                rx.icon("circle_check_big", color="green", size=16),
                rx.text("Length Recommendation", font_weight="bold"),
                align_items="center",
                spacing="2",
            ),
            rx.text(
                "The program suggests a minimum length of 8 characters to ensure a good level of password strength.",
                ml="6",
                mb="4",
                color="gray.600",
            ),
            # Feature 3
            rx.hstack(
                rx.icon("circle_check_big", color="green", size=16),
                rx.text("Error Handling", font_weight="bold"),
                align_items="center",
                spacing="2",
            ),
            rx.text(
                "Includes robust validations to handle invalid user input, such as: Non-numeric values and Negative numbers or zero.",
                ml="6",
                mb="4",
                color="gray.600",
            ),
            spacing="1",
        ),
        spacing="2",
        align_items="start",
        width="100%",
    )
