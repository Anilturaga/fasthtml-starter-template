from fasthtml.common import *  # noqa
from .components.header import header_comp


def index_hero(session):
    return (
        Div(cls="hero bg-base min-h-screen")(
            Div(cls="hero-content text-center")(
                Div(cls="max-w-md")(
                    H1(
                        "FastHTML Starter Kit",
                        cls="text-4xl font-bold text-base-content",
                    ),
                    P(
                        "Build full-stack web apps with Python and HTML!",
                        cls="py-6 text-base-content",
                    ),
                    (
                        A(
                            "Go to console",
                            cls="btn btn-primary",
                            href="/console",
                        )
                        if session.get("auth")
                        else Button(
                            "Login",
                            cls="btn btn-primary",
                            hx_post="/login-dialog",
                            hx_target="#hero-element",
                            hx_swap="content",
                            hx_trigger="click",
                        )
                    ),
                )
            )
        ),
    )


def index_page(session):
    return Div(cls="min-h-screen")(
        header_comp(session),
        Div(id="hero-element", cls="min-h-screen min-w-screen")(index_hero(session)),
    )
