import reflex as rx
from password_generator.components.title import title_component
from password_generator.components.description import description_component
from password_generator.components.generator_psw_box import generator_psw_box
from password_generator.layout.footer import footer_component

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)

    # JSON-LD structured data for SEO
    schema_data = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Secure Password Generator",
        "description": "Generate secure and random passwords instantly with our free password generator tool",
        "url": "https://password-generator.reflex.run/",
        "applicationCategory": "SecurityApplication",
        "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "featureList": [
            "Random password generation",
            "Customizable password length",
            "Password strength indicator",
            "One-click copy to clipboard",
            "No data storage - 100% secure",
        ],
        "browserRequirements": "Requires JavaScript enabled",
    }

    return rx.box(
        # Add JSON-LD script for structured data
        rx.script(
            f'var script = document.createElement("script"); script.type = "application/ld+json"; script.text = {repr(str(schema_data).replace("'", '"'))}; document.head.appendChild(script);'
        ),
        rx.container(
            rx.el.header(
                title_component(),
            ),
            rx.el.main(
                description_component(),
                generator_psw_box(),
                role="main",
            ),
            rx.el.footer(
                footer_component(),
                role="contentinfo",
            ),
            size="4",
        ),
        # Background with solid color
        style={
            "min_height": "100vh",
            "background": "#EEEEEE",
        },
    )


app = rx.App()
app.add_page(
    index,
    title="Secure Password Generator | Create Strong Passwords Online Free",
    description="Generate secure and random passwords instantly with our free password generator tool. Create strong passwords with custom length and character combinations. 100% secure, no data stored.",
    image="/preview.png",
    meta=[
        # Open Graph / Facebook
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": "https://password-generator.reflex.run/"},
        {
            "property": "og:title",
            "content": "Secure Password Generator | Create Strong Passwords Online Free",
        },
        {
            "property": "og:description",
            "content": "Generate secure and random passwords instantly. Free, easy to use, and 100% secure. No passwords stored.",
        },
        {"property": "og:image", "content": "/preview.png"},
        # Twitter
        {"name": "twitter:card", "content": "summary_large_image"},
        {
            "name": "twitter:title",
            "content": "Secure Password Generator | Create Strong Passwords",
        },
        {
            "name": "twitter:description",
            "content": "Generate secure and random passwords instantly. Free, easy to use, and 100% secure.",
        },
        {"name": "twitter:image", "content": "/preview.png"},
        # Additional SEO tags
        {
            "name": "keywords",
            "content": "password generator, secure password, random password, strong password, password creator, free password generator, online password tool",
        },
        {"name": "author", "content": "Secure Password Generator"},
        {"name": "robots", "content": "index, follow"},
        {"name": "language", "content": "English"},
        {"name": "revisit-after", "content": "7 days"},
        # Mobile optimization
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        {"name": "theme-color", "content": "#11224E"},
        {"name": "apple-mobile-web-app-capable", "content": "yes"},
        {
            "name": "apple-mobile-web-app-status-bar-style",
            "content": "black-translucent",
        },
        # PWA Manifest
        {"name": "manifest", "content": "/manifest.json"},
    ],
)
