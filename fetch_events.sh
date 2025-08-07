
current_date=$(date +%Y-%m-%d)
one_year_from_now=$(date -d "+1 year" +%Y-%m-%d)

echo "Starting at $current_date" > log.txt

# query the available calendars
url="https://elkw2808.krz.tools/index.php?q=churchcal%2Fajax"
data="func=getMasterData"

# Making the POST request using curl
response=$(curl -s -X POST -d "$data" "$url")

# Extracting the list of integers using jq
calendar_categories=$(echo "$response" | jq -r '.data.category | keys[] | tonumber')

echo "Fetched calendar categories: $calendar_categories" >> log.txt

# Initialize the events.json file
echo "{\"data\": []}" > events_raw.json

# Iterate over each integer and fetch the JSON results
for category_id in $calendar_categories; do
    api_url="https://elkw2808.krz.tools/api/calendars/$category_id/appointments?from=${current_date}&to=${one_year_from_now}"

    # Save the fetched JSON response to a temporary file
    temp_file="appointment_$category_id.json"
    curl -s "$api_url" -o "$temp_file"
    
    # Call the Python script to append the JSON data to events.json
    python3 append_json.py "$temp_file" "events_raw.json" >> log.txt
    
    # Remove the temporary file
    #rm "$temp_file"
done

python3 resolve_repeating_events.py >> log.txt

# available calendars: 31, 49, 52, 55, 58, 60, 67, 73, 76
# 31 Gottesdienst
# 46 Kirchenjahr 2023/24
# 49 Kinder
# 52 Jugend
# 55 Erwachsene
# 58 Familie
# 67 Westerfeld Café
# 73 Ferien BaWü
# 76 Kirchenjahr 2024/25

echo "finished downloading events at ${current_date}" >> log.txt
ls -l >> log.txt


