from fasthtml.common import *  # noqa


def login_form():
    return Div(cls="hero bg-base-200 min-h-screen")(
        Div(cls="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl")(
            Div(
                "Login",
                cls="items-center justify-center flex flex-col text-4xl font-bold text-base-content mt-6",
            ),
            Form(
                Div(cls="form-control")(
                    Label(cls="label")(Span("Email", cls="label-text")),
                    Input(
                        type="text",
                        placeholder="email",
                        required="",
                        cls="input input-bordered",
                        name="email",
                    ),
                ),
                Div(cls="form-control")(
                    Label(cls="label")(Span("Password", cls="label-text")),
                    Input(
                        type="password",
                        placeholder="password",
                        required="",
                        cls="input input-bordered",
                        name="password",
                    ),
                    # Label(cls='label')(
                    #     A('Forgot password?', href='#', cls='label-text-alt link link-hover')
                    # )
                ),
                Div(cls="form-control mt-6")(
                    Button("Login", cls="btn btn-primary ", type="submit")
                ),
                cls="card-body",
                hx_post="/login",
                hx_target="#hero-element",
                hx_swap="innerHTML",
            ),
            Button(
                "Cancel",
                cls="btn bg-warning",
                hx_post="/close-login-dialog",
                hx_target="#hero-element",
                hx_swap="innerHTML",
                hx_trigger="click",
            ),
        )
    )
