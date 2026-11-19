
// Wait until the HTML document has loaded.
document.addEventListener("DOMContentLoaded", function () {

    console.log("CampusConnect JavaScript loaded!");

    // ============================================
    // 1. EVENT SEARCH
    // ============================================

    const searchInput = document.getElementById("eventSearch");

    // Only run this code on the events page.
    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchValue = searchInput.value.toLowerCase();

            const eventCards = document.querySelectorAll(".event-item");

            let resultsFound = 0;

            // Check each event against the search.
            eventCards.forEach(function (card) {

                const eventName = card.textContent.toLowerCase();

                if (eventName.includes(searchValue)) {

                    card.style.display = "";

                    resultsFound++;

                } else {

                    card.style.display = "none";

                }

            });

            console.log("Events found:", resultsFound);

        });

    }


    // ============================================
    // 2. WEATHER API
    // ============================================

    const temperature = document.getElementById("temperature");

    // Only run this code on the weather page.
    if (temperature) {

        async function getWeather() {

            const description = document.getElementById("description");
            const feelsLike = document.getElementById("feelsLike");
            const humidity = document.getElementById("humidity");
            const windSpeed = document.getElementById("windSpeed");
            const errorMessage = document.getElementById("weatherError");

            try {

                // Request weather information from Flask.
                const response = await fetch("/api/weather-data");

                if (!response.ok) {
                    throw new Error("Unable to connect to weather API.");
                }

                // Convert API response into JavaScript data.
                const data = await response.json();

                const current = data.current;

                // Display the weather information.
                temperature.textContent =
                    current.temperature_2m + "°F";

                feelsLike.textContent =
                    current.apparent_temperature + "°F";

                humidity.textContent =
                    current.relative_humidity_2m + "%";

                windSpeed.textContent =
                    current.wind_speed_10m + " mph";

                // Convert weather codes into descriptions.
                const weatherDescriptions = {
                    0: "Clear Sky",
                    1: "Mainly Clear",
                    2: "Partly Cloudy",
                    3: "Overcast",
                    45: "Foggy",
                    48: "Depositing Rime Fog",
                    51: "Light Drizzle",
                    53: "Moderate Drizzle",
                    55: "Heavy Drizzle",
                    61: "Light Rain",
                    63: "Moderate Rain",
                    65: "Heavy Rain",
                    71: "Light Snow",
                    73: "Moderate Snow",
                    75: "Heavy Snow",
                    80: "Rain Showers",
                    81: "Moderate Rain Showers",
                    82: "Heavy Rain Showers",
                    95: "Thunderstorm",
                    96: "Thunderstorm with Hail",
                    99: "Severe Thunderstorm"
                };

                description.textContent =
                    weatherDescriptions[current.weather_code] ||
                    "Weather conditions unavailable";

                console.log("Weather information loaded:", data);

            } catch (error) {

                console.error("Weather API error:", error);

                temperature.textContent = "--";

                description.textContent =
                    "Weather information unavailable.";

                errorMessage.textContent =
                    "Could not load weather. Please try again later.";

            }

        }

        // Load weather information when the page opens.
        getWeather();

    }

});