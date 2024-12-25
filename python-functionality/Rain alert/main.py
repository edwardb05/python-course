import requests
import os
from twilio.rest import Client
TWILIO_ACC_SID = "ACdfbdff2ead5ab0bbe444e3f5427ea479"
TWILIO_AUTH_TOKEN = os.environ.get("TWIL_AUTH_TOKEN")
OWMAPI_KEY = os.environ.get("OWMAPI_KEY")
RAINYLAT =43.7228
RAINYLONG =10.4018
OWMPARAMS = {
    'lat' : RAINYLAT,
    'lon' : RAINYLONG,
    'appid': OWMAPI_KEY,
    'cnt': 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=OWMPARAMS)
response.raise_for_status()
data = response.json()
Raining = False
for i in range(0,4):
    if int(str(data['list'][i]['weather'][0]['id'])[0]) <= 7:
        Raining = True

if Raining:
    print(" You need an umbrella")
else:
    print("Sunny skies")
    client = Client(TWILIO_ACC_SID,TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body='its gonna rain today',
            from_= 'whatsapp:+14155238886',
            to= MYNUMBER
        )
    print(message.sid)