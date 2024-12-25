from fasthtml.common import *  # noqa
import json
import copy

from utils import *
from pages.login import login_page
from auth.loginHandler import loginHandler
from pages.components.header import header_comp
from pages.index import index_hero, index_page
from pages.login import login_element, login_page
from pages.console import console_component, console_page

# Set up the app, including daisyui and tailwind for the chat component
hdrs = (
    # Script(src="https://cdn.tailwindcss.com"),
    Script(
        src="https://cdn.tailwindcss.com?plugins=typography,aspect-ratio,container-queries"
    ),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css",
    ),
    # icons
    Script(src="https://unpkg.com/lucide@latest"),
    Script(
        """
        setTimeout(() => {
            lucide.createIcons();
        }, 50);
        """
    ),
    Script(
        """
    tailwind.config = {
      daisyui: {
        themes: ["cupcake","black","business","dim","corporate","night","nord","dracula", "lofi"],
      },

    };
    """
    ),
    MarkdownJS(),
    HighlightJS(langs=["python", "javascript", "html", "css"]),
)


# Auth middleware
def auth_check(req, sess):
    # print("request",req)
    auth = req.scope["auth"] = sess.get("auth", None)
    if not auth:
        return RedirectResponse("/", status_code=303)


beforeware = Beforeware(
    auth_check,
    skip=[
        r"/",
        r"/login",
        r"/login-dialog",
        r"/close-login-dialog",
    ],  # Don't check auth for these routes
)

# black, nord
app, rt = fast_app(
    hdrs=hdrs, debug=True, htmlkw={"data-theme": "cupcake"}, before=beforeware
)


# The main screen
@rt("/")
def index(session):
    return index_page(session)

@rt("/login")
def get(session):
    return login_page(session)

@rt("/console")
def get(session):
    return console_page(session)

@rt("/login")
def post(session, email: str, password: str):
    print(email, password)
    res = loginHandler(email, password)
    if res:
        print("AAAAA")
        session["auth"] = True
        session["user"] = email
        return Response(
            "Redirecting...",
            headers={"HX-Redirect": "/console"}
        )
    else:
        return Response(
            "Redirecting...",
            headers={"HX-Redirect": "/login"}
        )

@rt("/logout")
def get(session):
    print("logging out")
    session.clear()
    return RedirectResponse("/")


if __name__ == "__main__":
    serve()
