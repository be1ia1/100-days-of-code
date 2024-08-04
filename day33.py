import requests
from datetime import datetime

# responce = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
# data = responce.json()

# longtitude = data["iss_position"]["longtitude"]
# latitude = data["iss_position"]["latitude"]

MY_PARAMS = {
    "lat": 49.419444,
    "lng": 26.979444,
    "formatted": 0
}

responce = requests.get(url="https://api.sunrise-sunset.org/json", params=MY_PARAMS)
responce.raise_for_status()
data = responce.json()
sunrise = data["results"]["sunrise"]
sunrise_hour = int((sunrise.split('T')[1]).split(':')[0]) + 3
sunset = data["results"]["sunset"]

now = datetime.now()



print(sunrise_hour)