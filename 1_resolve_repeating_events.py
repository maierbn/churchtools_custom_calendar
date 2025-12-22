import json
from datetime import datetime, timedelta
import dateutil.parser
import dateutil.tz

def make_timezone_aware(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=dateutil.tz.UTC)
    return dt

def expand_events(events):
    # Initialize an empty list to store expanded events
    expanded_events = []

    # Define date boundaries
    now = datetime.now(dateutil.tz.UTC)
    one_year_later = now + timedelta(days=365)

    for event in events:
        # Extract base information about the event
        base = event["base"]
        appointment = event["appointment"]["base"]

        # Parse start/end
        start_date = make_timezone_aware(dateutil.parser.parse(event["calculated"]["startDate"]))
        end_date = make_timezone_aware(dateutil.parser.parse(event["calculated"]["endDate"]))

        # Skip events outside allowed window
        if not (now <= start_date <= one_year_later):
            continue

        # Add the original event if in range
        expanded_events.append(event)

        # Handle repeating events
        if appointment.get("repeatId", 0) != 0 and appointment.get("repeatUntil") is not None:
            repeat_frequency = appointment["repeatFrequency"]
            repeat_until = make_timezone_aware(dateutil.parser.parse(appointment["repeatUntil"]))
            repeat_until = min(repeat_until, one_year_later)  # clamp to +1 year

            # Exceptions
            exceptions = {
                dateutil.parser.parse(exc["date"]).date()
                for exc in appointment.get("exceptions", [])
            }

            while start_date <= repeat_until:
                start_date += timedelta(days=repeat_frequency * 7)
                end_date += timedelta(days=repeat_frequency * 7)

                if start_date.date() in exceptions:
                    continue

                if now <= start_date <= one_year_later:
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
                    # also update base start/end
                    new_event["appointment"]["base"]["startDate"] = start_date.isoformat()
                    new_event["appointment"]["base"]["endDate"] = end_date.isoformat()

                    expanded_events.append(new_event)

    return expanded_events

# Load input
with open('events_0_raw.json', 'r') as f:
    data = json.load(f)

# Expand + filter
expanded_data = expand_events(data["data"])

print(f"[1_resolve_repeating_events.py] Expanded {len(data["data"])} events to {len(expanded_data)} events")

# Save the expanded events back to a JSON  file
with open('events_1_expanded.json', 'w') as f:
    json.dump({"data": expanded_data}, f, indent=4)
