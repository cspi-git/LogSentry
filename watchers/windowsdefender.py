from main import colors
from parser import winevent as winevent_parser
import subprocess
import hashlib
import base64

ignore_list = [1151]
stored_events = []

async def Watch():
    # print(f"{colors.darkblue}Windows Defender watcher was started!{colors.reset}")
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
        
        base64_hash = hashlib.sha256(latest_event.encode("utf-8")).hexdigest()
        if base64_hash in stored_events:
            return None

        stored_events.append(base64_hash)

        event_id = latest_event.split("\n")[4].split(":")[1].strip()

        if int(event_id) in ignore_list:
            # exit()
            return "Retrieved event is in the ignore list."

        # return winevent_parser.Parser(latest_event).WindowsDefender()
        winevent_parser.Parser(latest_event).WindowsDefender()
        # print(latest_event)
        # exit()
        return latest_event

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        # exit()
        return None