from datetime import datetime


def get_days(daily_weather):
    if daily_weather == 404 or daily_weather == 400 or daily_weather == 409:
        daily_weather = {}

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
    if daily_weather == 404 or daily_weather == 400 or daily_weather == 409:
        return ["N/A"] * 5

    temperatures = []

    for weather in daily_weather:
        if temp_type == "max":
            temp = weather["temperature_max"]
        elif temp_type == "min":
            temp = weather["temperature_min"]
        else:
            print("Invalid temperature type. Use 'max' or 'min'.")
            return

        temperatures.append(f"{temp:.1f}º")

    return temperatures


def get_overview(daily_weather):
    if daily_weather == 404 or daily_weather == 400 or daily_weather == 409:
        return ["N/A"] * 5

    overview = []

    for weather in daily_weather:
        overview.append(weather["overview"])

    return overview


def get_wind_speed(daily_weather):
    if daily_weather == 404 or daily_weather == 400 or daily_weather == 409:
        return ["N/A"] * 5

    wind_speed = []

    for weather in daily_weather:
        wind_speed.append(weather["wind_speed"])

    return wind_speed
