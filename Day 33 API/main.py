import requests

MYLAT = 49.466004
MYLNG = -2.536076
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # raises a http error if there is one and states the problem

# data = response.json()
parameters = {
    "lat": MYLAT,
    "lng": MYLNG,
    "formatted" : 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data =response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)