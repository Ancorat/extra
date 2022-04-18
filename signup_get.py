from bottle import get, view, request

@get("/signup")
@view("signup")

def _():
    error = request.params.get("error")
    first_name = request.params.get("first_name")
    last_name = request.params.get("last_name")
    user_email = request.params.get("user_email")
    return dict(error=error, first_name=first_name, last_name=last_name, user_email=user_email)