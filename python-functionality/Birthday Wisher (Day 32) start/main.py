import smtplib
import datetime as dt
import random
import os

GMAILEMAIL = os.getenv("GMAILEMAIL")
GMAILPWD = os.getenv("GMAILEPWD")
GMAILAPPPWD =os.getenv("GMAILAPPPWD")
YAHOOEMAIL = os.getenv("YAHOOEMAIL")
YAHOOPWD = os.getenv("YAHOOPWD")

def motivationalemail():
    quote =random.choice(quotes)
    quote = quote.split("-")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Start connections
        connection.login(user= GMAILEMAIL, password= GMAILAPPPWD)
        connection.sendmail(
            from_addr= GMAILEMAIL, 
            to_addrs=YAHOOEMAIL, 
            msg=f"Subject:{quote[1]}\n\n {quote[0]}")

today = dt.datetime.now()
day = today.weekday()
with open("Birthday Wisher (Day 32) start/quotes.txt", "r") as file:
    lines = file.readlines()
    quotes = [ line.strip() for line in lines]

if day == 0:
    motivationalemail()





