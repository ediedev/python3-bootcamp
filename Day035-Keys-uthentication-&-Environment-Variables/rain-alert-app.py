import requests
from twilio.rest import Client
import os

# Create environment variable
os.environ["MY_APPID"] = "78ea50d7b0c4783f2516577959643fff"

# https://www.latlong.net/
MY_LAT = 0.347596
MY_LON = 32.582520
account_sid = "<KEY>"
auth_token = "<PASSWORD>"

# https://openweathermap.org/
forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"
my_appid = os.environ.get("MY_APPID")# Access environment variable

parameters = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":my_appid,
}
response = requests.get(forecast_endpoint, params=parameters)
weather_data = response.json()

will_rain = False
weather_slice = weather_data["list"][:12]
for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an Umbrella",
        from_="<Twilio generated phone number>",
        to="+256789914733",
    )
    print(message.sid)

