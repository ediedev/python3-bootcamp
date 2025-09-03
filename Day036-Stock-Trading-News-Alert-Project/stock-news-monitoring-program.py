import requests
from twilio.rest import Client
import os
STOCK_NAME = "TSLA"
MY_appid = os.environ.get("MY_APPID")
STOCK_END_POINT = "https://www.alphavantage.co/query"

MY_STOCK_API_KEY = "SBXMW1XJQ4B3OKNY"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_STOCK_API_KEY,
}
#Get yesterday's colsing price
response = requests.get(STOCK_END_POINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

#Get the day before yesterday's price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

#find the positive difference in prices
diffence = abs(yesterday_closing_price - day_before_yesterday_closing_price)
print(diffence)

#percentage difference
diff_percent = (diffence / yesterday_closing_price) * 100
print(diff_percent)

#check if the diffence percentage is greater the 5
if diff_percent > 5:
    print("Get News")