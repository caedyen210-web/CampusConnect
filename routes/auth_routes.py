
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

auth_bp = Blueprint("auth", __name__)

# Temporary demonstration login.
DEMO_EMAIL = "student@campus.edu"
DEMO_PASSWORD = "campus123"


# Login page.
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Check the login information.
        if email == DEMO_EMAIL and password == DEMO_PASSWORD:

            session["logged_in"] = True
            session["email"] = email

            return redirect(url_for("index"))

        flash("Incorrect email or password.")

    return render_template("login.html")


# Logout page.
@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))