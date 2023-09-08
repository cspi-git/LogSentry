from main import colors
from parser import winevent as winevent_parser
import subprocess
import hashlib
import base64
import time

ignore_list = [1151]
stored_events = []

def Watch():
    try:
        result = subprocess.run(
            ["wevtutil", "qe", "Microsoft-Windows-Windows Defender/Operational", "/c:1", "/rd:true", "/f:text"],
            capture_output=True,
            text=True,
            check=True
        )

        latest_event = result.stdout
        
        base64_hash = hashlib.sha256(latest_event.encode("utf-8")).hexdigest()
        if base64_hash in stored_events:
            return None

        stored_events.append(base64_hash)

        event_id = latest_event.split("\n")[4].split(":")[1].strip()

        if int(event_id) in ignore_list:
            return "Retrieved event is in the ignore list."

        winevent_parser.Parser(latest_event).WindowsDefender()
        return latest_event

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        with open("logs.txt", "w") as f:
            currenttime = time.strftime("%H:%M:%S")
            f.write(f"[{currenttime}] Error: {e}\n")

        # dont need to close bcos with open closes it automatically
        # f.close()

        return None