"""
File: test_data_splitter.py
Author: DelgadoDevT
Date: 2024-08-11
Description: This script contains unit tests for the functions defined in data_splitter.py.
             It includes tests for get_days, get_temperatures, get_overview, and get_wind_speed.
             The tests validate the correct functioning of these functions with various inputs.
             The daily_weather used in these functions is a simplification of the daily_weather provided
             by the function process_data defined in weather.py.
License: MIT License
"""

import pytest
from datetime import datetime
from data_splitter import get_days, get_temperatures, get_overview, get_wind_speed


def test_get_days():
    """
    Tests if the get_days function returns a list of the corresponding days of the week using the date.
    Also checks error code handling.
    """
    daily_weather = [
        {"date": datetime(2024, 7, 29)},  # Mon
        {"date": datetime(2024, 7, 30)},  # Tues
        {"date": datetime(2024, 7, 31)},  # Wed
        {"date": datetime(2024, 8, 1)},  # Thurs
        {"date": datetime(2024, 8, 2)},  # Fri
    ]
    assert get_days(daily_weather) == ["Mon", "Tues", "Wed", "Thurs", "Fri"]

    assert get_days(404) == ["N/A"] * 5
    assert get_days(400) == ["N/A"] * 5
    assert get_days(409) == ["N/A"] * 5


def test_get_temperatures():
    """
    Tests if the get_temperatures function returns a list of the corresponding temperatures.
    Also checks error code handling.
    """
    daily_weather = [
        {"temperature_max": 20.5},
        {"temperature_max": 21.3},
        {"temperature_max": 19.8},
        {"temperature_max": 22.1},
        {"temperature_max": 23.7},
    ]
    assert get_temperatures(daily_weather, "max") == [
        "20.5º",
        "21.3º",
        "19.8º",
        "22.1º",
        "23.7º",
    ]

    daily_weather = [
        {"temperature_min": 15.2},
        {"temperature_min": 16.4},
        {"temperature_min": 14.8},
        {"temperature_min": 17.1},
        {"temperature_min": 18.0},
    ]
    assert get_temperatures(daily_weather, "min") == [
        "15.2º",
        "16.4º",
        "14.8º",
        "17.1º",
        "18.0º",
    ]

    assert get_temperatures(404, "max") == ["N/A"] * 5
    assert get_temperatures(400, "max") == ["N/A"] * 5
    assert get_temperatures(409, "max") == ["N/A"] * 5


def test_get_overview():
    """
    Tests if the get_overview function returns a list of the corresponding weather overviews.
    Also checks error code handling.
    """
    daily_weather = [
        {"overview": "Clear"},
        {"overview": "Clouds"},
        {"overview": "Rain"},
        {"overview": "Clear"},
        {"overview": "Clear"},
    ]
    assert get_overview(daily_weather) == ["Clear", "Clouds", "Rain", "Clear", "Clear"]

    assert get_overview(404) == ["N/A"] * 5
    assert get_overview(400) == ["N/A"] * 5
    assert get_overview(409) == ["N/A"] * 5


def test_get_wind_speed():
    """
    Tests if the get_wind_speed function returns a list of the corresponding wind speeds.
    Also checks error code handling.
    """
    daily_weather = [
        {"wind_speed": 5.5},
        {"wind_speed": 10.2},
        {"wind_speed": 7.3},
        {"wind_speed": 8.8},
        {"wind_speed": 12.4},
    ]
    assert get_wind_speed(daily_weather) == [5.5, 10.2, 7.3, 8.8, 12.4]

    assert get_wind_speed(404) == ["N/A"] * 5
    assert get_wind_speed(400) == ["N/A"] * 5
    assert get_wind_speed(409) == ["N/A"] * 5
