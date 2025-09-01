import requests
from twilio.rest import Client
import os

# Create environment variable
os.environ["MY_APPID"] = "78ea50d7b0c4783f2516577959643fff"
os.environ["TWILIO_ACCOUNT_SID"] = "ACcbadacc7f646347edf16696b8d191c3e"
# latlong.net
MY_LAT = 45.189505
MY_LON = 11.604997
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = "74661cb0f513955e363cd208f03e9430"

# openweathermap
forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
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
        from_="+1 909 403 0243",
        to="+256726777004",
    )
    print(message.sid)

