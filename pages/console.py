from fasthtml.common import *  # noqa
from .components.header import header_comp

def console_component(session):
  return H1("Hello")

def console_page(session):
  return Div(cls="min-h-screen")(
      header_comp(session),
      Div(id="hero-element",
          cls="min-h-screen min-w-screen")(console_component(session)),
  )
