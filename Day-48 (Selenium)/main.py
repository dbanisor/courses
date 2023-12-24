from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import numpy

chrome_driver_path = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")
#
# logo = driver.find_element(By.ID, "nav-logo-sprites")
# print(logo.size)

# search_bar = driver.find_element(By.NAME, "field-keywords")
#print(search_bar.get_attribute("placeholder"))

# documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for n in range(0, len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text,
    }

print(events)


driver.close()















