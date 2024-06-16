
current_date=$(date +%Y-%m-%d)
one_year_from_now=$(date -d "+1 year" +%Y-%m-%d)

# query the available calendars
url="https://elkw2808.krz.tools/index.php?q=churchcal%2Fajax"
data="func=getMasterData"

# Making the POST request using curl
response=$(curl -s -X POST -d "$data" "$url")

# Printing the response
echo "Response from server:"
echo "$response"

# fetch events from churchtools and store in "events.json"
wget -O events.json "https://elkw2808.krz.tools/api/calendars/31/appointments?from=${current_date}&to=${one_year_from_now}"

# available calendars: 31, 49, 52, 55, 58, 60, 67, 73, 76

echo "finished downloading events at ${current_date}" > msg.html
ls -l >> msg.html


