import requests
from bs4 import BeautifulSoup
import time
import random

vividData = {
    'Allister-V3': 4,
    'Rayquaza-Amazing-Burst': 35,
    'Bea-V3': 37
}

for key in vividData:
    item = key
    buyPrice = round(vividData[key] * 1.12, 2)
    

    # Build Url
    vividURL = 'https://www.cardmarket.com/en/Pokemon/Products/Singles/Vivid-Voltage/' + item + '?language=1&minCondition=2'

    #Setup and scrape data
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    page = requests.get(vividURL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    container = soup.find('div', {'class': 'price-container'})

    #Format price
    price = container.span.text
    price = price.replace(',','.')
    price = float(price[:-2])

    #Calculate difference between price and buy price
    difference = buyPrice - price
    difference = round(difference, 2)

    if price <= buyPrice:
        print('Price for item "' + item + '" is lower than its buy price by ' + str(difference) + '. Currently listed at ' + str(price) + '.')
    else:
        print('No deals found for "' + item + '".')

    time.sleep(random.randint(30, 60))
