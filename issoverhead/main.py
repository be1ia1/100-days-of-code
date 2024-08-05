import requests
from datetime import datetime

MY_LAT = 49.419444 # Your latitude
MY_LONG = 26.979444 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
MY_LAT = iss_latitude + 2
MY_LONG = iss_longitude + 2

print(f"My coords: {MY_LAT} {MY_LONG}")
print(f"ISS coords: {iss_latitude} {iss_longitude}")

def is_nearby():
    return (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and\
        (MY_LONG - 5 < iss_longitude < MY_LONG + 5)

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }

parameters = {
    "lat": iss_latitude,
    "lng": iss_longitude,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_night():
    # print(time_now.hour)
    return sunset < time_now.hour < sunrise

print(is_nearby())
print(is_night())
if is_nearby() and not is_night():
    print('Look up')
