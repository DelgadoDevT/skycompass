"""
File: test_weather.py
Author: João Delgado
Date: 2024-07-29
Description: This script contains unit tests for the functions defined in weather.py.
             It includes tests for api_fetch, wind_class, common_overview, and process_data.
             The tests validate the correct functioning of these functions with various inputs
             and check for correct handling of errors.
License: MIT License
"""

import pytest
from weather import wind_class, common_overview, api_fetch, process_data


def test_api_fetch():
    """
    Test the api_fetch function with a real API request.
    Ensure it returns a successful response.
    """
    location = "Amsterdam"
    response = api_fetch(location)

    assert (
        response.status_code == 200
    ), f"API request failed with status code: {response.status_code}"

    data = response.json()
    assert "list" in data, "'list' key not found in the API response"

    assert len(data["list"]) > 0


def test_wind_class():
    """
    Test the wind_class function to ensure it categorises wind speeds correctly.
    """
    assert wind_class(5) == "Light"
    assert wind_class(10) == "Moderate"
    assert wind_class(15) == "Strong"


def test_common_overview():
    """
    Test the common_overview function to ensure it finds the most common weather overview.
    """
    assert common_overview(["Clear", "Clear", "Clouds"]) == "Clear"
    assert common_overview(["Rain", "Rain", "Clouds", "Clouds", "Clouds"]) == "Clouds"
    assert common_overview(["Snow", "Snow", "Snow"]) == "Snow"


def test_process_data():
    """
    Test the process_data function for valid and invalid locations, checking the error codes.
    """
    valid_location = "Amsterdam"
    invalid_location = "hello"
    wrong_request_parameter = "###"

    valid_result = process_data(valid_location)
    invalid_result = process_data(invalid_location)
    wrong_request_result = process_data(wrong_request_parameter)

    assert isinstance(valid_result, list)
    assert invalid_result == 404
    assert wrong_request_result == 400
