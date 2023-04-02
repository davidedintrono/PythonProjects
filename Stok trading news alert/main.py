import requests as req
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "ZQJGBCRIFQ929CP7"
NEWS_API_KEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    "interval": "60min",
}

stock_response = req.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (60min)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_close = float(data_list[0]["4. close"])
before_yesterday_close = float(data_list[16]["4. close"])

diff = round(((abs(yesterday_close - before_yesterday_close)/yesterday_close)*100), 2)

up_down = None
if yesterday_close - before_yesterday_close > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = req.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]

    formatted_articles = [f'{STOCK_NAME}: {up_down}{diff}%\nHeadline: {article["title"]}. \nBrief:\
                            {article["description"]}' for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
