function getParamsFromURL(queryString) {

    if (queryString.indexOf("?") == -1)
    {
        return {};
    }
    // Remove the leading question mark (?)
    var queryStringWithoutQuestionMark = queryString.split('.html?')[1];

    // Split the query string into an array of key-value pairs
    const keyValuePairs = queryStringWithoutQuestionMark.split('&');

    // Initialize an object to store the parameters
    const params = {};

    // Iterate over the key-value pairs array
    keyValuePairs.forEach(pair => {
        // Split each pair into key and value
        const [key, value] = pair.split('=');

        // Decode URI components to handle special characters
        const decodedKey = decodeURIComponent(key);
        const decodedValue = decodeURIComponent(value);

        // Add the key-value pair to the params object
        params[decodedKey] = decodedValue;
    });

    return params;
}

function formatDates(startDate, endDate) {
    // Create Date objects
    const start = new Date(startDate);
    const end = new Date(endDate);

    // Define options for date and time formatting
    const optionsDate = { weekday: 'short', day: 'numeric', month: 'long', year: 'numeric' };
    const optionsTime = { hour: '2-digit', minute: '2-digit' };

    // Format the date part
    const formattedDate = new Intl.DateTimeFormat('de-DE', optionsDate).format(start);
    // Format the time parts
    const formattedStartTime = new Intl.DateTimeFormat('de-DE', optionsTime).format(start);
    const formattedEndTime = new Intl.DateTimeFormat('de-DE', optionsTime).format(end);

    // Combine the formatted parts
    const formattedString = `${formattedDate}, ${formattedStartTime} - ${formattedEndTime}`;

    return formattedString;
}

function escapeICSField(text) {
    return text.replace(/\\/g, '\\\\')  // Escape backslashes first
               .replace(/,/g, '\\,')     // Escape commas
               .replace(/;/g, '\\;')     // Escape semicolons
               .replace(/\n/g, '\\n');   // Escape newlines
}

function createICSFile(startDate, endDate, summary, description, location) {
    const start = new Date(startDate).toISOString().replace(/-|:|\.\d+/g, '');
    const end = new Date(endDate).toISOString().replace(/-|:|\.\d+/g, '');

    // Escape special characters for ICS fields
    const escapedSummary = escapeICSField(summary);
    const escapedDescription = escapeICSField(description);
    const escapedLocation = escapeICSField(location);

    const icsContent = `
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Evang Kirchengemeinde Malmsheim//Gottesdienste//EN
BEGIN:VEVENT
UID:${new Date().getTime()}@malmsheim-evangelisch.de
DTSTAMP:${new Date().toISOString().replace(/-|:|\.\d+/g, '')}
DTSTART:${start}
DTEND:${end}
SUMMARY:${escapedSummary}
DESCRIPTION:${escapedDescription}
LOCATION:${escapedLocation}
END:VEVENT
END:VCALENDAR
    `.trim();

    const blob = new Blob([icsContent], { type: 'text/calendar' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'event.ics';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
