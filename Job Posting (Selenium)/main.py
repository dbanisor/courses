from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


path = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&keywords=python%20developer")

sing_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sing_in_button.click()

email = driver.find_element(By.ID, "username")
email.send_keys("denise.banisor@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("Bani$or123!@#")

sing_in_again_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sing_in_again_button.click()