
import sqlite3
from datetime import date, timedelta

# Connect to database
connection = sqlite3.connect("db/campusconnect.db")


cursor = connection.cursor()


# Create campus events table
cursor.execute("""
CREATE TABLE IF NOT EXISTS external_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date DATE,
    event_time TEXT,
    event_location TEXT,
    description TEXT
)
""")


# Create weather data table
cursor.execute("""
CREATE TABLE IF NOT EXISTS api_data (
    api_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    weather_description TEXT,
    humidity INTEGER,
    wind_speed REAL
)
""")


# Check whether sample events already exist
event_count = cursor.execute("""
SELECT COUNT(*) FROM external_events
""").fetchone()[0]


if event_count == 0:

    # Find the next Monday
    today = date.today()

    days_until_monday = (
        7 - today.weekday()
    ) % 7

    if days_until_monday == 0:
        days_until_monday = 7

    next_monday = today + timedelta(
        days=days_until_monday
    )


    # Six campus events
    sample_events = [

        (
            "Student Welcome Meeting",
            "10:00 AM",
            "Student Center",
            "Meet other students and learn about campus."
        ),

        (
            "Campus Club Fair",
            "12:00 PM",
            "Main Quad",
            "Discover student organizations and clubs."
        ),

        (
            "Career Development Workshop",
            "2:00 PM",
            "Library",
            "Learn about resumes and career opportunities."
        ),

        (
            "Intramural Sports",
            "4:00 PM",
            "Sports Complex",
            "Participate in recreational campus sports."
        ),

        (
            "Campus Movie Night",
            "7:00 PM",
            "Auditorium",
            "Enjoy a movie with fellow students."
        ),

        (
            "Community Volunteer Day",
            "9:00 AM",
            "Campus Entrance",
            "Participate in a campus volunteer activity."
        )

    ]


    # Insert six events
    for index, event in enumerate(sample_events):

        event_date = (
            next_monday + timedelta(days=index)
        )

        cursor.execute("""
        INSERT INTO external_events
        (
            event_name,
            event_date,
            event_time,
            event_location,
            description
        )

        VALUES (?, ?, ?, ?, ?)
        """, (
            event[0],
            event_date.isoformat(),
            event[1],
            event[2],
            event[3]
        ))


# Save changes
connection.commit()


connection.close()

print("CampusConnect database setup complete!")