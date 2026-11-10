import sqlite3
import os
import requests

from flask import Blueprint, render_template
from utils.event_scraper import EventScraper

# Create the events blueprint
event_routes = Blueprint("event_routes", __name__)

# Your college events webpage
CALENDAR_URL = "https://www.adrian.edu/events/"


@event_routes.route("/events")
def events():

    # Create an EventScraper object
    scraper = EventScraper(CALENDAR_URL)

    try:
        # Collect events from the college website
        scraped_events = scraper.scrape_events()

        # Clean the event information
        cleaned_events = scraper.parse_event_data(scraped_events)

        # Save the events in the database
        scraper.save_events(cleaned_events)

    except requests.RequestException as error:
        print("Event scraping error:", error)

    # Connect to the database
    connection = sqlite3.connect("db/campusconnect.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Get internal events
    cursor.execute("SELECT * FROM internal_events")
    internal_events = cursor.fetchall()

    # Get external events
    cursor.execute("SELECT * FROM external_events")
    external_events = cursor.fetchall()

    connection.close()

    # Display both types of events
    return render_template(
        "events.html",
        internal_events=internal_events,
        external_events=external_events
    )