from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get("https://tinder.com/")

time.sleep(3)
log_in = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span').click()

time.sleep(3)
login_google = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button/span[2]').click()

time.sleep(3)
email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email.send_keys("contnoug22@gmail.com")

time.sleep(3)
