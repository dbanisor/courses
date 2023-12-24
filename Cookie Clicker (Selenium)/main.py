from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import math


path = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


five_sec_timer = float('{0:.1f}'.format(0.0))
how_fast_to_click = 0.1


def buy_upgrades():
    raw_store = []
    store = []
    entire_store = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]
    cursor = driver.find_elements(By.CLASS_NAME, "grayed")
    for i in cursor:
        raw_store.append(i.text)
    for i in raw_store:
        store.append(i.split(" - ")[0])
    can_buy = [element for element in entire_store if element not in store]
    button = "buy" + (can_buy[-1])
    find_button = driver.find_element(By.ID, button)
    find_button.click()

def check_score():
    money = driver.find_element(By.ID, "money")
    cookies = int(money.text)
    print(cookies)


def click_cookie(miliseconds):
    global five_sec_timer

    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    time.sleep(miliseconds)
    five_sec_timer += miliseconds


while five_sec_timer <= 60.0:
    click_cookie(miliseconds=how_fast_to_click)

    if round(five_sec_timer, 1) % 5 == 0:
        buy_upgrades()










