from kivy.config import Config

Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_splitter import get_days, get_temperatures
from weather import process_data

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)

        gray = 211 / 255
        self.location_input = TextInput(
            size_hint=(0.5, 0.05),
            pos_hint={"x": 0.2, "y": 0.9},
            hint_text="Enter location",
            background_color=(gray, gray, gray, 1),
        )
        self.add_widget(self.location_input)

        deep_blue = 139 / 255
        self.search_button = Button(
            size_hint=(0.15, 0.05),
            pos_hint={"x": 0.7, "y": 0.9},
            background_color=(0.0, 0.0, deep_blue, 1),
            text="Search",
        )
        self.search_button.bind(on_press=self.button_click)
        self.add_widget(self.search_button)

    def set_grid_layout(self, grid_layout):
        self.grid_layout = grid_layout
        self.grid_layout.update(404)

    def button_click(self, button):
        location = self.location_input.text
        daily_weather = process_data(location)
        self.grid_layout.update(daily_weather)


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 6
        self.padding = [20, 400, 20, 40]
        deep_blue = 139 / 255
        self.button_color = (0.0, 0.0, deep_blue, 1)
        self.daily_weather = 404

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
            self.add_widget(
                Button(
                    text=button_text,
                    background_color=self.button_color,
                    halign="center",
                )
            )


class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        red, green, blue = 26 / 255, 26 / 255, 51 / 255

        with self.canvas.before:
            Color(red, green, blue, 1)
            self.bgrect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_bg, size=self.update_bg)

        self.grid_layout = MyGridLayout()
        self.float_layout = MyFloatLayout()

        self.float_layout.set_grid_layout(self.grid_layout)

        self.add_widget(self.float_layout)
        self.add_widget(self.grid_layout)

    def update_bg(self, background, value):
        self.bgrect.pos = self.pos
        self.bgrect.size = self.size


class SkyCompass(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    SkyCompass().run()
