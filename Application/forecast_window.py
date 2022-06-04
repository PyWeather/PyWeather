import json
import tkinter as tk
from typing import Dict

from API.DailyForecast import DailyForecast
from API.ThreeHourForecast import ThreeHourForecast
from API.CurrentWeather import CurrentWeather


class ForecastWindow(object):
    def __init__(self, current: CurrentWeather, hourly: ThreeHourForecast, daily: DailyForecast, units: str):
        self.current: CurrentWeather = current
        self.hourly: ThreeHourForecast = hourly
        self.daily: DailyForecast = daily
        self.units: str = units

        self.window: tk.Tk = tk.Tk()
        self.window.title("PyWeather")
        self.icon: tk.PhotoImage = tk.PhotoImage(file="res/images/icon.png")
        self.window.iconphoto(False, self.icon)
        self.canvas: tk.Canvas = tk.Canvas(self.window)
        self.background: tk.PhotoImage = tk.PhotoImage(file="res/images/background/background2.png")

        with open("res/data/images.json") as file:
            self.weather_icons: Dict[str, str] = json.load(file)

        with open("res/data/wind_speed.json") as file:
            self.wind_speed_unit: str = json.load(file)[self.units]

        self.current_weather_image: tk.PhotoImage = tk.PhotoImage(file=f"res/images/weather_icons/"
                                                                       f"{self.weather_icons[self.current.icon_id[:2]]}"
                                                                  ).subsample(9, 9)
        self.unit_image: tk.PhotoImage = tk.PhotoImage(file=f"res/images/symbols/{self.units}.png").subsample(17, 17)
        self.unit_icon: tk.PhotoImage = tk.PhotoImage(file=f"res/images/symbols/{self.units}.png").subsample(35, 35)
        self.wind_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/wind.png").subsample(30, 30)
        self.humidity_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/humidity.png").subsample(8, 8)
        self.sunrise_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/sunrise.png").subsample(25, 25)
        self.sunset_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/sunset.png").subsample(25, 25)

        self.create_window()
        self.window.mainloop()

    def create_window(self):
        self.window.geometry("+500+200")
        self.window.resizable(width=False, height=False)
        self.canvas.config(width=800, height=600, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(400, 300, image=self.background)
        self.show_current_weather()

    def show_current_weather(self):
        self.canvas.create_image(150, 120, image=self.current_weather_image)
        self.canvas.create_text(300, 130, text=round(self.current.temperature, 1), font=("TkDefaultFont", 45))
        self.canvas.create_image(390, 130, image=self.unit_image)
        self.canvas.create_image(470, 60, image=self.unit_icon)
        self.canvas.create_text(515, 60, text=round(self.current.feels_like, 1), font=("TkDefaultFont", 20))
        self.canvas.create_image(470, 120, image=self.humidity_icon)
        self.canvas.create_text(525, 120, text=f"{self.current.humidity} %", font=("TkDefaultFont", 20))
        self.canvas.create_image(470, 180, image=self.wind_icon)
        self.canvas.create_text(550, 180, text=f"{self.current.wind_speed} {self.wind_speed_unit}",
                                font=("TkDefaultFont", 20))
        self.canvas.create_image(620, 60, image=self.sunrise_icon)
        self.canvas.create_text(700, 60, text=self.current.sunrise, font=("TkDefaultFont", 20))
        self.canvas.create_image(620, 120, image=self.sunset_icon)
        self.canvas.create_text(700, 120, text=self.current.sunset, font=("TkDefaultFont", 20))
