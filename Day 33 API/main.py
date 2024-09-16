import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status() # raises a http error if there is one and states the problem

data = response.json()