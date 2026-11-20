
from flask import Blueprint, render_template, jsonify
import requests



api_routes = Blueprint("api_routes", __name__)


@api_routes.route("/api")
def api():
    return render_template("api.html")


@api_routes.route("/api/weather-data")
def weather_data():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 41.8975,
        "longitude": -84.0372,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "America/Detroit"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return jsonify(response.json()["current"])

    except requests.RequestException as error:
        return jsonify({"error": str(error)}), 500
