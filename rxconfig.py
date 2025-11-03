import reflex as rx

config = rx.Config(
    app_name="password_generator",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
