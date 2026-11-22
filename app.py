
from flask import Flask, render_template

from routes.api_routes import api_routes
from routes.event_routes import event_routes

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Connect Events page
app.register_blueprint(event_routes)

# Connect Weather page and API
app.register_blueprint(api_routes)


if __name__ == "__main__":
    app.run(debug=True)
