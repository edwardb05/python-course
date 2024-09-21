import os
import smtplib


# Using a .env file to retrieve the phone numbers and tokens.
GMAILEMAIL = os.environ.get("GMAILEMAIL")
GMAILAPPPWD = os.environ.get("GMAILAPPPWD")

class NotificationManager:


    def sendemail(self, message_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #Start secure connections
            connection.login(user= GMAILEMAIL, password= GMAILAPPPWD)
            connection.sendmail(
                from_addr= GMAILEMAIL, 
                to_addrs=GMAILEMAIL, 
                msg=message_body)