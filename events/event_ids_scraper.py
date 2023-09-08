import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the Microsoft documentation page
url = "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all event ID sections
    event_id_sections = soup.find_all("h2", {"id": lambda x: x and x.startswith("event-id-")})

    # Initialize a dictionary to store event IDs and their meanings
    event_id_meanings = {}

    # Iterate through event ID sections and extract meanings
    for section in event_id_sections:
        event_id = section.get("id").replace("event-id-", "")
        content_div = section.find_next("div", class_="content")
        
        # Find the first <p> element in the content
        meaning_paragraph = content_div.find("p")

        # Extract the text and remove unnecessary prefixes
        meaning = meaning_paragraph.get_text(strip=True)

        # Remove "Message:" or "Symbolic name:" if present
        meaning = meaning.replace("Message: ", "").replace("Symbolic name:", "")

        # Replace underscores with spaces and capitalize the first letter
        meaning = meaning.replace("_", " ").capitalize()

        event_id_meanings[event_id] = meaning

    # Convert the dictionary to JSON
    result_json = json.dumps(event_id_meanings, indent=4)

    # Save the JSON to a file
    with open("windows_defender_event_ids.json", "w", encoding="utf-8") as json_file:
        json_file.write(result_json)

    print("Event IDs and meanings scraped and saved to 'windows_defender_event_ids.json'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
