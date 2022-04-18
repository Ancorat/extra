from bottle import get, view, request

@get("/login")
@view("login")
def _():
    error = request.params.get("error")
    user_email = request.params.get("user_email")
    first_name = request.params.get("user_first_name")
    last_name = request.params.get("user_last_name")
    return dict(error=error, first_name=first_name, last_name=last_name, user_email = user_email)


#@get("/")
#@view("login")
#def _():
    #error = request.params.get("error")
    #user_email = request.params.get("user_email")
    #first_name = request.params.get("user_first_name")
    #last_name = request.params.get("user_last_name")
    #return dict(error=error, first_name=first_name, last_name=last_name, user_email = user_email)

