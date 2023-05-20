# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 11:25:07 2022

@author: user
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.airbnb.ca/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Honolulu%2C%20HI%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-07-03&checkout=2022-07-04&source=structured_search_input_header&search_type=autocomplete_click"
page = requests.get(url,headers = {'User-agent': 'Super Bot Power Level Over 9000'})
print(page)

soup = BeautifulSoup(page.text,'lxml')

df = pd.DataFrame({'Links': [''],'Title':[''], 'Details': [''], 'Price': [''], 'Rating': [""]})
count = 0 
# Go Through Every page
while True:
    postings = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
    
    for post in postings:
        try:
            link = soup.find('a', class_ = 'ln2bl2p dir dir-ltr').get('href')
            link_full ="https://www.airbnb.ca" + link
            title = post.find('div', class_ = 't1jojoys dir dir-ltr').text
            price = post.find('span', class_ = 'a8jt5op dir dir-ltr').text
            rating = post.find('span', class_ = 'ru0q88m dir dir-ltr').text
            df = df.append({'Links':link_full,'Title':title,
                                'Price':price, 'Rating':rating}, ignore_index = True)
            count +=1
            if count > 200:
                break
        except:
            pass
        
    if count > 200:
        df.to_csv('C:/Users/user/Downloads/air.csv')
        break
    # Find a tag with aria label Next, then get the element in the href string
    try:
        next_page = soup.find('a', {'aria-label':'Next'}).get('href')
        next_page_full ="https://www.airbnb.ca" + next_page
        
        url = next_page_full
        page = requests.get(url,headers = {'User-agent': 'Super Bot Power Level Over 9000'})
        soup = BeautifulSoup(page.text,'lxml')
    except:
        pass
    
    
    
df.to_csv('C:/Users/user/Downloads/air.csv')

#next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
#next_page_full = "https://www.airbnb.ca" + next_page
#next_page_full

