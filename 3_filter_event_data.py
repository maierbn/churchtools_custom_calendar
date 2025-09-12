import json

def filter_event_fields(event: dict) -> dict:
    """Keep only the fields actually used by the frontend."""
    return {
        "base": {
            "id": event.get("base", {}).get("id"),
            "caption": event.get("base", {}).get("caption"),
            "note": event.get("base", {}).get("note"),
            "information": event.get("base", {}).get("information"),
            "link": event.get("base", {}).get("link"),
            "address": {
                "meetingAt": event.get("base", {}).get("address", {}).get("meetingAt")
            } if event.get("base", {}).get("address") else None,
            "image": {
                "fileUrl": event.get("base", {}).get("image", {}).get("fileUrl")
            } if event.get("base", {}).get("image") else None,
            "calendar": {
                "name": event.get("base", {}).get("calendar", {}).get("name")
            } if event.get("base", {}).get("calendar") else None,
        },
        "calculated": {
            "startDate": event.get("calculated", {}).get("startDate"),
            "endDate": event.get("calculated", {}).get("endDate"),
        }
    }

# Load input
with open('events_2_sorted.json', 'r') as f:
    sorted_data = json.load(f)

# Keep only used fields
filtered_data = [filter_event_fields(e) for e in sorted_data["data"]]

print(f"[3_filter_event_data.py] Filtered {len(filtered_data)} events")

# Save the expanded events back to a JSON file
with open('events.json', 'w') as f:
    json.dump({"data": filtered_data}, f, indent=4)
