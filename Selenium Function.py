# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 01:20:44 2022

@author: user
"""

# Write things into input box
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://www.google.com')

# Fill in input box
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Web Scraping Skill')
box.send_keys(Keys.ENTER)
'''
box.send_keys('Web Scraping Skill')
box.send_keys(Keys.ENTER)
'''

button = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a/h3')
button.click()



# Taking A screenshot
driver.save_screenshot('C:/users/user/Downloads/Halo.png')
driver.find_element().screenshot('C:/users/user/Downloads/Halo2.png')
# Scrape only X-Path Element

# Self- Scrolling
driver.execute_script('return document.body.scrollHeight') # The Body Height
driver.execute_script('window.scrollTo(0,60000)')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# Wait Time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://www.google.com')

# Wait 3 seconds until data is found
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(By.ID, 'cnt'))