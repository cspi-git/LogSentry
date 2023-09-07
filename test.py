import subprocess
from parser import winevent as winevent_parser

ignore_list = [1151]

def get_latest_defender_event():
    try:
        # Run the wevtutil command
        result = subprocess.run(
            ["wevtutil", "qe", "Microsoft-Windows-Windows Defender/Operational", "/c:1", "/rd:true", "/f:text"],
            capture_output=True,
            text=True,
            check=True
        )

        # Capture the standard output
        latest_event = result.stdout
        event_id = latest_event.split("\n")[4].split(":")[1].strip()

        if int(event_id) in ignore_list:
            return "Retrieved event is in the ignore list."

        return winevent_parser.Parser(latest_event).WindowsDefender()

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

# Example usage:
latest_event = get_latest_defender_event()
if latest_event is not None or latest_event != "Retrieved event is in the ignore list.":
    print("Latest Defender Event:")
    print(latest_event)
else:
    print("Failed to retrieve the latest Defender event.")
