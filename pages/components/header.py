from fasthtml.common import *  # noqa
from utils import generate_random_string


def header_comp(session):
    if session.get("auth"):
        return Div(cls="navbar bg-base-100", hx_swap_oob="true", id="header")(
            Div(cls="navbar-start")(
                A(
                    # replace with your logo
                    Kbd(cls="kbd text-base-content")("Your Logo Here"),
                    href="/",
                )
            ),
            Div(cls="navbar-end")(A("Logout", cls="btn btn-ghost", href="/logout")),
        )
    else:
        return Div(cls="navbar bg-base-100", hx_swap_oob="true", id="header")(
            Div(cls="navbar-start")(
                # replace with your logo
                A(Kbd(cls="kbd text-base-content")("Your Logo Here"), href="/")
            ),
            # Div(cls="navbar-end")(A("Login", cls="btn")),
        )
