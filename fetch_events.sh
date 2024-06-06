
current_date=$(date +%Y-%m-%d)
one_year_from_now=$(date -d "+1 year" +%Y-%m-%d)

# fetch events from churchtools and store in "events.json"
wget -O events.json "https://elkw2808.krz.tools/api/calendars/31/appointments?from=${current_date}&to=${one_year_from_now}"
