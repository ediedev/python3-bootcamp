import smtplib
import pandas as pd
import datetime as dt
import random

PLACEHOLDER = "[NAME]"
SENDER_EMAIL = "<EMAIL>"
SENDER_PASSWORD = "<PASSWORD>"
BD_FILE_LINK = "birthdays.csv"
random.choice("")

MESSAGE_LINK = f"letters/letter_{random.randint(1,2)}.txt"
message = pd.read_csv(BD_FILE_LINK)
names = message["name"]
receiver_email = message["email"]

now = dt.datetime.now()
month = now.month
day = now.day

if day == message["day"] and month == message["month"]:
    with open(MESSAGE_LINK) as letter_file:
        letter_content = letter_file.read()
        for name in names:
            new_letter = letter_content.replace(PLACEHOLDER, name)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=receiver_email,
            msg=f"Subject:Happy Birthday\n\n{new_letter}"
        )