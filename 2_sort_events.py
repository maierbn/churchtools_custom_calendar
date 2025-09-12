import json
import dateutil.parser
import dateutil.tz

def make_timezone_aware(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=dateutil.tz.UTC)
    return dt

def sort_events(events):
    
    # Sort events by their startDate
    return sorted(events, key=lambda x: make_timezone_aware(dateutil.parser.parse(x["calculated"]["startDate"])))

# Load input
with open('events_1_expanded.json', 'r') as f:
    expanded_data = json.load(f)

# Sort the events by date
sorted_data = sort_events(expanded_data)

print(f"[2_sort_events.py] Sorted {len(sorted_data)} events")

# Save the expanded events back to a JSON file
with open('events_2_sorted.json', 'w') as f:
    json.dump({"data": sorted_data}, f, indent=4)
