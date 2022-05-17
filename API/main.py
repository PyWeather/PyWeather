from CurrentWeather import CurrentWeather

api_key = "e3b4d61af9466bfa61b7d81adff527ba"


data = CurrentWeather("PL", "Zielona Góra", api_key)

print(f"{data.city}:\n"
      f"Data i godzina: {data.date_time}\n"
      f"Temperatura: {data.temperature}\n"
      f"Odczuwalna temperatora: {data.feels_like}\n"
      f"Wilgotność powietrza: {data.humidity}\n"
      f"Prędkość wiatru: {data.wind_speed}\n"
      f"Pogoda: {data.description.capitalize()}")
