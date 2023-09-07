from main import colors

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
