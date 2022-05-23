from CurrentWeather import CurrentWeather
from ThreeHourForecast import ThreeHourForecast
from DailyForecast import DailyForecast

api_key = "e3b4d61af9466bfa61b7d81adff527ba"

current_weather = CurrentWeather("PL", "Zielona Góra", api_key)

print(f"{current_weather.city}:\n"
      f"Data i godzina: {current_weather.date_time}\n"
      f"Temperatura: {current_weather.temperature}\n"
      f"Odczuwalna temperatura: {current_weather.feels_like}\n"
      f"Wilgotność powietrza: {current_weather.humidity}\n"
      f"Prędkość wiatru: {current_weather.wind_speed}\n"
      f"Pogoda: {current_weather.description.capitalize()}\n"
      f"Wschód słońca: {current_weather.sunrise}\n"
      f"Zachód słońca: {current_weather.sunset}")

print("\n=================\n")

three_hour_forecast = ThreeHourForecast("PL", "Zielona Góra", api_key)

print(f"{three_hour_forecast.parsed_data[0].city}:\n"
      f"Data i godzina: {three_hour_forecast.parsed_data[0].date}\n"
      f"Temperatura: {three_hour_forecast.parsed_data[0].temperature}\n"
      f"Odczuwalna temperatura: {three_hour_forecast.parsed_data[0].feels_like}\n"
      f"Wilgotność powietrza: {three_hour_forecast.parsed_data[0].humidity}\n"
      f"Prędkość wiatru: {three_hour_forecast.parsed_data[0].wind_speed}\n"
      f"Pogoda: {three_hour_forecast.parsed_data[0].description.capitalize()}")

print("\n=================\n")

daily_forecast = DailyForecast("PL", "Zielona Góra", api_key)

for i in daily_forecast.parsed_day_data:
    print(f"{i.city}:\n"
          f"Data i godzina: {i.date}\n"
          f"Temperatura: {i.temperature}\n"
          f"Odczuwalna temperatura: {i.feels_like}\n"
          f"Wilgotność powietrza: {i.humidity}\n"
          f"Prędkość wiatru: {i.wind_speed}\n"
          f"Pogoda: {i.description.capitalize()}\n")

for i in daily_forecast.parsed_night_data:
    print(f"{i.city}:\n"
          f"Data i godzina: {i.date}\n"
          f"Temperatura: {i.temperature}\n"
          f"Odczuwalna temperatura: {i.feels_like}\n"
          f"Wilgotność powietrza: {i.humidity}\n"
          f"Prędkość wiatru: {i.wind_speed}\n"
          f"Pogoda: {i.description.capitalize()}\n")
