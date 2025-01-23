from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# sets chrome to stay open
driver = webdriver.Chrome(options=chrome_options)
# accesses the form
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def press_button_repeatedly(driver, duration=5, interval=0.0000001):

    start_time = time.time()
    
    # Find the button using the selector
    button = driver.find_element(By.ID, value = "cookie")
    
    # Repeat pressing the button for the given duration
    while time.time() - start_time < duration:
        button.click()
        time.sleep(interval)

def find_price(button):
        if button != None:
            button_price = button.find_element(By.TAG_NAME, "b").text

            # Split the text to extract the price part
            item_name, price_text = button_price.split(" - ")

            # Remove commas if they exist and convert to integer
            price = int(price_text.replace(",", ""))
        else:
            price = 0
        return price


def buy_most_expensive_item(driver):
    cookies = int(driver.find_element(By.ID, value = "money").text)
    button_ids = [
        'buyCursor',     # Cursor
        'buyGrandma',    # Grandma
        'buyFactory',    # Factory
        'buyMine',       # Mine
        'buyShipment',   # Shipment
    ]
    mostexpensive = None
    for button in button_ids:
        button = driver.find_element(By.ID, value = button)
        price = find_price(button)
        expensive_price = find_price(mostexpensive)

        if price <= cookies:
            if mostexpensive == None:
                mostexpensive = button

            elif int(price) >= int(expensive_price):
                mostexpensive = button
    if mostexpensive != None:
        mostexpensive.click()
    

# run code for 5 mins
start_time = time.time()
while time.time() - start_time < 300:
   
    press_button_repeatedly(driver)
    buy_most_expensive_item(driver)

driver.close()