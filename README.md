
# CampusConnect

CampusConnect is a campus information application
that connects students with campus events and weather.

## Features

- Home page
- Campus Events
- Current Weather
- Weather refreshing
- Crimson-red design
- Navigation between pages
- Public access without login

## Requirements

Install Python and the required packages.

```bash
pip install flask requests beautifulsoup4 selenium
```

## Database Setup

Create the database:

```bash
sqlite3 db/campusconnect.db < db/schema.sql
```

Add starter data:

```bash
python db/seed_data.py
```

## Run the Application

Start CampusConnect:

```bash
python app.py
```

Open your browser:

http://127.0.0.1:5000/

## Navigation

Home:
/

Events:
/events

Weather:
/api

Weather API:
/api/weather-data