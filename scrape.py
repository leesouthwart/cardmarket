from bs4 import BeautifulSoup
import time, random, json, requests

f = open('data.json',)
data = json.load(f)


def checkPrice(setName):
    for key in data[setName]:
        val = data[setName][key]
        item = key
        buyPrice = round(val * 1.12, 2) #Multiply to get EUR price
        

        # Build Url
        vividURL = 'https://www.cardmarket.com/en/Pokemon/Products/Singles/' + setName + '/' + item + '?language=1&minCondition=2'

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

        # Lets not get IP banned or stress their servers
        time.sleep(random.randint(15, 60))

    f.close()

checkPrice('rebel-clash')
checkPrice('vivid-voltage')