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
        self.icon: tk.PhotoImage = tk.PhotoImage(file="res/images/icon.png")
        self.canvas: tk.Canvas = tk.Canvas(self.window)
        self.background: tk.PhotoImage = tk.PhotoImage(file="res/images/background/background2.png")

        with open("res/data/images.json", encoding="UTF-8") as file:
            self.weather_icons: Dict[str, str] = json.load(file)

        with open("res/data/wind_speed.json", encoding="UTF-8") as file:
            self.wind_speed_unit: str = json.load(file)[self.units]

        with open("res/data/temp_units.json", encoding="UTF-8") as file:
            self.temp_units: str = json.load(file)[self.units]

        self.current_weather_image: tk.PhotoImage = tk.PhotoImage(file=f"res/images/weather_icons/"
                                                                       f"{self.weather_icons[self.current.icon_id[:2]]}"
                                                                  ).subsample(9, 9)
        self.unit_image: tk.PhotoImage = tk.PhotoImage(file=f"res/images/symbols/{self.units}.png").subsample(17, 17)
        self.unit_icon: tk.PhotoImage = tk.PhotoImage(file=f"res/images/symbols/{self.units}.png").subsample(35, 35)
        self.wind_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/wind.png").subsample(30, 30)
        self.humidity_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/humidity.png").subsample(8, 8)
        self.sunrise_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/sunrise.png").subsample(25, 25)
        self.sunset_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/sunset.png").subsample(25, 25)
        self.day_night_icon: tk.PhotoImage = tk.PhotoImage(file="res/images/symbols/day_night.png").subsample(25, 25)

        self.hourly_icons = [tk.PhotoImage(file=f"res/images/weather_icons/"
                                                f"{self.weather_icons[i.icon_id[:2]]}").subsample(17, 17)
                             for i in self.hourly.parsed_data]

        self.daily_icons = [tk.PhotoImage(file=f"res/images/weather_icons/"
                                               f"{self.weather_icons[i.icon_id[:2]]}").subsample(14, 14)
                            for i in self.daily.parsed_day_data]

        self.create_window()
        self.window.mainloop()

    def create_window(self):
        self.window.geometry("+500+200")
        self.window.resizable(width=False, height=False)
        self.window.title(f"PyWeather - {self.current.city}, {self.current.date_time}")
        self.window.iconphoto(False, self.icon)
        self.canvas.config(width=800, height=600, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(400, 300, image=self.background)
        self.show_current_weather()
        self.canvas.create_line(0, 255, 800, 255, width=2)
        self.show_hourly_forecast()
        self.canvas.create_line(0, 405, 800, 405, width=2)
        self.show_daily_forecast()

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

    def show_hourly_forecast(self):
        x = 85
        hour_y = 270
        icon_y = 330
        temp_y = 385

        for icon, data in zip(self.hourly_icons, self.hourly.parsed_data):
            self.canvas.create_text(x-2, hour_y, text=data.date[12:][:6], font=("TkDefaultFont", 14))
            self.canvas.create_image(x, icon_y, image=icon)
            self.canvas.create_text(x, temp_y, text=f"{round(data.temperature, 1)} {self.temp_units}",
                                    font=("TkDefaultFont", 14))
            x += 90

    def show_daily_forecast(self):
        x = 100
        date_y = 420
        weather_symbol_y = 485
        icon_temp_y = 565

        for icon, day_data, night_data in zip(self.daily_icons, self.daily.parsed_day_data, self.daily.parsed_night_data):
            self.canvas.create_text(x, date_y, text=day_data.date[:12], font=("TkDefaultFont", 14))
            self.canvas.create_image(x, weather_symbol_y, image=icon)
            self.canvas.create_image(x-40, icon_temp_y, image=self.day_night_icon)
            self.canvas.create_text(x+20, icon_temp_y, text=f"{round(day_data.temperature, 1)} {self.temp_units}\n"
                                                            f"{round(night_data.temperature, 1)} {self.temp_units}",
                                    font=("TkDefaultFont", 14))
            x += 150
