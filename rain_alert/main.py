import requests
import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

WEATHER_PARAMS = {
    "appid": os.environ["OPENWEATHERMAP_APP_ID"],
    "lat": 49.42,
    "lon": 26.99,
    "cnt": 4
}
URL = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=URL, params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()

ids = []
for weather_list in weather_data["list"]:
    ids.append(weather_list["weather"][0]["id"])

if any(id < 700 for id in ids):
    message = client.messages.create(
    body="Bring an umbrella.",
    from_="+12489878966",
    to=os.environ["MY_PHONE_NUMBER"],
)
