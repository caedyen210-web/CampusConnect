
from flask import Flask, render_template, redirect, url_for, session
import os

from routes.auth_routes import auth_bp
from routes.api_routes import api_routes
from routes.event_routes import event_routes

app = Flask(__name__)

# Secret key is used to protect login sessions.
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "campusconnect-development-key"
)

app.template_folder = "templates"
app.static_folder = "static"


# Homepage - requires login.
@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    return render_template("index.html")


# Register application routes.
app.register_blueprint(auth_bp)
app.register_blueprint(api_routes)
app.register_blueprint(event_routes)


if __name__ == "__main__":
    app.run(debug=True)
