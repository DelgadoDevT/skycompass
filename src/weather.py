"""
File: weather.py
Author: DelgadoDevT
Date: 2024-07-29
Description: This script fetches weather data from the OpenWeatherMap API, processes it, 
             and provides daily weather summaries including temperature, wind speed, and overview.
License: MIT License
"""

from config import api_key
import requests
from datetime import datetime


def api_fetch(location):
    """
    Fetches weather data for a location using OpenWeatherMap API
    Returns the raw response from the API request
    """

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={api_key}"
    weather_raw = requests.get(url)

    return weather_raw


def wind_class(wind_speed):
    """
    Classifies wind speed in m/s as “Light”, “Moderate” or “Strong” based on a simplification of the Beaufort wind scale.
    Arguments: winds speed in meters per second
    Returns the winds speed category
    """
    if wind_speed <= 5:
        return "Light"
    elif wind_speed <= 10:
        return "Moderate"
    return "Strong"


def common_overview(day_overview):
    """
    Finds the most common weather overview for a day
    Arguments: List of weather descriptions
    Retuns: Most common weather description
    """
    overview_counter = {}

    for overview in day_overview:
        if overview in overview_counter:
            overview_counter[overview] += 1
        else:
            overview_counter[overview] = 1

    avg_overview = None
    max_count = 0

    for overview, count in overview_counter.items():
        if count > max_count:
            max_count = count
            avg_overview = overview

    return avg_overview


def process_data(location):
    """
    Main function for obtaining, processing and organizing selected meteorological data
    Returns a list of dictionaries with selected weather data over five/six days
    """
    weather_raw = api_fetch(location)

    if weather_raw.status_code == 200:
        weather_json = weather_raw.json()

        day_temperature = {}
        day_wind = {}
        day_overview = {}

        for data in weather_json["list"]:
            dt = datetime.fromtimestamp(data["dt"])
            date = dt.date()
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            wind_speed = data["wind"]["speed"]
            overview = data["weather"][0]["main"]

            if date not in day_temperature:
                day_temperature[date] = {
                    "temperature_min": temp_min,
                    "temperature_max": temp_max,
                }
                day_wind[date] = [wind_speed]
                day_overview[date] = [overview]
            else:
                day_temperature[date]["temperature_min"] = min(
                    day_temperature[date]["temperature_min"], temp_min
                )
                day_temperature[date]["temperature_max"] = max(
                    day_temperature[date]["temperature_max"], temp_max
                )
                day_wind[date].append(wind_speed)
                day_overview[date].append(overview)

        daily_weather = []
        for date in sorted(day_temperature.keys()):
            avg_wind = wind_class(sum(day_wind[date]) / len(day_wind[date]))
            avg_overview = common_overview(day_overview[date])

            daily_weather.append(
                {
                    "date": date,
                    "overview": avg_overview,
                    "temperature_max": day_temperature[date]["temperature_max"],
                    "temperature_min": day_temperature[date]["temperature_min"],
                    "wind_speed": avg_wind,
                }
            )

        print("The data was fetched and processed without errors (200 - OK)")
        return daily_weather

    elif weather_raw.status_code == 404:
        print("This location does not exist (404 - Not Found)")
        return 404
    else:
        print("Error on fetching data from API (400 - Bad Request)")
        return 400
