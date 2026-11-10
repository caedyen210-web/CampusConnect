import sqlite3
import os

from flask import Blueprint, render_template
try:
    from ..utils.api import WeatherAPI # type: ignore
except ImportError:
    from utils.api import WeatherAPI # type: ignore

# Create the API blueprint
api_routes = Blueprint("api_routes", __name__)

# Get your API key from an environment variable
API_KEY = os.environ.get("WEATHER_API_KEY")


@api_routes.route("/api")
def api():

    # Connect to the database
    connection = sqlite3.connect("db/campusconnect.db")
    connection.row_factory = sqlite3.Row

    # Create the WeatherAPI object
    weather_api = WeatherAPI(API_KEY) if API_KEY else None

    if weather_api:
        try:
            # Get weather information for Adrian, Michigan
            weather_data = weather_api.get_weather("Adrian")

            # Clean the returned information
            cleaned_data = weather_api.parse_weather_data(weather_data)

            # Save weather information in the database
            weather_api.save_api_data(cleaned_data)

        except Exception as error:
            print("Weather API error:", error)

    # Retrieve weather information from SQLite
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_data")
    api_data = cursor.fetchall()

    connection.close()

    # Display weather information
    return render_template("api.html", api_data=api_data)