# ссылка из ДЗ с доступными api не открывает список, поэтому взял OpenWeather API
# После регистрации получил api key, который использовал для получения данных
import requests
import json
# данные погоды моего города (Таганрог)
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Taganrog&appid=my_api_key')
weather_data = json.loads(response.text)
with open('weather.json', 'w') as weather_data_file:
    json.dump(weather_data, weather_data_file)
