import requests
from datetime import datetime
from typing import List, Dict
from API.WeatherData import WeatherData


class DailyForecast(object):
    def __init__(self, country: str, city: str, api_key: str, units: str = 'metric', lang: str = 'pl'):
        lat_lon_url: str = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}"
        lat_lon: Dict = requests.get(lat_lon_url).json()
        forecast_url: str = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat_lon[0]['lat']}" \
                            f"&lon={lat_lon[0]['lon']}&appid={api_key}&units={units}&lang={lang}"
        data: Dict = requests.get(forecast_url).json()
        self.list_of_weather_data: List[Dict] = data["list"]
        self.parsed_day_data: List[WeatherData] = [WeatherData(city,
                                                               datetime.utcfromtimestamp(x["dt"] + 7200)
                                                               .strftime('%d-%m-%Yr. %H:%M:%S'),
                                                               x["main"]["temp"],
                                                               x["main"]["feels_like"],
                                                               x["main"]["humidity"],
                                                               x["wind"]["speed"],
                                                               x["weather"][0]["description"],
                                                               x["weather"][0]["icon"])
                                                   for x in self.list_of_weather_data
                                                   if datetime.utcfromtimestamp(x["dt"] + 7200).strftime('%H') == "14"]
        self.parsed_night_data: List[WeatherData] = [WeatherData(city,
                                                                 datetime.utcfromtimestamp(x["dt"] + 7200)
                                                                 .strftime('%d-%m-%Yr. %H:%M:%S'),
                                                                 x["main"]["temp"],
                                                                 x["main"]["feels_like"],
                                                                 x["main"]["humidity"],
                                                                 x["wind"]["speed"],
                                                                 x["weather"][0]["description"],
                                                                 x["weather"][0]["icon"])
                                                     for x in self.list_of_weather_data
                                                     if datetime.utcfromtimestamp(x["dt"] + 7200).strftime('%H') == "02"]
