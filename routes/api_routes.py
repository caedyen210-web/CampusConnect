
from flask import Blueprint, render_template, jsonify
import json
import urllib.error
import urllib.parse
import urllib.request



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
        query = urllib.parse.urlencode(params)
        request = urllib.request.Request(
            f"{url}?{query}",
            headers={"User-Agent": "CampusConnect"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            weather_data = json.loads(response.read().decode("utf-8"))

        return jsonify(weather_data["current"])

    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as error:
        return jsonify({"error": str(error)}), 500

    