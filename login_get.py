from bottle import get, view, request

@get("/login")
@view("login")

def _():
    user_email = request.params.get("user_email")
    return dict(user_email = user_email)