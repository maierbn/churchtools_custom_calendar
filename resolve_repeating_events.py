import json
from datetime import datetime, timedelta
import dateutil.parser

def expand_events(events):
    # Initialize an empty list to store expanded events
    expanded_events = []

    for event in events:
        # Extract base information about the event
        base = event["base"]
        appointment = event["appointment"]["base"]

        # Add the original event to the expanded list
        expanded_events.append(event)

        # Check if the event has a repeat frequency and end date
        if appointment["repeatId"] != 0 and appointment["repeatUntil"] is not None:
            repeat_frequency = appointment["repeatFrequency"]
            repeat_until = dateutil.parser.parse(appointment["repeatUntil"])
            start_date = dateutil.parser.parse(appointment["startDate"])
            end_date = dateutil.parser.parse(appointment["endDate"])

            print(f"[resolve_repeating_events.py] Event {base['title']} in recurring.")
            print(f"[resolve_repeating_events.py] {repeat_frequency=} {repeat_until=} {start_date=} {end_date=}")

            # Extract exceptions if any
            exceptions = set()
            for exception in appointment["exceptions"]:
                exceptions.add(dateutil.parser.parse(exception["date"]).date())

            # Calculate and add each occurrence of the repeating event
            while start_date <= repeat_until:
                start_date += timedelta(days=repeat_frequency * 7)
                end_date += timedelta(days=repeat_frequency * 7)

                if start_date.date() not in exceptions:
                    # Create a new event occurrence based on the original
                    new_event = {
                        "appointment": {
                            "base": appointment.copy(),
                            "calculated": {
                                "startDate": start_date.isoformat(),
                                "endDate": end_date.isoformat()
                            }
                        },
                        "base": base.copy(),
                        "calculated": {
                            "startDate": start_date.isoformat(),
                            "endDate": end_date.isoformat()
                        }
                    }
                    # Update startDate and endDate for the new occurrence
                    new_event["appointment"]["base"]["startDate"] = start_date.isoformat()
                    new_event["appointment"]["base"]["endDate"] = end_date.isoformat()

                    expanded_events.append(new_event)

    return expanded_events

def sort_events(events):
    print(f"[resolve_repeating_events.py] Sort {len(events)} events")
    
    # Sort events by their startDate
    return sorted(events, key=lambda x: dateutil.parser.parse(x["calculated"]["startDate"]))

# Load the JSON data from the file
with open('events_raw.json', 'r') as f:
    data = json.load(f)

# Expand the events
expanded_data = expand_events(data["data"])

# Sort the events by date
sorted_data = sort_events(expanded_data)

# Save the expanded events back to a JSON file
with open('events.json', 'w') as f:
    json.dump({"data": expanded_data}, f, indent=4)
