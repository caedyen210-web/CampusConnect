const weatherButton = document.getElementById("weather-button");

weatherButton.addEventListener("click", getWeather);

async function getWeather() {

    const latitude = 34.2749;
    const longitude = -81.6187;

    const weatherURL =
        `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,wind_speed_10m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone=America%2FNew_York&forecast_days=7`;

    weatherButton.textContent = "Loading...";
    weatherButton.disabled = true;

    try {

        const response = await fetch(weatherURL);

        if (!response.ok) {
            throw new Error("Unable to retrieve weather.");
        }

        const data = await response.json();

        // Current temperature
        document.getElementById("temperature").textContent =
            Math.round(data.current.temperature_2m) + "°F";

        // Current conditions
        document.getElementById("conditions").textContent =
            getWeatherDescription(data.current.weather_code);

        // Current wind
        document.getElementById("wind").textContent =
            "Wind: " + Math.round(data.current.wind_speed_10m) + " mph";

        // Weekly forecast
        const forecastContainer =
            document.getElementById("forecastCards");

        forecastContainer.innerHTML = "";

        for (let i = 0; i < data.daily.time.length; i++) {

            const dateParts = data.daily.time[i].split("-");

            const date = new Date(
                Number(dateParts[0]),
                Number(dateParts[1]) - 1,
                Number(dateParts[2])
            );

            const day = date.toLocaleDateString("en-US", {
                weekday: "long"
            });

            const high = Math.round(data.daily.temperature_2m_max[i]);
            const low = Math.round(data.daily.temperature_2m_min[i]);
            const rain = data.daily.precipitation_probability_max[i];
            const wind = Math.round(data.daily.wind_speed_10m_max[i]);

            const weather = getWeatherDescription(
                data.daily.weather_code[i]
            );

            const card = document.createElement("div");

            card.className = "col-12 col-md-6 col-lg-4";

            card.innerHTML = `
                <div class="card weather-card h-100">
                    <div class="card-body text-center">

                        <h2>${day}</h2>

                        <h3>${weather}</h3>

                        <h1>${high}°F</h1>

                        <p>Low: ${low}°F</p>

                        <p>${rain ?? "N/A"}% chance of rain</p>

                        <p>Wind: ${wind} mph</p>

                    </div>
                </div>
            `;

            forecastContainer.appendChild(card);

        }

    } catch (error) {

        console.error(error);

        document.getElementById("conditions").textContent =
            "Unable to load weather. Please try again.";

    } finally {

        weatherButton.textContent = "Check Weather";
        weatherButton.disabled = false;

    }

}


// Weather descriptions
function getWeatherDescription(code) {

    const weatherCodes = {

        0: "Clear Sky ☀️",
        1: "Mostly Clear 🌤️",
        2: "Partly Cloudy ⛅",
        3: "Cloudy ☁️",
        45: "Foggy 🌫️",
        48: "Foggy 🌫️",
        51: "Light Drizzle 🌦️",
        53: "Drizzle 🌦️",
        55: "Heavy Drizzle 🌧️",
        61: "Light Rain 🌧️",
        63: "Rain 🌧️",
        65: "Heavy Rain 🌧️",
        71: "Light Snow ❄️",
        73: "Snow ❄️",
        75: "Heavy Snow ❄️",
        80: "Rain Showers 🌦️",
        81: "Rain Showers 🌧️",
        82: "Heavy Rain Showers 🌧️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with Hail ⛈️",
        99: "Severe Thunderstorm ⛈️"

    };

    return weatherCodes[code] || "Weather Conditions Unknown";

}