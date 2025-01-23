from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# sets chrome to stay open
driver = webdriver.Chrome(options=chrome_options)
# accesses the form
driver.get("http://secure-retreat-92358.herokuapp.com/")

# enter each element of the form
search = driver.find_element(by=By.CLASS_NAME, value="top")
search.send_keys("ed", Keys.TAB, 'b', Keys.TAB, 'eb@gmail.com')

# find the submit button and click it
submit = driver.find_element(by=By.CLASS_NAME, value="btn")
submit.click()
driver.close()