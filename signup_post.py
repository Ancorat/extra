from bottle import post, view, request, redirect
import uuid
import g
import re


@post("/signup")
def _():
    user_id = str(uuid.uuid4())
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    last_name = request.forms.get("last_name")
    first_name = request.forms.get("first_name")

    if not request.forms.get("user_email"):
        return redirect(f"/signup?error=user_email&first_name={first_name}&ulast_name={last_name}")
    if not re.match(g.REGEX_EMAIL,user_email):
        return redirect(f"/signup?error=user_email&first_name={first_name}&last_name={last_name}")

    if not user_password:
        return redirect(f"/signup?error=user_password&first_name={first_name}&last_name={last_name}&user_email={user_email}")
    if len(user_password) < 8:
        return redirect(f"/signup?error=user_password&first_name={first_name}&last_name={last_name}&user_email={user_email}")

    if len(first_name) < 2:
        return redirect(f"/signup?error=first_name&first_name={first_name}&last_name={last_name}&user_email={user_email}")
    if len(first_name) > 60:
        return redirect(f"/signup?error=first_name&first_name={first_name}&last_name={last_name}&user_email={user_email}")
    
    if len(last_name) < 2:
        return redirect(f"/signup?error=last_name&first_name={first_name}&last_name={last_name}&user_email={user_email}")
    if len(last_name) > 60:
        return redirect(f"/signup?error=last_name&first_name={first_name}&last_name={last_name}&user_email={user_email}")

    user = {"user_id":user_id, "user_email":user_email, "user_password":user_password, "last_name":last_name, "first_name":first_name} 

    print(user)

    g.USERS.append(user)

    return redirect("/login")

