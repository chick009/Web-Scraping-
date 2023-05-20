# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:12:43 2022

@author: user
"""

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

driver.maximize_window()
driver.get('https://twitter.com/i/flow/login')
# Loading Time
time.sleep(10)
#element = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
#element = WebDriverWait(driver, 10).until(
   # EC.visibility_of_element_located((By.CLASS_NAME, 'r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu')))

# Login the twitter
login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys('johnnyyik5744@gmail.com')
button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
time.sleep(10)

password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys('yik147258')


button2 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
button2.click()
# Wait Search bar appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))

SearchBar = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
SearchBar.send_keys('The Rock')
SearchBar.send_keys(Keys.ENTER)

Find_People = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')
Find_People.click()

time.sleep(2)
Select = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span')
Select.click()

time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'lxml')
#postings = soup.find_all('')
postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
tweets = []
count = 0 

while True:
    for post in postings:
        tweets.append(post.text)
        print(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweets))
    
    count += 1
    if len(tweets2) > 20:
        break
    if count > 20:
        break

new_tweets = []
for i in tweets2:
    if '' in i:
        new_tweets.append(i)



