import sys
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import json
import os
from API.CurrentWeather import CurrentWeather
from API.DailyForecast import DailyForecast
from API.ThreeHourForecast import ThreeHourForecast
from forecast_window import ForecastWindow


class Menu(object):
    def __init__(self):
        self.api_key = self.get_api()
        self.window: tk.Tk = tk.Tk()
        self.icon: tk.PhotoImage = tk.PhotoImage(file="res/images/icon.png")
        self.canvas: tk.Canvas = tk.Canvas(self.window)
        self.background: tk.PhotoImage = tk.PhotoImage(file="res/images/background/background1.png")
        with open("res/data/country_codes.json", encoding="UTF-8") as file:
            self.country_codes = json.load(file)
        self.countries: Combobox = Combobox(self.window, values=list(self.country_codes.values()), state="readonly")
        with open("res/data/units.json", encoding="UTF-8") as file:
            self.units = json.load(file)
        self.units_widget: Combobox = Combobox(self.window, values=list(self.units.keys()), state="readonly")
        self.city: tk.Entry = tk.Entry(self.window, width=100)
        self.search_button: tk.Button = tk.Button(self.window, command=self.search, text="\U0001F50D Szukaj")
        self.create_menu()

    @staticmethod
    def get_api() -> str:
        if not os.path.isfile("api_key.txt"):
            open("api_key.txt", 'x').close()
            sys.exit()
        else:
            with open("api_key.txt") as file:
                return file.read()

    def search(self):
        units: str = self.units[self.units_widget.get()]
        try:
            current: CurrentWeather = CurrentWeather(self.countries.get(),
                                                     self.city.get(),
                                                     self.api_key,
                                                     units)
            hourly: ThreeHourForecast = ThreeHourForecast(self.countries.get(),
                                                          self.city.get(),
                                                          self.api_key,
                                                          units)
            daily: DailyForecast = DailyForecast(self.countries.get(),
                                                 self.city.get(),
                                                 self.api_key,
                                                 units)

            self.window.destroy()
            ForecastWindow(current, hourly, daily, units)

        except IndexError:
            messagebox.showerror("Nieznana miejscowość", "Nie znaleźliśmy takiej miejsowości.")
        except KeyError:
            messagebox.showerror("Brak miasta", "Nazwa miasta nie została wprowadzona.")

    def create_menu(self):
        self.window.geometry("+500+200")
        self.window.resizable(width=False, height=False)
        self.window.title("PyWeather")
        self.window.iconphoto(False, self.icon)
        self.canvas.config(width=800, height=600, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(400, 300, image=self.background)
        self.countries.current(list(self.country_codes.keys()).index("PL"))
        self.countries.place(x=60, y=330, width=120, height=50)
        self.units_widget.current(list(self.units.keys()).index("Celsius"))
        self.units_widget.place(x=600, y=330, width=120, height=50)
        self.city.place(x=190, y=330, width=400, height=50)
        self.search_button.place(x=315, y=400, width=150, height=50)


if __name__ == "__main__":
    menu: Menu = Menu()
    menu.window.mainloop()
