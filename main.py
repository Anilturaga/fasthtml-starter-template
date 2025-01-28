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
    # favicon
    Link(
        rel="icon",
        href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗂️</text></svg>",
        type="image/svg+xml",
    ),
    Script(
        src="https://cdn.tailwindcss.com?plugins=typography,aspect-ratio,container-queries"
    ),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css",
    ),
    # icons
    # Script(src="https://unpkg.com/lucide@latest"),
    # Script(
    #     """
    #     setTimeout(() => {
    #         lucide.createIcons();
    #     }, 50);
    #     """
    # ),
    Script(
        """
    tailwind.config = {
      daisyui: {
        themes: ["cupcake","black","business","dim","corporate","night","nord","dracula", "lofi"],
      },
    };
    document.title ="FastHTML Template";
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


# Setup routes from modules
from routes.auth import setup_auth_routes
from routes.pages import setup_page_routes

setup_auth_routes(rt)
setup_page_routes(rt)


if __name__ == "__main__":
    serve()
