# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:52:59 2022

@author: user
"""

'''
1. input job title into input box
2. get link, title, company, salary, date, location
3. Do this for every page until no jobs are left
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome(
        'C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://hk.indeed.com/?from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt')
time.sleep(2)

# Enter Job, Place, then click the button
JobTitle = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
JobTitle.send_keys('web developer')
#Place = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
#Place.send_keys('Hong Kong')
button = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button').click()

time.sleep(2)

df = pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Location':[''],'Salary':[''], 'Date':['']})
soup = BeautifulSoup(driver.page_source, 'lxml')
section = soup.find('div', class_ = 'mosaic mosaic-provider-jobcards mosaic-provider-hydrated')
postings = section.find_all('li')
count = 0 
while True:
    count += 1
    for post in postings:
        try:
            link = post.find('a', class_ = 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
            link_full = 'https://hk.indeed.com'+link
            title = post.find('h2', class_ = 'jobTitle css-1h4a4n5 eu4oa1w0').text.strip()
            company = post.find('span', class_ = 'companyName').text.strip()
            location = post.find('div', class_ = 'companyLocation').text.strip()
            salary = post.find('div', class_ = 'attribute_snippet').text.strip()
            date = post.find('span', class_ = 'date').text.strip()
        except:
            pass
        df = df.append({'Link':link_full, 'Job Title':title, 'Company':company, 'Location':location,'Salary':salary, 'Date':date}, ignore_index = True)
    if count > 20:
        break
    time.sleep(2)
    try: 
        next_page = soup.find('a', {'aria-label':'Next'}).get('href')
        next_page_full ="https://hk.indeed.com/" + next_page
        url = next_page_full
            
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        section = soup.find('div', class_ = 'mosaic mosaic-provider-jobcards mosaic-provider-hydrated')
        postings = section.find_all('li')
    except:
        pass
df.to_csv('C:/Users/user/Downloads/joblist.csv')