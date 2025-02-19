import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(url, 'lxml')

def scrape_data(url,pages)->object:
    url = f''
    pages = [x for x in range(1,51)]
    names=[]
    current_prices=[]
    previous_price=[]
    discount=[]
    rating=[]

    for page in pages:
        items_name = soup.find_all('h3', class_='name')

        for name in items_name:
            names.append(name.text)



        prices = soup.find_all('div', class_='prc')
        for price in prices:
            current_price.append(price.text)


        old_prices = soup.find_all('div', class_='old')
        for price in old_prices:
            previous_price.append(price.text)

        p_discount = soup.find_all('div', class_='bdg _dsct _sm')
        for dsct in p_discount:
            discount.append(dsct.text)


        p_rating = soup.find_all('div',class_='rev')
        for rate in p_rating:
            rating.append(rate.text)

