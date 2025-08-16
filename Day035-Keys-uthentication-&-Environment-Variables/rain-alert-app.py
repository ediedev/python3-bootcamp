import requests

# https://www.latlong.net/
MY_LAT = 0.347596
MY_LON = 32.582520

# https://openweathermap.org/
forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"
my_appid = "78ea50d7b0c4783f2516577959643fff"

parameters = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":my_appid,
}
response = requests.get(forecast_endpoint, params=parameters)
print(response.status_code)
weather_data = response.json()

weather_slice = weather_data["list"][:12]
for hourly_data in weather_slice:
    print(hourly_data["weather"][0])
