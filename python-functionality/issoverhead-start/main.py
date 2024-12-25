import requests
from datetime import datetime
import smtplib

import os

GMAILEMAIL = os.getenv("GMAILEMAIL")
GMAILAPPPWD = os.getenv("GMAILAPPPWD")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
MYLAT = iss_latitude
MYLNG = iss_longitude
#Your position is within +5 or -5 degrees of the ISS position.
def istheissnearme():
    if MYLAT-5 <= iss_latitude <=  MYLAT+5 and MYLNG-5 <= iss_longitude <=  MYLNG+5 :
        return True
    else:
        return False
    
def isitnighttime():
    if sunrise<= time_now <= sunset:
        return False
    else:
        return True
    
def sendemail():
    if istheissnearme()  and isitnighttime() :
     with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Start secure connections
        connection.login(user= GMAILEMAIL, password= GMAILAPPPWD)
        connection.sendmail(
            from_addr= GMAILEMAIL, 
            to_addrs=GMAILEMAIL, 
            msg=f"You can see the ISS")
    else:
        if istheissnearme() == False:
            print("ISS not near")
        elif isitnighttime() == False:
            print("its not dark enough")
        else:
            print("error")


parameters = {
    "lat": MYLAT,
    "lng": MYLNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

datenow = datetime.now()
time_now = datenow.hour 

sendemail()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



