import requests
from bs4 import BeautifulSoup
import pandas as pd

pages = [x for x in range(1,51)]
names = []
current_price = []
previous_price = []
discount = []

for page in pages:

    url = f'https://www.jumia.co.ke/televisions/?special_price={page}#catalog-listing'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')

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
        
    TV_data = {
        'name':names,
        'price':current_price,
        'initial_price': previous_price,
        'percentage_discount': discount
        }

TV = pd.DataFrame(TV_data,columns=['name','price','initial_price','percentage_discount'])
print(TV)


