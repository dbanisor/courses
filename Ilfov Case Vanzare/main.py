import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "myhttpheader.com",
    "Accept-Encoding": "gzip, deflate",
}



google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSepbdBedc_o_kkYm6GpiOS4pGoekdjX0WSgUmCpR-2xCkSYqA/viewform?usp=sf_link"

response = requests.get(url="https://www.zillow.com/new-york-ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51938436914062%2C%22east%22%3A-73.43997763085937%2C%22south%22%3A40.370121612150115%2C%22north%22%3A41.023977113739846%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list_card_info a")

all_links = []
for link in all_link_elements:
    all_links.append(link["href"])
    # if "http" not in href:
    #     all_links.append(f"https://www.zillow.com{href}")
    # else:
    #     all_links.append(href)

print(all_links)




# all_properties = soup.find_all(name="div", class_="list-card-info")
# print(all_properties)
# links = []
# texts = []
#
# for property_link in all_properties:
#     text = property_link.getText()
#     texts.append(text)
#     link = property_link.get("href")
#     links.append(link)
# print(texts)
# print(links)
#
# for a in soup.find_all("a", href=True):
#     links = []
#     links.append(a['href'])
#     print(links)



# adress_text = [each_adress.getText() for each_adress in adresses]
# print(adress_text)
#
# prices = soup.find_all("span", "price")














