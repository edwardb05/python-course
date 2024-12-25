import os
import smtplib


# Using a .env file to retrieve the phone numbers and tokens.


class NotificationManager:
    def __init__(self) -> None:
        self.email =os.environ.get("GMAILEMAIL")
        self.password = os.environ.get("GMAILAPPPWD")
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])

    def sendemail(self, message_body, email_list):
        with self.connection:
            self.connection.starttls() #Start secure connections
            self.connection.login(user= self.email, password= self.password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message_body}".encode('utf-8')
                                    )
                            