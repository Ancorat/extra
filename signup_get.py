from bottle import get, view, request

@get("/signup")
@view("signup")

def _():
    user_email = request.params.get("user_email")
    return dict(user_email = user_email)