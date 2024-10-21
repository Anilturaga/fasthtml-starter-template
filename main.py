from fasthtml.common import *  # noqa
import json
import copy

from utils import *
from auth.loginHandler import loginHandler
from pages.components.header import header_comp
from pages.index import index_hero, index_page
from pages.components.loginDialogIndex import login_form

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
        themes: ["cupcake","black","business","dim","corporate","night","nord","dracula"],
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


# login dialog on index page
@rt("/login-dialog")
def post_dialog():
    return login_form()


@rt("/close-login-dialog")
def post_close_dialog(session):
    return index_hero(session)


@rt("/login")
def post(session, email: str, password: str):
    res = loginHandler(email, password)
    if res:
        session["auth"] = True
        session["user"] = email
        return index_hero(session), header_comp(session)
    else:
        return RedirectResponse("/")


@rt("/logout")
def get(session):
    print("logging out")
    session.clear()
    return RedirectResponse("/")


if __name__ == "__main__":
    serve()
