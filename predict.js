function showSelected(spanId, value) {
    document.getElementById(spanId).innerText = value;
}
async function senddata()
{
    const data = {
    Weather: document.getElementById('weather').innerText,
    Season: document.getElementById('season').innerText,
    DayOfWeek: document.getElementById('day-of-week').innerText,
    Promotion: document.getElementById('special-promotion').innerText,
    TimeSlot: document.getElementById('time').innerText,
    SpecialEvent: document.getElementById('special-event').innerText
    }
    try
    {
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    const result = await response.json()
    document.getElementById('result').innerText = `Prediction: ${result.Prediction}`;
    } 
    catch (error) 
    {
        console.error('Error:', error); // Handle errors
    }
};

