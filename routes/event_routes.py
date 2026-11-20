
from flask import Blueprint, render_template
import sqlite3
import os



event_routes = Blueprint("event_routes", __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, "db", "campusconnect.db")


@event_routes.route("/events")
def events():
    events_list = []

    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row

        table_exists = connection.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='external_events'
        """).fetchone()

        if table_exists:
            rows = connection.execute(
                "SELECT * FROM external_events"
            ).fetchall()

            for row in rows:
                data = dict(row)

                events_list.append({
                    "name": data.get("event_name") or data.get("name") or data.get("title", "Untitled Event"),
                    "date": data.get("event_date") or data.get("date") or data.get("start_date", ""),
                    "time": data.get("time", ""),
                    "location": data.get("location", ""),
                    "description": data.get("description", "")
                })

        connection.close()

    except sqlite3.Error as error:
        print("Database error:", error)

    return render_template("events.html", events=events_list)
