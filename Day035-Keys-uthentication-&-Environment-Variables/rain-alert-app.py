import requests
from twilio.rest import Client
import os

# Create environment variable
# latlong.net
MY_LAT = 45.189505
MY_LON = 11.604997

# openweathermap
forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_appid = os.environ.get("MY_APPID")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
parameters = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":my_appid,
}
weather_data = requests.get(forecast_endpoint, params=parameters).json()

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

