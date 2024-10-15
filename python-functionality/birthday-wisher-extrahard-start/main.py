##################### Extra Hard Starting Project ######################
import datetime as dt 
import random
import smtplib
import pandas as pd
import os

GMAILEMAIL = os.getenv("GMAILEMAIL")
GMAILAPPPWD = os.getenv("GMAILEAPPPWD")
# ------send email ----#
def sendemail(name, year, EMAIL ):
    age = currentyear - year  
    rannum = random.randint(1,3)
    with open(f'birthday-wisher-extrahard-start/letter_templates/letter_{rannum}.txt', 'r') as letter:
        msg = letter.read()
    namedmsg =msg.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Start secure connections
        connection.login(user= GMAILEMAIL, password= GMAILAPPPWD)
        connection.sendmail(
            from_addr= GMAILEMAIL, 
            to_addrs=EMAIL, 
            msg=f"Subject:Can't believe you're {age}\n\n {namedmsg}")
    

# Read the CSV file
data = pd.read_csv("birthday-wisher-extrahard-start/birthdays.csv")
people = data.to_dict(orient="records")
today = dt.datetime.now()
currentmonth = today.month
currentday = today.day
currentyear= today.year
for person in people:
    if person['month'] == currentmonth and person['day'] == currentday:
        sendemail(person["name"], person['year'], person['email'])
        

# Added daily automation with python anywhere