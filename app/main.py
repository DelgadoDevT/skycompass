from kivy.config import Config

Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_splitter import get_days, get_temperatures, get_overview, get_wind_speed
from weather import process_data
import webbrowser

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.label import Label


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)

        self.logo = Image(
            size_hint=(0.15, 0.15),
            pos_hint={"x": 0.03, "y": 0.85},
            source="../images/skycompass_logo.png",
        )
        self.add_widget(self.logo)

        gray = 211 / 255
        self.location_input = TextInput(
            size_hint=(0.6, 0.05),
            pos_hint={"x": 0.20, "y": 0.9},
            hint_text="Enter location",
            background_color=(gray, gray, gray, 1),
        )
        self.add_widget(self.location_input)

        deep_blue = 139 / 255
        self.search_button = Button(
            size_hint=(0.15, 0.05),
            pos_hint={"x": 0.8, "y": 0.9},
            background_color=(0.0, 0.0, deep_blue, 1),
            text="Search",
        )
        self.search_button.bind(on_press=self.button_click)
        self.add_widget(self.search_button)

        self.openweather_label = Label(
            text="Weather data provided by OpenWeather",
            pos_hint={"center_x": 0.4, "center_y": 0.03},
            size_hint=(None, None),
            font_size="16sp",
        )
        self.openweather_label.texture_update()
        self.openweather_label.size = self.openweather_label.texture_size
        self.openweather_label.bind(on_touch_down=self.hyperlink)
        self.add_widget(self.openweather_label)

        self.openweather_logo = Image(
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.9, "center_y": 0.03},
            source="../images/openweather_logo.png",
        )
        self.openweather_logo.texture_update()
        self.openweather_logo.size = self.openweather_logo.texture_size
        self.openweather_logo.bind(on_touch_down=self.hyperlink)
        self.add_widget(self.openweather_logo)

    def set_grid_layout(self, grid_layout):
        self.grid_layout = grid_layout
        self.grid_layout.update(409)

    def button_click(self, button):
        location = self.location_input.text
        daily_weather = process_data(location)
        self.grid_layout.update(daily_weather)

    def hyperlink(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if touch.button == "left":
                webbrowser.open("https://openweathermap.org/")
                return True
        return False


class MyCenterLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyCenterLayout, self).__init__(**kwargs)
        self.daily_weather = 409

    def daily_button_click(self, index, daily_weather):
        self.daily_weather = daily_weather
        self.clear_widgets()

        if daily_weather == 409:
            enter_location_label = Label(
                text="Please insert a valid location",
                pos_hint={"center_x": 0.5, "center_y": 0.65},
                font_size="25sp",
            )
            self.add_widget(enter_location_label)
        elif daily_weather == 404:
            miss_location_label = Label(
                text="This location does not exist",
                pos_hint={"center_x": 0.5, "center_y": 0.65},
                font_size="25sp",
            )
            self.add_widget(miss_location_label)
        elif daily_weather == 400:
            data_fetch_fail_label = Label(
                text="Error on fetching data from API",
                pos_hint={"center_x": 0.5, "center_y": 0.65},
                font_size="25sp",
            )
            self.add_widget(data_fetch_fail_label)
        else:
            overview = get_overview(self.daily_weather)[index]
            img_path = {
                "Clear": "../images/clear.png",
                "Clouds": "../images/clouds.png",
                "Snow": "../images/snow.png",
                "Rain": "../images/rain.png",
                "Thunderstorm": "../images/thunderstorm.png",
            }.get(overview, "")

            self.add_widget(
                Image(
                    size_hint=(0.6, 0.8),
                    pos_hint={"center_x": 0.25, "center_y": 0.78},
                    source=img_path,
                )
            )

            wind_speeds = get_wind_speed(self.daily_weather)[index]
            img_path2 = {
                "Light": "../images/light.png",
                "Moderate": "../images/moderate.png",
                "Strong": "../images/strong.png",
            }.get(wind_speeds, "")

            self.add_widget(
                Image(
                    size_hint=(0.6, 0.8),
                    pos_hint={"center_x": 0.25, "center_y": 0.475},
                    source=img_path2,
                )
            )

            max_temps = get_temperatures(self.daily_weather, "max")[index]
            min_temps = get_temperatures(self.daily_weather, "min")[index]

            maxtemp_label = Label(
                text=f"Max Temp: {max_temps}",
                pos_hint={"center_x": 0.5, "center_y": 0.60},
                font_size="18sp",
            )
            mintemp_label = Label(
                text=f"Min Temp: {min_temps}",
                pos_hint={"center_x": 0.5, "center_y": 0.66},
                font_size="18sp",
            )
            wind_speed_label = Label(
                text=f"Wind Speed: {wind_speeds}",
                pos_hint={"center_x": 0.65, "center_y": 0.475},
                font_size="18sp",
            )
            overview_label = Label(
                text=f"Description: {overview}",
                pos_hint={"center_x": 0.73, "center_y": 0.78},
                font_size="18sp",
            )

            self.add_widget(maxtemp_label)
            self.add_widget(mintemp_label)
            self.add_widget(wind_speed_label)
            self.add_widget(overview_label)


class MyGridLayout(GridLayout):
    def __init__(self, center_layout, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 6
        self.padding = [20, 400, 20, 40]
        deep_blue = 139 / 255
        self.button_color = (0.0, 0.0, deep_blue, 1)
        self.daily_weather = 409
        self.center_layout = center_layout

    def update(self, daily_weather):
        self.clear_widgets()
        self.daily_weather = daily_weather

        days_week = get_days(daily_weather)
        max_temps = get_temperatures(daily_weather, "max")
        min_temps = get_temperatures(daily_weather, "min")

        for i in range(6):
            day = days_week[i]
            max_temp = max_temps[i]
            min_temp = min_temps[i]
            button_text = f"{day}\n\nMax:\n{max_temp}\n\nMin:\n{min_temp}"
            daily_button = Button(
                text=button_text,
                background_color=self.button_color,
                halign="center",
            )
            if i == 0:
                self.center_layout.daily_button_click(0, daily_weather)

            daily_button.bind(
                on_press=lambda btn, index=i: self.center_layout.daily_button_click(
                    index, daily_weather
                )
            )
            self.add_widget(daily_button)


class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        red, green, blue = 26 / 255, 26 / 255, 51 / 255

        with self.canvas.before:
            Color(red, green, blue, 1)
            self.bgrect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_bg, size=self.update_bg)

        self.center_layout = MyCenterLayout()
        self.grid_layout = MyGridLayout(self.center_layout)
        self.float_layout = MyFloatLayout()

        self.float_layout.set_grid_layout(self.grid_layout)

        self.add_widget(self.float_layout)
        self.add_widget(self.grid_layout)
        self.add_widget(self.center_layout)

    def update_bg(self, background, value):
        self.bgrect.pos = self.pos
        self.bgrect.size = self.size


class SkyCompass(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    SkyCompass().run()
