# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:16:54 2022

@author: user
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ = "d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")
print(table)

table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns = headers)

# Find Row Elements
for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [td.text.strip() for td in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row
    