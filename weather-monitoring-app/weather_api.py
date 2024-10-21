import requests
import json
from config import CITIES, API_KEY

# Function to fetch weather data for a single city
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None

# Function to fetch weather data for all cities in CITIES
def get_weather_for_all_cities():
    weather_data = {}
    for city in CITIES:
        weather_data[city] = get_weather(city)
        print(f"Weather data for {city}:", weather_data[city])  # Debugging line
    return weather_data



# Helper function to convert Kelvin to Celsius
def kelvin_to_celsius(temp):
    return temp - 273.15

# Function to parse raw weather data into a simplified structure
def parse_weather_data(data):
    print(f"Parsing data: {data}")  # Debugging line
    return {
        'main': data['weather'][0]['main'],
        'temp': kelvin_to_celsius(data['main']['temp']),
        'feels_like': kelvin_to_celsius(data['main']['feels_like']),
        'dt': data['dt']
    }

