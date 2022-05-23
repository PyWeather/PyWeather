import requests
from datetime import datetime
from typing import Dict


class CurrentWeather(object):
    def __init__(self, country: str, city: str, api_key: str, units: str = 'metric', lang: str = 'pl'):
        lat_lon_url: str = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}"
        lat_lon: Dict = requests.get(lat_lon_url).json()
        current_url: str = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]['lat']}" \
                           f"&lon={lat_lon[0]['lon']}&appid={api_key}&units={units}&lang={lang}"
        data: Dict = requests.get(current_url).json()

        self.date_time: str = datetime.utcfromtimestamp(data["dt"] + 7200).strftime('%d-%m-%Yr. %H:%M:%S')
        self.temperature: float = data["main"]["temp"]
        self.feels_like: float = data["main"]["feels_like"]
        self.wind_speed: float = data["wind"]["speed"]
        self.humidity: int = data["main"]["humidity"]
        self.description: str = data["weather"][0]["description"]
        self.city: str = city
