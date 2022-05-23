from CurrentWeather import CurrentWeather
from ThreeHourForecast import ThreeHourForecast

api_key = "e3b4d61af9466bfa61b7d81adff527ba"

data = CurrentWeather("PL", "Zielona Góra", api_key)

print(f"{data.city}:\n"
      f"Data i godzina: {data.date_time}\n"
      f"Temperatura: {data.temperature}\n"
      f"Odczuwalna temperatura: {data.feels_like}\n"
      f"Wilgotność powietrza: {data.humidity}\n"
      f"Prędkość wiatru: {data.wind_speed}\n"
      f"Pogoda: {data.description.capitalize()}\n"
      f"Wschód słońca: {data.sunrise}\n"
      f"Zachód słońca: {data.sunset}")

print("\n=================\n")

data2 = ThreeHourForecast("PL", "Zielona Góra", api_key)

print(f"{data2.parsed_data[0].city}:\n"
      f"Data i godzina: {data2.parsed_data[0].date}\n"
      f"Temperatura: {data2.parsed_data[0].temperature}\n"
      f"Odczuwalna temperatura: {data2.parsed_data[0].feels_like}\n"
      f"Wilgotność powietrza: {data2.parsed_data[0].humidity}\n"
      f"Prędkość wiatru: {data2.parsed_data[0].wind_speed}\n"
      f"Pogoda: {data2.parsed_data[0].description.capitalize()}")
