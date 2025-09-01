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
print(response.json())