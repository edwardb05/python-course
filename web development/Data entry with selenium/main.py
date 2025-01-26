import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(ZILLOW_URL, headers=header)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")


prices_html = soup.find_all(class_ = "PropertyCardWrapper__StyledPriceLine")

prices_clean =[]
for price in prices_html:
    price =price.getText()
        # Remove any non-numeric characters after the price
    price = price.split("+")[0].split("/")[0]
        # Convert to integer and add to the list
    print(price)
    prices_clean.append(price)

address_html = soup.find_all('address')

address_clean =[]
for address in address_html:
    address =address.getText(strip =True)
    print(address)
    address_clean.append(address)

urls_html = soup.find_all(class_ = "property-card-link")

urls_clean =[]
for url in urls_html:
    url =url.get("href")
    print(url)
    urls_clean.append(url)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)




for n in range(len(address_clean)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf4b8MjfLxCPApxUZUxgOHkx-6bIQtf-xoX7uEdDQfHmeVb9Q/viewform?usp=header")
    time.sleep(2)

    
    address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submitbutton = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_input.send_keys(address_clean[n])
    price_input.send_keys(prices_clean[n])
    url_input.send_keys(urls_clean[n])
    submitbutton.click()