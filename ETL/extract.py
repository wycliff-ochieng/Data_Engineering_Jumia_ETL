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
#print(TV)

TV.to_csv('jumiatv.csv',index=False)


phone_pages = [x for x in range(1,51)]
phone_name = []
phone_price = []
old_price = []
percentage_discount = []

for phone in phone_pages:
    url2 = f'https://www.jumia.co.ke/mobile-phones/?price_discount=10-100&page={phone}#catalog-listing'
    r2 = requests.get(url2)
    soup = BeautifulSoup(r2.text,'lxml')

    brand = soup.find_all('h3', class_='name')
    for name in brand:
        phone_name.append(name.text)
    prc = soup.find_all('div',class_='prc')
    for price in prc:
        phone_price.append(price.text)
    prev_prc = soup.find_all('div',class_='old')
    for price in prev_prc:
        old_price.append(price.text)
    p_discount = soup.find_all('div','bdg _dsct _sum')
    for p_dsct in p_discount:
        percentage_discount.append(p_dsct.text)

    phone_data = {
        "name":phone_name,
        "price":phone_price,
        "before":old_price,
        "discount":percentage_discount
    }
phones = pd.DataFrame(phone_data,columns=["name","price","before","discount"])

phones.to_csv("jumia_phones.csv",index=False)



