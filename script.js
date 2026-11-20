
// WEATHER CONDITIONS

function getWeather(code) {

    const conditions = {

        0: ["Clear Sky", "☀️"],
        1: ["Mostly Clear", "🌤️"],
        2: ["Partly Cloudy", "⛅"],
        3: ["Overcast", "☁️"],

        45: ["Foggy", "🌫️"],
        48: ["Foggy", "🌫️"],

        51: ["Light Drizzle", "🌦️"],
        53: ["Drizzle", "🌦️"],
        55: ["Heavy Drizzle", "🌧️"],

        61: ["Light Rain", "🌧️"],
        63: ["Rain", "🌧️"],
        65: ["Heavy Rain", "🌧️"],

        71: ["Light Snow", "🌨️"],
        73: ["Snow", "❄️"],
        75: ["Heavy Snow", "❄️"],

        80: ["Rain Showers", "🌦️"],
        81: ["Rain Showers", "🌧️"],
        82: ["Heavy Showers", "🌧️"],

        95: ["Thunderstorm", "⛈️"],
        96: ["Thunderstorm", "⛈️"],
        99: ["Severe Thunderstorm", "⛈️"]

    };

    return conditions[code] || ["Unknown Conditions", "🌡️"];

}


// LOAD WEATHER INFORMATION

async function loadWeather() {

    const temperature = document.getElementById("temperature");
    const description = document.getElementById("description");
    const feelsLike = document.getElementById("feelsLike");
    const humidity = document.getElementById("humidity");
    const windSpeed = document.getElementById("windSpeed");
    const weatherError = document.getElementById("weatherError");
    const refreshButton = document.getElementById("refreshWeather");

    // Stop if this is not the Weather page
    if (!temperature || !description) {
        return;
    }

    weatherError.textContent = "";
    temperature.textContent = "Loading...";
    description.textContent = "Getting weather information...";

    refreshButton.disabled = true;

    try {

        // Adrian, Michigan coordinates
        const latitude = 41.8975;
        const longitude = -84.0372;

        const url =
            `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone=America%2FDetroit`;

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Unable to retrieve weather information.");
        }

        const data = await response.json();

        const current = data.current;

        // Get weather description
        const weather = getWeather(current.weather_code);

        // Display weather information
        temperature.textContent = `${Math.round(current.temperature_2m)}°F`;

        description.textContent =
            `${weather[1]} ${weather[0]}`;

        feelsLike.textContent =
            `${Math.round(current.apparent_temperature)}°F`;

        humidity.textContent =
            `${current.relative_humidity_2m}%`;

        windSpeed.textContent =
            `${current.wind_speed_10m} mph`;

    }

    catch (error) {

        console.error("Weather Error:", error);

        temperature.textContent = "--";

        description.textContent =
            "Weather information is currently unavailable.";

        weatherError.textContent =
            "Unable to load weather. Please try again.";

    }

    finally {

        refreshButton.disabled = false;

    }

}


// REFRESH WEATHER BUTTON

document.addEventListener("DOMContentLoaded", function() {

    const refreshButton =
        document.getElementById("refreshWeather");

    if (refreshButton) {

        refreshButton.addEventListener("click", loadWeather);

        // Automatically load weather when page opens
        loadWeather();

    }

});