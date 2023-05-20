# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:02:09 2022

@author: user
"""

# 1. Links
# 2. Name of each car
# 3. price of each car
# 4. Color of each car
# 5. put all data in a table
# 6. do this for the first 10-15 pages

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7"
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

df = pd.DataFrame({'Links': [''],'Name':[''], 'Price': [''], 'Color': ['']})
count = 0 
while count < 10:
    cars = soup.find_all('div', class_ = 'media soft push-none rule')
    for car in cars:
        try:
            link = car.find('a', class_ = 'media__img media__img--thumb').get('href')
            link_full = 'https://www.carpages.ca' + link
            name = car.find('h4', class_ = 'hN').text.strip()
            price = car.find('strong', class_ = 'delta').text.strip()
            color = car.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
            #price = car.find('strong', class_ = 'delta ').text, text will remove space automatically
            df = df.append({'Links':link_full,'Name':name,
                                'Price':price, 'Color':color}, ignore_index = True)
        except:
            pass
    try:
        try:
            next_page = soup.find_all('a', class_ = 'nextprev')[1].get('href')
        except:
            next_page = soup.find('a', class_ = 'nextprev').get('href')
        next_page_full = 'https://www.carpages.ca' + next_page
        url = next_page_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'lxml')
        count += 1
    except:
        pass
  
    
df.to_csv('C:/Users/user/Downloads/cars_new.csv')
        
        
        