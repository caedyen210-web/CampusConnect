
// CampusConnect JavaScript

document.addEventListener("DOMContentLoaded", function () {
    console.log("CampusConnect JavaScript loaded!");

});
// ===================================
// CampusConnect JavaScript
// ===================================

// Wait until the HTML page has loaded
document.addEventListener("DOMContentLoaded", function () {

    console.log("CampusConnect JavaScript is running!");

    // ===================================
    // 1. EVENT SEARCH FUNCTIONALITY
    // ===================================

    const searchForm = document.getElementById("searchForm");

    if (searchForm) {

        searchForm.addEventListener("submit", function (event) {

            // Prevent the page from refreshing
            event.preventDefault();

            // Get the student's search input
            const searchInput = document.getElementById("eventSearch");

            const searchValue = searchInput.value.toLowerCase();

            // Get all event cards
            const events = document.querySelectorAll(".event-item");

            let resultsFound = 0;

            // Loop through events and filter them
            events.forEach(function (item) {

                const eventName = item.textContent.toLowerCase();

                if (eventName.includes(searchValue)) {

                    item.style.display = "block";
                    resultsFound++;

                } else {

                    item.style.display = "none";

                }

            });

            // Display search results
            const message = document.getElementById("searchMessage");

            if (resultsFound > 0) {
                message.textContent = resultsFound + " event(s) found.";
            } else {
                message.textContent = "No events found.";
            }

        });

    }


    // ===================================
    // 2. API INTEGRATION
    // ===================================

    const apiButton = document.getElementById("apiButton");

    if (apiButton) {

        apiButton.addEventListener("click", async function () {

            const result = document.getElementById("apiResult");

            result.textContent = "Connecting to API...";

            try {

                // Replace this placeholder with your actual API endpoint
                const API_URL = "/api/your-endpoint";

                const response = await fetch(API_URL);

                // Check whether the request worked
                if (!response.ok) {
                    throw new Error("API request failed");
                }

                // Convert response into JSON
                const data = await response.json();

                // Display API information
                result.textContent = JSON.stringify(data);

            } catch (error) {

                // Display an error if the API is unavailable
                console.error("API Error:", error);

                result.textContent =
                    "API connection is not configured yet.";

            }

        });

    }

});