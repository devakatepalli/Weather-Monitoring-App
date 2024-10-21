import pandas as pd


# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    print("Processing weather data:", weather_data)  # Debugging line
    daily_summaries = {}
    for city, data in weather_data.items():
        if 'main' in data:
            temp = kelvin_to_celsius(data['main']['temp'])
            summary = {
                'temperature': temp,
                'condition': data['weather'][0]['main'],
                'feels_like': kelvin_to_celsius(data['main']['feels_like']),
                'humidity': data['main']['humidity']
            }
            # Calculate additional metrics for daily summary
            daily_summaries[city] = {
                'average_temp': temp,  # Replace with actual average calculation if you have multiple entries
                'max_temp': temp,      # Update based on data
                'min_temp': temp,      # Update based on data
                'dominant_condition': data['weather'][0]['main']  # Assuming it's the dominant condition
            }
        else:
            print(f"No weather data for {city}")
    return daily_summaries




