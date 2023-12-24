from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Denise")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Banisor")
email = driver.find_element(By.NAME, "email")
email.send_keys("denise.banisor@gmail.com")
email.send_keys(Keys.TAB)
first_name.send_keys(Keys.ENTER)



# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
#
# random_article = driver.find_element(By.LINK_TEXT, "Random article")
# # random_article.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# driver.close()






