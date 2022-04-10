from bottle import get, view, request

@get("/index")
@view("index")

def _():
    return 