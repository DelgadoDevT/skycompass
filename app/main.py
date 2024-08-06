from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        
        gray = 211 / 255
        self.location_input = TextInput(size_hint=(0.5, 0.05), pos_hint={'x': 0.2, 'y': 0.9}, hint_text='Enter location', background_color=(gray, gray, gray, 1))
        self.add_widget(self.location_input)

        deep_blue = 139 / 255
        self.search_button = Button(size_hint=(0.05, 0.05), pos_hint={'x': 0.7, 'y': 0.9}, background_color=(0.0, 0.0, deep_blue, 1))
        self.add_widget(self.search_button)

class MyGridLayout(GridLayout): 
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 6
        self.padding = [20, 400, 20, 40]

        deep_blue = 139 / 255
        self.button_color = (0.0, 0.0, deep_blue, 1)

        self.add_widget(Button(text='World 1', background_color=self.button_color))
        self.add_widget(Button(text='World 2', background_color=self.button_color))
        self.add_widget(Button(text='World 3', background_color=self.button_color))
        self.add_widget(Button(text='World 4', background_color=self.button_color))
        self.add_widget(Button(text='World 5', background_color=self.button_color))
        self.add_widget(Button(text='World 6', background_color=self.button_color))

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        red, green, blue = 26 / 255, 26 / 255, 51 / 255

        with self.canvas.before:
            Color(red, green, blue, 1) 
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self._update_bg, size=self._update_bg)
        
        self.float_layout = MyFloatLayout()
        self.grid_layout = MyGridLayout()  
        
        self.add_widget(self.float_layout)
        self.add_widget(self.grid_layout)
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

class SkyCompass(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    SkyCompass().run()
