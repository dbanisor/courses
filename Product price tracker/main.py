import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

MY_EMAIL = "contnoug22@gmail.com"
MY_PASS = "wqtkhzrqqetqhphg"


product_url = "https://www.amazon.com/BOOX-Android-G-Sensor-Digital-Notepad/dp/B08H83GCBT/ref=sr_1_11?keywords=remarkable+tablet&qid=1656601250&sr=8-11"

headers = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}

response = requests.get(product_url, headers=headers)
amazon_page = response.text.encode("utf-8")
soup = BeautifulSoup(amazon_page, "lxml")
titles = soup.select("h1")
title_text = [each_title.getText() for each_title in titles]
title = title_text[0].strip()


prices = soup.find(class_="a-offscreen")
price = float(prices.getText().split("$")[1])



if price < 300.00:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="denise.banisor@gmail.com",
            msg=f"Subject: Price drop for your product at Amazon!\n\nThe price of this product has dropped: {title}!\nIt is now ${price}! Check it out: {product_url}"
        )










