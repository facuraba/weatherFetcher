import json
import requests

def lambda_handler(event, context):
    # OpenWeather API key
    api_key = "a916d026ef85bc431e78689ec58ab200"
    # Extract location from the event
    location = event.get("queryStringParameters", {}).get("location", "London")
    
    # OpenWeather API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    # Fetch weather data
    response = requests.get(url)
    weather_data = response.json()
    
    # Convert temperature from Kelvin to Celsius
    if 'main' in weather_data:
        kelvin_temp = weather_data['main']['temp']
        celsius_temp = kelvin_temp - 273.15
        weather_data['main']['temp'] = round(celsius_temp, 2)  # Rounded to 2 decimal places

    # Return weather data with CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': json.dumps(weather_data)
    }
