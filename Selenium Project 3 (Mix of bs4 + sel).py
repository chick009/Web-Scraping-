# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 19:45:40 2022

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome(
        'C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')

driver.get('https://store.unionlosangeles.com/collections/kapital')

# Scroll To The Bottom
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

# Find The section and postings
soup = BeautifulSoup(driver.page_source, 'lxml')

section = soup.find('div', {'class': 'isp_serp_theme_classico', 'id': 'isp_search_result_page_container'})

postings = section.find_all('li')

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Price':['']})
    
# Find the text and append DF
for post in postings:
    try:
        link = post.find('a', class_ = 'isp_product_image_href').get('href')
        link_full = 'https://store.unionlosangeles.com' + link
        name = post.find('div', class_ = 'isp_product_title').text
        price = post.find('div', class_ = 'isp_product_price_wrapper').text
        df = df.append({'Link':link_full, 'Name':name,'Price':price},
                       ignore_index = True)
    except:
        pass