# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:18:19 2022

@author: user
"""

# 1. Import HTML into Python
# 2. Getting the price of stock
# 3. Closing Price of the stock
# 4. 52-Week Range (lower, upper)
# 5. Analyst Rating

import requests
from bs4 import BeautifulSoup
Result = dict()

# Requirement 1 
url = 'https://www.marketwatch.com/investing/stock/msft?mod=search_symbol'
page = requests.get(url)
page 

# Requirement 2 
soup = BeautifulSoup(page.text, 'lxml')
print(soup.find('bg-quote', class_ = 'value').text)
Result["Price Of Stock"] = soup.find('bg-quote', class_ = 'value').text

# Requirement 3
print(soup.find('td', class_ = 'table__cell u-semi').text)
Result["Closing Price Of Stock"] = soup.find('td', class_ = 'table__cell u-semi').text

# Requirement 4 
nested = soup.find('mw-rangebar', class_ = "element element--range range--yearly")
nested
FiftyWeek = nested.find_all('span', class_ = "primary")

# 1st Approach

New = []
for i in FiftyWeek:
    name = i.text
    New.append(name)

Result["52-Week-Range"] = New

# 2nd Approach
lower = nested.find_all('span', class_ = 'primary')[0].text
upper = nested.find_all('span', class_ = 'primary')[1].text
'''
New = []
for i in FiftyWeek:
    name = i.text
    New.append(FiftyWeek)
Result["Fifty Week"] = New
'''

# Requirement 5
Analyst = soup.find('li', class_ = 'analyst__option active').text
print(Analyst)
Result["Analyst-Rating"] = Analyst
print(Result)
