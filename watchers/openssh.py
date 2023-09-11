from parser import winevent as winevent_parser
import subprocess
import hashlib
import base64
import time

ignore_list = []
stored_events = []

class colors:
    darkred = "\033[31m"
    red = "\033[91m"
    lightred = "\033[38;5;196m"
    darkgreen = "\033[32m"
    green = "\033[92m"
    lightgreen = "\033[38;5;46m"
    darkyellow = "\033[33m"
    yellow = "\033[93m"
    lightyellow = "\033[38;5;226m"
    darkblue = "\033[34m"
    blue = "\033[94m"
    lightblue = "\033[38;5;21m"
    reset = "\033[0m"
    fire = "\033[38;5;196m"

def Watch():
    try:
        result = subprocess.run(
            ["wevtutil", "qe", "OpenSSH/Operational", "/c:1", "/rd:true", "/f:text"],
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

        winevent_parser.Parser(latest_event).OpenSSH()
        return latest_event

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        with open("logs.txt", "w") as f:
            currenttime = time.strftime("%H:%M:%S")
            f.write(f"[{currenttime}] Error: {e}\n")

        # dont need to close bcos with open closes it automatically
        # f.close()

        return None