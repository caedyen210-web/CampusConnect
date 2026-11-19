
import requests

from flask import (
    Blueprint,
    jsonify,
    render_template,
    session,
    redirect,
    url_for
)

api_routes = Blueprint("api_routes", __name__)

# Weather page.
@api_routes.route("/api")
def api():

    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    return render_template("api.html")


# Weather API endpoint.
@api_routes.route("/api/weather-data")
def weather_data():

    if not session.get("logged_in"):
        return jsonify({"error": "Please log in first."}), 401

    # Adrian, Michigan coordinates.
    latitude = 41.8975
    longitude = -84.0372

    weather_url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "America/Detroit"
    }

    try:
        response = requests.get(
            weather_url,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return jsonify(data)

    except requests.RequestException as error:

        print("Weather API error:", error)

        return jsonify({
            "error": "Unable to retrieve weather information."
        }), 500
