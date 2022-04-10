from bottle import post, view, request, redirect
import uuid
import g

@post("/login")


def _():
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    for user in g.USERS:
        if user["user_email"] == user_email and user["user_password"] == user_password:
            return redirect("/index")
    return redirect("/signup")