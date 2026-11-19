import flask

app = flask.Flask(__name__)

# Login page
@app.route("/login")
def login():
    return flask.render_template("login.html")

# Homepage
@app.route("/")
def home():
    return flask.render_template("index.html")

# Events page
@app.route("/events")
def events():
    return flask.render_template("events.html")

# Weather page
@app.route("/weather")
def weather():
    return flask.render_template("api.html")


if __name__ == "__main__":
    app.run(debug=True)