import smtplib
import datetime as dt

MY_EMAIL = "<EMAIL>"
MY_PASSWORD = "<PASSWORD>"

# #email
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="<EMAIL>",
        msg="Subject:Test Message\n\nThis is a test message."
    )

#datetime
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
date_string = now.strftime("%d/%m/%Y")
time_string = now.strftime("%H:%M:%S")
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1990, month=7, day=30)

print(now)
print(year)
print(month)
print(day)
print(date_string)
print(time_string)
print(day_of_week)
print(date_of_birth)

