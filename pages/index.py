from fasthtml.common import *  # noqa
from .components.header import header_comp


def index_hero(session):
    return (Section(cls="bg-base-100")(Div(
        cls=
        'mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center'
    )(Div(
        cls='mx-auto max-w-xl text-center'
    )(H1(cls='text-3xl font-extrabold sm:text-5xl text-base-content')(
        'Understand User Flow.',
        Br(),
        Strong('Increase Conversion.',
               cls='font-extrabold sm:block')),
      P('Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus\r\n        numquam ea!',
        cls='mt-4 sm:text-xl/relaxed text-base-content'),
      Div(cls='mt-8 flex flex-wrap justify-center gap-4')
      (A('Get Started',
         href='/login',
         cls=
         'block w-full rounded bg-primary px-12 py-3 text-sm font-medium text-primary-content shadow hover:bg-primary-darker focus:outline-none focus:ring active:bg-primary-light sm:w-auto'
         ),
       A('Learn More',
         href='/about',
         cls=
         'block w-full rounded px-12 py-3 text-sm font-medium text-neutral-content bg-neutral shadow hover:text-secondary-darker focus:outline-none focus:ring active:text-secondary-light sm:w-auto'
         ))))))


def index_page(session):
    return Div(cls="min-h-screen")(
        header_comp(session),
        Div(id="hero-element",
            cls="min-h-screen min-w-screen")(index_hero(session)),
    )
