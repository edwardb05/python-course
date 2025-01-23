from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# sets chrome to stay open
driver = webdriver.Chrome(options=chrome_options)
# accesses python
driver.get("https://www.python.org")
# uses css selectors to pinpoint the time and then name
times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

# uses dictionary comprehension to creat dict with date and time
events = {n:{ 'name': names[n].text, 'time': times[n].text,} for n in range(len(times))}
print(events)


driver.close()