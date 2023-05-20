# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:32:59 2022

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome(
        'C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')

driver.get('https://www.nike.com.hk/su22_summerdelight/list.htm?ds_rl=1272577&cp=hkns_kw_200622_u_CCAT_SU22SeasonEndSale_gg01_brand_pure&gclid=CjwKCAjwk_WVBhBZEiwAUHQCmQepBerjSffXKXfnVMWLCh2VBUrZj4wmcOeYDYrGQjk3TSmLvR6ECBoCxR8QAvD_BwE&gclsrc=aw.ds')

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('li', class_ = 'style_liborder_new swiper-slide')

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''], 'Price':[''], 'Sale Price':['']})

for product in product_card:
    try:
        link = product.find('a', class_ = 'product_list_name').get('href')
        name = product.find('span', class_ = 'up').text
        full_price = product.find('span', class_ = 'origin_price').text
        discount_price = product.find('dd', class_ = 'color666').text
        df = df.append({'Link':link, 'Name':name,'Price':full_price, 'Sale Price':discount_price},
                       ignore_index = True)
    except: 
        pass

df.to_csv('C:/Users/user/Downloads/file_name.csv')