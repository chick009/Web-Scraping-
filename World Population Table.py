# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:31:57 2022

@author: user
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
print(table)

# Get Column Header
# Headers usually use th tag
table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

# Find Row Elements
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td') 
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
    
df.to_csv("C:/Users/user/Downloads/Table_Scraping.csv")