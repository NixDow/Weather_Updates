import requests
import os
from dotenv import load_dotenv
import json
import pprint
from config import city, temp_high,temp_low, windy_speed

#open weather api configuration
load_dotenv()
api_key = os.getenv("openweather_api_key")
URL = "https://api.openweathermap.org/data/3.0/onecall?"
parameters = {"lat": city['lat'], "lon": city['lon'], "appid": api_key, "units": "metric"}

#get weather data using API
def get_weather(city):
    try:
        response = requests.get(URL, params=parameters)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    
#get average temperature for the day
def get_avg_temp(daily_temp):
    all_temp = []
    for key, value in daily_temp.items():
            all_temp.append(value)
    avg_temp = round(sum(all_temp) /len(all_temp), 2)
    return avg_temp

if __name__ == "__main__":
    weather_data = get_weather(city)
    pprint.pprint(weather_data['daily'][0]) #call trhe API for today's weather forecast

#weather suggestion logic
def message_gen(weather_data):
    main = weather_data['daily'][0]['weather'][0]['main']
    description = weather_data['daily'][0]['weather'][0]['description']
    temp = get_avg_temp(weather_data['daily'][0]['temp'])
    wind_speed = weather_data['daily'][0]['wind_speed']

    # Rain
    if "Rain" in main:
        if "moderate" in description:
            return f"Moderate rain today in {city['name']}, bring a waterproof jacket."
        return f"Heavy rain today in {city['name']}! Make sure to bring an umbrella."

    # Snow
    if "Snow" in main:
        return f" Snowfall expected in {city['name']}. Don't forget your boots, coat and gloves"
    
    # Hot
    if temp >= temp_high:
        return f" Very hot today in {city['name']} {temp}°C! Sunglasses and sunscreen recommended."

    # Cold
    if temp <= temp_low:
        return f"Cold weather today in {city['name']} {temp}°C! Wear a warm coat."

    # Windy
    if wind_speed > windy_speed:
        return f"Windy conditions in {city['name']}. Hold onto your hat!"

    return f"{main} today in {city['name']}. Have a great day!"

