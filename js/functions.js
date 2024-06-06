
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


function createICSFile(startDate, endDate, summary, description, location) {
    const start = new Date(startDate).toISOString().replace(/-|:|\.\d+/g, '');
    const end = new Date(endDate).toISOString().replace(/-|:|\.\d+/g, '');

    const icsContent = `
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Your Organization//Your Product//EN
    BEGIN:VEVENT
    UID:${new Date().getTime()}@yourdomain.com
    DTSTAMP:${new Date().toISOString().replace(/-|:|\.\d+/g, '')}
    DTSTART:${start}
    DTEND:${end}
    SUMMARY:${summary}
    DESCRIPTION:${description}
    LOCATION:${location}
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