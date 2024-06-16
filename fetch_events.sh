
current_date=$(date +%Y-%m-%d)
one_year_from_now=$(date -d "+1 year" +%Y-%m-%d)

# query the available calendars
url="https://elkw2808.krz.tools/index.php?q=churchcal%2Fajax"
data="func=getMasterData"

# Making the POST request using curl
response=$(curl -s -X POST -d "$data" "$url")

# Extracting the list of integers using jq
calendar_categories=$(echo "$response" | jq -r '.data.category | keys[] | tonumber')

# Initialize the events.json file
echo "[]" > events.json

# Iterate over each integer and fetch the JSON results
for category_id in $calendar_categories; do
    api_url="https://elkw2808.krz.tools/api/calendars/$category_id/appointments?from=${current_date}&to=${one_year_from_now}"
    appointment_response=$(curl -s "$api_url")
    
    # Append the fetched JSON to the events.json file
    jq ". += [$appointment_response]" events.json > temp.json && mv temp.json events.json
done

# available calendars: 31, 49, 52, 55, 58, 60, 67, 73, 76

echo "finished downloading events at ${current_date}" > msg.html
ls -l >> msg.html


