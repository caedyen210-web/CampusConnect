-- Create a table to store external campus events
CREATE TABLE IF NOT EXISTS external_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date DATE,
    event_time TEXT,
    event_location TEXT,
    description TEXT
);

-- Create a table to store weather API information
CREATE TABLE IF NOT EXISTS api_data (
    api_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    weather_description TEXT,
    humidity INTEGER,
    wind_speed REAL
);