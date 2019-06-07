# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:01:14 2019

@author: 81802
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='c:\\chromedriver_win32 (1)\\chromedriver.exe')
driver.get('https://spaia.jp/baseball/npb/game/2019040902')



inning        =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[1]')
top_bottom    =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[3]')
batcount      =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/p[2]/span[2]')
course         = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[4]/div[3]')
pitcher        = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
pitch_styles   = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
batter         = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
batter_styles  = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
ball           = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[2]/table/tbody')


for i in range(5):
    print(course.find_elements(By.TAG_NAME,"span")[i*3].get_attribute("class"))
    
print("終了")  
 
driver.quit()                   

 
 
 