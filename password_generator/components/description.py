import reflex as rx


def description_component() -> rx.Component:
    """A description component for the password generator app."""
    return rx.box(
        rx.vstack(
            # Introduction card
            rx.box(
                rx.text(
                    "A simple and effective tool to generate secure and random passwords. Choose your desired length and get a robust combination of characters instantly.",
                    size="4",
                    color="#11224E",
                    line_height="1.7",
                    text_align="center",
                ),
                padding="24px",
                bg="rgba(203, 217, 155, 0.3)",
                border_radius="16px",
                border="1px solid",
                border_color="#CBD99B",
                mb="6",
            ),
            # Features section with cards
            rx.heading(
                "Key Features",
                size="6",
                font_weight="bold",
                color="#11224E",
                mb="4",
                text_align="center",
            ),
            rx.grid(
                # Feature 1
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("shuffle", size=32, color="#F87B1B"),
                            padding="12px",
                            bg="#EEEEEE",
                            border_radius="12px",
                            mb="3",
                        ),
                        rx.text(
                            "Random Generation",
                            font_weight="bold",
                            size="4",
                            color="#11224E",
                            mb="2",
                        ),
                        rx.text(
                            "Uses cryptographically secure random generation with letters, numbers, and special characters.",
                            size="2",
                            color="#11224E",
                            line_height="1.6",
                            text_align="center",
                            opacity="0.8",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    padding="24px",
                    bg="white",
                    border_radius="16px",
                    border="1px solid",
                    border_color="#EEEEEE",
                    box_shadow="0 4px 6px rgba(17, 34, 78, 0.08)",
                    style={
                        "_hover": {
                            "box_shadow": "0 10px 20px rgba(248, 123, 27, 0.2)",
                            "transform": "translateY(-4px)",
                            "border_color": "#F87B1B",
                        },
                        "transition": "all 0.3s ease",
                    },
                ),
                # Feature 2
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("gauge", size=32, color="#F87B1B"),
                            padding="12px",
                            bg="#EEEEEE",
                            border_radius="12px",
                            mb="3",
                        ),
                        rx.text(
                            "Strength Indicator",
                            font_weight="bold",
                            size="4",
                            color="#11224E",
                            mb="2",
                        ),
                        rx.text(
                            "Real-time password strength evaluation based on length with visual feedback.",
                            size="2",
                            color="#11224E",
                            line_height="1.6",
                            text_align="center",
                            opacity="0.8",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    padding="24px",
                    bg="white",
                    border_radius="16px",
                    border="1px solid",
                    border_color="#EEEEEE",
                    box_shadow="0 4px 6px rgba(17, 34, 78, 0.08)",
                    style={
                        "_hover": {
                            "box_shadow": "0 10px 20px rgba(248, 123, 27, 0.2)",
                            "transform": "translateY(-4px)",
                            "border_color": "#F87B1B",
                        },
                        "transition": "all 0.3s ease",
                    },
                ),
                # Feature 3
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("clipboard_check", size=32, color="#F87B1B"),
                            padding="12px",
                            bg="#EEEEEE",
                            border_radius="12px",
                            mb="3",
                        ),
                        rx.text(
                            "Easy Copy",
                            font_weight="bold",
                            size="4",
                            color="#11224E",
                            mb="2",
                        ),
                        rx.text(
                            "One-click copy to clipboard with instant visual confirmation for seamless usage.",
                            size="2",
                            color="#11224E",
                            line_height="1.6",
                            text_align="center",
                            opacity="0.8",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    padding="24px",
                    bg="white",
                    border_radius="16px",
                    border="1px solid",
                    border_color="#EEEEEE",
                    box_shadow="0 4px 6px rgba(17, 34, 78, 0.08)",
                    style={
                        "_hover": {
                            "box_shadow": "0 10px 20px rgba(248, 123, 27, 0.2)",
                            "transform": "translateY(-4px)",
                            "border_color": "#F87B1B",
                        },
                        "transition": "all 0.3s ease",
                    },
                ),
                columns="3",
                spacing="5",
                width="100%",
                style={
                    "@media (max-width: 768px)": {
                        "grid_template_columns": "1fr",
                    },
                },
            ),
            spacing="4",
            width="100%",
            max_width="1000px",
            margin="0 auto",
        ),
        padding="20px",
        mb="8",
    )
