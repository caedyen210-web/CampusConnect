import sqlite3

# Connect to the CampusConnect database
connection = sqlite3.connect("db/campusconnect.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Create the external events table
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

# Create the weather API table
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

# Save the database changes
connection.commit()

# Close the database connection
connection.close()

print("Database tables created successfully!")