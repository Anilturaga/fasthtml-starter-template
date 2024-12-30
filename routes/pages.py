
from fasthtml.common import *

def setup_page_routes(rt):
    @rt("/")
    def index(session):
        from pages.index import index_page
        return index_page(session)

    @rt("/console")
    def get(session):
        from pages.console import console_page
        return console_page(session)
