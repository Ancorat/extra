from bottle import get, view, request

@get("/tweets")
@view("tweet")

def _():
    return