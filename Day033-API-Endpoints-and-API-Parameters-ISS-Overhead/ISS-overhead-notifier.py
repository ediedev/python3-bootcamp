import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0.347596
MY_LONG = 32.582520
SENDER_EMAIL = "<EMAIL>"
SENDER_PASSWORD = "<PASSWORD>"
RECEIVER_EMAIL = "<EMAIL>"

def is_iss_overhead():
    """Returns true if iss_location is close to my_location"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float((data["iss_position"]["longitude"]))

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return None


def is_night():
    """Returns true if its at night"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    response.raise_for_status()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now <= sunrise:
        return True
    return None

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Monday Motivation\n\nThe ISS is above you in the Sky."
            )
