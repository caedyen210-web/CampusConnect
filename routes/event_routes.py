
import sqlite3
import os

from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    current_app
)

event_routes = Blueprint("event_routes", __name__)


@event_routes.route("/events")
def events():

    # Require the student to log in first.
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    # Connect to the existing CampusConnect database.
    database = os.path.join(
        current_app.root_path,
        "db",
        "campusconnect.db"
    )

    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    # Retrieve saved campus events.
    cursor.execute("SELECT * FROM external_events")

    events = cursor.fetchall()

    connection.close()


    return render_template(
        "events.html",
        events=events
    )
