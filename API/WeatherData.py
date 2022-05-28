class WeatherData(object):
    def __init__(self, city: str, date: str, temperature: float, feels_like: float,
                 humidity: int, wind_speed: float, description: str, icon_id: str):
        self.city: str = city
        self.date: str = date
        self.temperature: float = temperature
        self.feels_like: float = feels_like
        self.humidity: int = humidity
        self.wind_speed: float = wind_speed
        self.description: str = description
        self.icon_id: str = icon_id
