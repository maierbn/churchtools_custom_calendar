
current_date=$(date +%Y-%m-%d)
one_year_from_now=$(date -d "+1 year" +%Y-%m-%d)

echo "Starting at $current_date" | tee log.txt

if true; then

    # login
    churchtools_url="https://elkw2808.krz.tools"
    cookie_file="cookies.txt"

    # login to churchtools
    # response=$(curl -s -X POST "$churchtools_url/api/login" \
    #   -H "Content-Type: application/json" \
    #   -d "{\"username\": \"$CHURCHTOOLS_USERNAME\", \"password\": \"$CHURCHTOOLS_PASSWORD\"}" \
    #   -c "$cookie_file")
    # 
    # echo "Login response: $response" | tee -a log.txt

    # # query the available calendars
    # 
    # # Making the POST request using curl
    # response=$(curl -s -X POST -b "$cookie_file" -d "$data" "$url")
    
    echo "Fetching calendar categories ..." | tee -a log.txt
    echo "url=[$url]" | tee -a log.txt
    echo "data=[$data]" | tee -a log.txt

    response=$(curl 'https://elkw2808.krz.tools/index.php?q=churchcal/ajax' \
    --compressed \
    -X POST \
    -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'Accept-Language: en-US,en;q=0.5' \
    -H 'Accept-Encoding: gzip, deflate, br, zstd' \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
    -H 'CSRF-Token: null' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'Origin: https://elkw2808.krz.tools' \
    -H 'DNT: 1' \
    -H 'Connection: keep-alive' \
    -H 'Referer: https://elkw2808.krz.tools/?q=churchcal' \
    -H 'Cookie: language=de' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'TE: trailers' \
    --data-raw 'func=getMasterData')

    echo "response=[$response]" | tee -a log.txt

    # Extracting the list of integers using jq
    calendar_categories=$(echo "$response" | jq -r '.data.category | keys[] | tonumber')

    echo "Fetched calendar categories: $calendar_categories" | tee -a log.txt
fi 

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

#calendar_categories="31 49 52 55 58 60 67 76 80"
#echo "Using pre-defined calendar categories: $calendar_categories" | tee -a log.txt

# Initialize the events.json file
echo "{\"data\": []}" > events_raw.json

# Iterate over each integer and fetch the JSON results
for category_id in $calendar_categories; do
    api_url="https://elkw2808.krz.tools/api/calendars/$category_id/appointments?from=${current_date}&to=${one_year_from_now}"

    # Save the fetched JSON response to a temporary file
    temp_file="appointment_$category_id.json"
    curl -s "$api_url" \
        -H "Authorization: Bearer $token" \
        -o "$temp_file"
    
    # Call the Python script to append the JSON data to events.json
    python3 append_json.py "$temp_file" "events_raw.json" | tee -a log.txt
    
    # Remove the temporary file
    rm "$temp_file"
done

python3 1_resolve_repeating_events.py | tee -a log.txt
python3 2_sort_events.py | tee -a log.txt
python3 3_filter_event_data.py | tee -a log.txt

echo "finished downloading events at ${current_date}" | tee -a log.txt
ls -l | tee -a log.txt


