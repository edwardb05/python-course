import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("GMAILEMAIL")
PASSWORD = os.getenv("GMAILPWD")
APPPWD = os.getenv("GMAILAPPPWD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
URL = "https://appbrewery.github.io/instant_pot/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

text = requests.get(url=URL, headers=header).text


soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

price_as_float = float(price.strip("$"))
title = soup.find(id="productTitle").get_text().strip()


# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, APPPWD,)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )