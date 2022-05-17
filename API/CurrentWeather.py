import requests
from datetime import datetime


class CurrentWeather(object):
    def __init__(self, country: str, city: str, api_key: str, units: str = 'metric', lang: str = 'pl'):
        lat_lon_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}"
        lat_lon = requests.get(lat_lon_url).json()
        current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]['lat']}" \
                      f"&lon={lat_lon[0]['lon']}&appid={api_key}&units={units}&lang={lang}"
        data = requests.get(current_url).json()

        self.date_time = datetime.utcfromtimestamp(data["dt"] + 7200).strftime('%d-%m-%Yr. %H:%M:%S')
        self.temperature = data["main"]["temp"]
        self.feels_like = data["main"]["feels_like"]
        self.wind_speed = data["wind"]["speed"]
        self.humidity = data["main"]["humidity"]
        self.description = data["weather"][0]["description"]
        self.city = city
