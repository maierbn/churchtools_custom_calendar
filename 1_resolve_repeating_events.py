import json

with open("events_0_raw.json", "r") as f:
    data = json.load(f)

print(f"[1_resolve_repeating_events.py] Keeping {len(data['data'])} API events")

with open("events_1_expanded.json", "w") as f:
    json.dump(data, f, indent=4)