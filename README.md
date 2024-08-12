# SkyCompass <img src="images/skycompass_logo.png" alt="Logo" width="35" height="35">
A simple mobile weather app using Python with the Kivy framework and the OpenWeatherMap API.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Image Gallery](#image-gallery)
- [Mobile](#mobile)
- [Tests](#tests)
- [Credits](#credits)
- [License](#license)


## Installation
1. Clone the repository:
```bash
 git clone https://github.com/DelgadoDevT/skycompass.git
```

2. Create a virtual environment:
```bash
python -m venv kivy_venv
 ```

3. Activate the virtual environment:
```bash
# Windows:
kivy_venv\Scripts\activate

# Linux or MacOS
source kivy_venv/bin/activate
```

4. Install Kivy:
```bash
python -m pip install "kivy[base]" kivy_examples
```

## Usage
To run the project, navigate to the main folder and use the following command:
```bash
python main.py
```

## Features
The program allows users to input a location into a search bar. It fetches weather data from the OpenWeatherMap API, retrieving information for the next five days.

The program processes this data, extracting the necessary details and organising them into a dictionary. It then displays key information such as maximum and minimum temperatures, weather overview, and wind speed. The wind speed is measured in metres per second (m/s) and is classified as "Light", "Moderate", or "Strong" based on a simplified version of the Beaufort wind scale. To provide a comprehensive view, the program calculates the average weather details since the data is provided in three-hour intervals throughout each day.

The interface features five buttons, each corresponding to one of the five days. Clicking a button updates the main layout to show a weather symbol and other relevant weather information for the selected day.

On mobile devices, the application includes a loading screen. The program also manages common errors, such as when a location is not found or if there is an issue with fetching data from the API.

## Image Gallery

Below are some screenshots of the project as seen on an Android mobile device:

<div>
    <img src="/screenshots/loading_screen.jpg" alt="Loading Screen" width="250" style="display:inline-block; margin-right:10px;">
    <img src="/screenshots/empty_screen.jpg" alt="Empty Screen" width="250" style="display:inline-block; margin-right:10px;">
    <img src="/screenshots/weather_screen.jpg" alt="Weather Screen" width="250" style="display:inline-block;">
</div>

## Mobile
To create an APK (Android) or IPA (iOS), follow the steps for installation and running of [Buildozer](https://buildozer.readthedocs.io/en/latest/).

Note that you do not need to run `buildozer init` as a `buildozer.spec` file is already provided and pre-configured for the project. You can proceed directly with building your application using the provided configuration.

## Tests
This project includes unit tests developed with the Pytest framework:
1. Install pytest:
```bash
pip install pytest
```

2. Run the tests:
```bash
pytest 
```

## Credits

This project uses data from the [OpenWeatherMap API](https://openweathermap.org/). I appreciate their service for providing accurate and reliable weather data.

Special thanks to [Kivy](https://kivy.org/) for the framework used to build this application.

I also acknowledge [Buildozer](https://buildozer.readthedocs.io/en/latest/) for its role in packaging the app for Android and iOS.

My testing process was made easier with [Pytest](https://docs.pytest.org/en/stable/), a framework that provides powerful testing features.

## License
This project is licensed under the [MIT License](LICENSE).

