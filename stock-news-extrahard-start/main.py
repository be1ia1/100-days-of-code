import os
import requests
from datetime import date, timedelta


today = date(2024, 10, 18)
today_fd = today.strftime('%Y-%m-%d')
yesterday = today - timedelta(days=1)
yesterday_fd = yesterday.strftime('%Y-%m-%d')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("alphavantage_api_key")
}
alphavantage_url = "https://www.alphavantage.co/query"

# responce = requests.get(url=alphavantage_url, params=alphavantage_params)
# responce.raise_for_status()
# price_data = responce.json()

today_price = 248.89 #float(price_data['Time Series (Daily)'][today_fd]['4. close'])
yesterday_price = 220.89#float(price_data['Time Series (Daily)'][yesterday_fd]['4. close'])
percentage = int((today_price * 100 / yesterday_price) - 100)
# if percentage >= 5 or percentage <= -5:
#     print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
newsapi_params = {
    "q" : COMPANY_NAME,
    "language": "en",
    "apiKey": os.environ.get("newsapi_key")
}
newsapi_url = "https://newsapi.org/v2/everything"

responce = requests.get(url=newsapi_url, params=newsapi_params)
responce.raise_for_status()
news_data = responce.json()

first_news = news_data['articles'][:3]
for news in first_news:
    print(news['title'])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

