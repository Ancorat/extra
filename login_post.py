from bottle import post, view, request, redirect
import uuid
import g

@post("/login")


def _():
    user_email = request.forms.get("user_email")

    user_password = request.forms.get("user_password")
    user_session_id = str(uuid.uuid4())

    g.SESSIONS.append(user_session_id)

    for user in g.USERS:
        if user["user_email"] == user_email and user["user_password"] == user_password:
            return redirect("/index")
    return redirect("/login?error=wrong_credentials")