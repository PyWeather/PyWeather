import json
import tkinter as tk
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
        self.background: tk.PhotoImage = tk.PhotoImage(file="res/images/background/background3.png")

        with open("res/data/images.json") as file:
            self.weather_icons = json.load(file)

        self.current_weather_image = tk.PhotoImage(file=f"res/images/weather_icons/"
                                                        f"{self.weather_icons[self.current.icon_id[:2]]}").subsample(9, 9)

        self.unit_image = tk.PhotoImage(file=f"res/images/symbols/{self.units}.png").subsample(17, 17)

        self.create_window()
        self.window.mainloop()

    def create_window(self):
        self.window.geometry("+500+200")
        self.window.resizable(width=False, height=False)
        self.canvas.config(width=800, height=600, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(400, 300, image=self.background)
        self.canvas.create_image(150, 120, image=self.current_weather_image)
        self.canvas.create_text(300, 130, text=round(self.current.temperature, 1), font=("TkDefaultFont", 45))
        self.canvas.create_image(380, 130, image=self.unit_image)

    def show_current_weather(self): ...
