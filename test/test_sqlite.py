from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
# driver = webdriver.Chrome()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.ID, "gsc-i-id2")

# print complete element
print(element)