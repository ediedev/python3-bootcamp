import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
iss_position_data = data["iss_position"]
latitude = data["iss_position"]["latitude"]
# latitude_data = iss_position_data["latitude"]
longitude = (data["iss_position"]["longitude"])

iss_position = (latitude,longitude)
response.raise_for_status()
print(data)
print(iss_position_data)
print(latitude)
print(longitude)
print(iss_position)