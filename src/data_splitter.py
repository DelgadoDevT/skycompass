"""
File: data_splitter.py
Author: DelgadoDevT
Date: 2024-08-11
Description: This script contains helper functions that process the output from process_data in weather.py
             and create lists with the selected weather elements.
License: MIT License
"""

from datetime import datetime

def get_days(daily_weather):
    """
    Process the data from daily_weather to make a list of abbreviated day names.
    Arguments: processed daily_weather
    Returns: List of five corresponding days of the week.
             Returns ["N/A"] * 5 for error codes (404, 400, 409).
    """
    if daily_weather in [404, 400, 409]:
        return ["N/A"] * 5

    days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    days_week = ["N/A"] * 5

    for weather in daily_weather:
        date = weather["date"]
        weekday_index = date.weekday()

        for i in range(5):
            if days_week[i] == "N/A":
                days_week[i] = days[weekday_index]
                break

    return days_week

def get_temperatures(daily_weather, temp_type):
    """
    Process the data from daily_weather to make a list of maximum or minimum temperatures.
    Arguments: processed daily_weather and the 'max' or 'min'
    Returns: List of five temperatures formatted as strings with one decimal place.
             Returns ["N/A"] * 5 for error codes (404, 400, 409).
    """
    if daily_weather in [404, 400, 409]:
        return ["N/A"] * 5

    temperatures = []

    for weather in daily_weather:
        if temp_type == "max":
            temp = weather["temperature_max"]
        elif temp_type == "min":
            temp = weather["temperature_min"]
        else:
            print("Invalid temperature type. Use 'max' or 'min'.")
            return ["N/A"] * 5

        temperatures.append(f"{temp:.1f}º")

    return temperatures

def get_overview(daily_weather):
    """
    Process the data from daily_weather to make a list of weather overviews for five days.
    Arguments: processed daily_weather
    Returns: List of five weather overviews.
             Returns ["N/A"] * 5 for error codes (404, 400, 409).
    """
    if daily_weather in [404, 400, 409]:
        return ["N/A"] * 5

    overview = []

    for weather in daily_weather:
        overview.append(weather["overview"])

    return overview

def get_wind_speed(daily_weather):
    """
    Process the data from daily_weather to make a list of wind speeds for five days.
    Arguments: processed daily_weather
    Returns: List of five wind speeds.
             Returns ["N/A"] * 5 for error codes (404, 400, 409).
    """
    if daily_weather in [404, 400, 409]:
        return ["N/A"] * 5

    wind_speed = []

    for weather in daily_weather:
        wind_speed.append(weather["wind_speed"])

    return wind_speed
