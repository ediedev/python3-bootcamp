import smtplib
import datetime as dt
import random

SENDER_EMAIL = "<EMAIL>"
SENDER_PASSWORD = "<PASSWORD>"
RECEIVER_EMAIL = "<EMAIL>"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
        print(quote)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

