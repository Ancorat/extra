from bottle import post, view, request, redirect
import uuid
import g
@post("/signup")


def _():
    user_id = str(uuid.uuid4())
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    user = {"user_id":user_id, "user_email":user_email, "user_password":user_password} 
    g.USERS.append(user)
    return redirect("/login")

