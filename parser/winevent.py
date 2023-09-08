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

    
class Parser:
    def __init__(self, event_record):
        self.event_record = event_record

    def WindowsDefender(self):
        event_info = {}
        lines = self.event_record.split("\n")[1:]  # Exclude the first line (Event[0])
        description = []

        for line in lines:
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                event_info[key] = value
            else:
                # If the line does not contain a colon, assume it's part of the description
                description.append(line.strip())

        # Combine multiline description
        event_info["Description"] = "\n".join(description)

        # Extract additional information from the Description field
        for line in event_info["Description"].split("\n"):
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                event_info[key] = value

        # Print the extracted information
        print("\n")
        print(f"{colors.blue}-" * 58)
        print("-" * 15 + " | Windows Defender Event | " + "-" * 15)
        print("-" * 58 + colors.reset)

        for key, value in event_info.items():
            print(f"{key}: {value}")

        return event_info

    def WindowsFirewall(self):
        event_info = {}
        lines = self.event_record.split("\n")[1:]
        description = []

        for line in lines:
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                event_info[key] = value
            else:
                # If the line does not contain a colon, assume it's part of the description
                description.append(line.strip())

        # Combine multiline description
        event_info["Description"] = "\n".join(description)

        # Extract additional information from the Description field
        for line in event_info["Description"].split("\n"):
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                event_info[key] = value

        # Print the extracted information
        print("\n")
        print(f"{colors.fire}-" * 58)
        print("-" * 15 + " | Windows Firewall Event | " + "-" * 15)
        print("-" * 58 + colors.reset)

        for key, value in event_info.items():
            print(f"{key}: {value}")

        return event_info