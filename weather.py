import requests
from datetime import datetime, timezone
import pandas as pd
import numpy as np
import sys

# Define your OpenWeatherMap API key
API_KEY = ""

# Check if API key is provided
if not API_KEY:
    print("API key is not found. Please provide a valid API key.")
    sys.exit(1)

# Initialize a list to store city data
cities_data = []

# Read city names from CSV file
city_df = pd.read_csv('in_cities.csv')

# Function to fetch city data
def fetch_city_data(city_name):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data['name'],
            "lat": data['coord']['lat'],
            "lon": data['coord']['lon']
        }
    else:
        print(f"Failed to fetch data for {city_name}")
        return None

# Iterate over each city in the DataFrame and fetch data
for city in city_df['City']:
    city_info = fetch_city_data(city)
    if city_info:
        cities_data.append(city_info)

# Print the collected city data
print(cities_data)
print()

# Function to fetch forecast data for a city
def fetch_forecast_data(city):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        forecasts = []
        for forecast_data in data['list']:
            forecast = {
                'city': city['name'],
                'timestamp': forecast_data['dt'],
                'date_time': datetime.fromtimestamp(forecast_data['dt'], timezone.utc).strftime('%d-%m-%Y %H:%M:%S'),
                'weather_main': forecast_data['weather'][0]['main'],
                'weather_description': forecast_data['weather'][0]['description'],
                'temperature_celsius': forecast_data['main']['temp'],
                'feels_like_celsius': forecast_data['main']['feels_like'],
                'temp_min_celsius': forecast_data['main']['temp_min'],
                'temp_max_celsius': forecast_data['main']['temp_max'],
                'pressure': forecast_data['main']['pressure'],
                'humidity': forecast_data['main']['humidity'],
                'wind_speed': forecast_data['wind']['speed'],
                'wind_deg': forecast_data['wind']['deg'],
                'clouds': forecast_data['clouds']['all'],
                'lat': city['lat'],
                'lon': city['lon']
            }
            forecasts.append(forecast)
        return forecasts
    else:
        print(f"Failed to fetch data for {city['name']}")
        return []

# Collect forecasts for all cities
all_forecasts = []
for city in cities_data:
    city_forecasts = fetch_forecast_data(city)
    all_forecasts.extend(city_forecasts)

# Convert data to DataFrame
df = pd.DataFrame(all_forecasts)

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Save the DataFrame to a CSV file
df.to_csv('Realtime_WeatherDate.csv', index=False)
print('The DataFrame are successfully saved to a CSV file')
