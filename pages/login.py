from fasthtml.common import *  # noqa
from .components.header import header_comp


def login_element(session):
  return (
    Div(cls='hero min-h-screen')(
        Div(cls='hero-content flex-col lg:flex-row-reverse')(
            Div(cls='text-center lg:text-left')(
                H1('Login now!', cls='text-5xl font-bold'),
                P('Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem\r\n        quasi. In deleniti eaque aut repudiandae et a id nisi.', cls='py-6')
            ),
            Div(cls='card bg-base-100 w-full max-w-lg shrink-0 shadow-2xl')(
                Form(cls='card-body', hx_post="/login",hx_target=None)(
                    Div(cls='form-control')(
                        Label(cls='label')(
                            Span('Email', cls='label-text')
                        ),
                        Input(type='text', placeholder='email', required='', cls='input input-bordered', name='email')
                    ),
                    Div(cls='form-control')(
                        Label(cls='label')(
                            Span('Password', cls='label-text')
                        ),
                        Input(type='password',  name="password",placeholder='password', required='', cls='input input-bordered'),
                        Label(cls='label')(
                            A('Forgot password?', href='#', cls='label-text-alt link link-hover')
                        )
                    ),
                    Div(cls='form-control mt-6')(
                        Button('Login', cls='btn btn-primary', type='submit')
                    )
                )
            )
        )
    )
  )

def login_page(session):
  return Div(cls="min-h-screen")(
      header_comp(session),
      Div(id="hero-element",
          cls="min-h-screen min-w-screen")(login_element(session)),
  )