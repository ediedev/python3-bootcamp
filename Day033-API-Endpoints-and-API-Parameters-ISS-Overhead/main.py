import requests
from datetime import datetime

# #iss
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()
# iss_position_data = data["iss_position"]
# latitude = data["iss_position"]["latitude"]
# # latitude_data = iss_position_data["latitude"]
# longitude = (data["iss_position"]["longitude"])
#
# iss_position = (latitude,longitude)
# response.raise_for_status()
# print(data)
# print(iss_position_data)
# print(latitude)
# print(longitude)
# print(iss_position)

#sunset sun rise
MY_LAT = 0.347596
MY_LONG = 32.582520

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
response.raise_for_status()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(data)
# print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":"))
# print(sunrise.split("T")[1].split(":")[0])
# print(sunrise.split("T")[1].split(":")[2].split("+"))

print(sunrise)
print(sunset)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)