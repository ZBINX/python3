# scraper.py


import requests
from bs4 import BeautifulSoup

# The URL for the page the item is being sold on. Best Buy in this example
URL = "https://www.bestbuy.com/site/amd-ryzen-5-3600-3rd-generation-6-core-12-thread-3-6-ghz-4-2-ghz-max-boost-socket-am4-unlocked-desktop-processor/6356278.p?skuId=6356278"

# Get this by searching google for your 'User Agent'
headers = { "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/89.0.4389.90 Safari/537.36'}


page = requests.get(URL, headers=headers)


soup = BeautifulSoup(page.content, "html.parser")

# variables that calls on soup to find the certain class on the page. class_ not class
title = soup.find(class_="heading-5 v-fw-regular").get_text()

price = soup.find(class_="priceView-hero-price priceView-customer-price").get_text()

# Only shows the price 0:7, excluding other chars after 7 position.
converted_price = price[0:7]

print(converted_price)

print(title.strip())
