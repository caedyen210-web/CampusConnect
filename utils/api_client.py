import requests
import sqlite3
import re


class WeatherAPI:

    # Constructor stores the API key and base URL
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherapi.com/v1/current.json"

    # Request weather information from WeatherAPI
    def get_weather(self, city):
        params = {
            "key": self.api_key,
            "q": city
        }

        response = requests.get(
            self.base_url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    # Extract and clean the weather information
    def parse_weather_data(self, data):
        weather = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_f"],
            "weather_description": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_mph"]
        }

        # Remove unwanted characters from the description
        weather["weather_description"] = re.sub(
            r"[^a-zA-Z0-9 ]", "",
            weather["weather_description"]
        )

        return weather

    # Save weather information into SQLite
    def save_api_data(self, weather):
        connection = sqlite3.connect("db/campusconnect.db")
        cursor = connection.cursor()

        # Replace the previous weather record for this city
        cursor.execute(
            "DELETE FROM api_data WHERE city = ?",
            (weather["city"],)
        )

        cursor.execute("""
            INSERT INTO api_data
            (city, temperature, weather_description,
             humidity, wind_speed)
            VALUES (?, ?, ?, ?, ?)
        """, (
            weather["city"],
            weather["temperature"],
            weather["weather_description"],
            weather["humidity"],
            weather["wind_speed"]
        ))

        connection.commit()
        connection.close()