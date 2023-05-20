# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:55:51 2022

@author: user
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://www.google.com/')

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Top 100 Movies of All Time')


# The Type is submit(Form), so cannot use click
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')))
element.submit()

button = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a')
button.click()
print(driver.execute_script('return document.body.scrollHeight'))
time.sleep(3)


driver.execute_script('window.scrollTo(0,10000)')
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[50]/div[2]/a/img').screenshot('C:/users/user/Downloads/Halo3.png')

