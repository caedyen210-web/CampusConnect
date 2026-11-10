import requests
import sqlite3
from bs4 import BeautifulSoup
import re


class EventScraper:

    # Constructor that accepts a campus events URL
    def __init__(self, calendar_url):
        self.calendar_url = calendar_url

    # Get the events webpage
    def scrape_events(self):
        response = requests.get(self.calendar_url, timeout=15)
        response.raise_for_status()

        # Parse the webpage HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find event information
        events = []

        # These selectors are examples and must be
        # adjusted to match your college's events webpage.
        for event in soup.select(".event"):
            name = event.select_one(".event-title")
            date = event.select_one(".event-date")
            time = event.select_one(".event-time")
            location = event.select_one(".event-location")
            description = event.select_one(".event-description")

            events.append({
                "event_name": name.get_text(strip=True) if name else "",
                "event_date": date.get_text(strip=True) if date else "",
                "event_time": time.get_text(strip=True) if time else "",
                "event_location": location.get_text(strip=True) if location else "",
                "description": description.get_text(strip=True) if description else ""
            })

        return events

    # Clean event information
    def parse_event_data(self, events):
        cleaned_events = []

        for event in events:
            # Remove extra spaces and unwanted characters
            event["event_name"] = re.sub(
                r"\s+", " ", event["event_name"]
            ).strip()

            event["event_location"] = re.sub(
                r"\s+", " ", event["event_location"]
            ).strip()

            if event["event_name"]:
                cleaned_events.append(event)

        return cleaned_events

    # Save events into the SQLite database
    def save_events(self, events):
        connection = sqlite3.connect("db/campusconnect.db")
        cursor = connection.cursor()

        for event in events:
            cursor.execute("""
                INSERT INTO external_events
                (event_name, event_date, event_time,
                 event_location, description)
                VALUES (?, ?, ?, ?, ?)
            """, (
                event["event_name"],
                event["event_date"],
                event["event_time"],
                event["event_location"],
                event["description"]
            ))

        connection.commit()
        connection.close()