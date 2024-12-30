
from fasthtml.common import *
from auth.loginHandler import loginHandler

def setup_auth_routes(rt):
    @rt("/login")
    def get(session):
        from pages.login import login_page
        return login_page(session)

    @rt("/login")
    def post(session, email: str, password: str):
        res = loginHandler(email, password)
        if res:
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
        session.clear()
        return RedirectResponse("/")
