from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# sets chrome to stay open
driver = webdriver.Chrome(options=chrome_options)
# accesses wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# #use # for id
# articlecount = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount li:nth-child(2) a")
# print(articlecount.text)
# articlecount.click()

# # finds an element by the text the hyperlink shows
# portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# portals.click()

# find the search input
search = driver.find_element(by=By.NAME, value="search")
# use the keys library to press the enter key
search.send_keys("python", Keys.ENTER)
driver.close()