# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:01:14 2019

@author: 81802
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import numpy as np
import csv



options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='c:\\chromedriver_win32 (1)\\chromedriver.exe')
driver.get('https://spaia.jp/baseball/npb/game/2019040902')



inning         = driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[1]')
top_bottom     = driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[3]')
batcount       = driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/p[2]/span[2]')
course         = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[4]/div[3]')
pitcher        = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
pitch_styles   = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
batter         = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
batter_styles  = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
ball           = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[2]/table')
team_p         = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]/span[1]')
team_b         = driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]/span[1]')

def ps_t_separate():
    initialize_pitcher = pitch_styles.find_elements(By.TAG_NAME,"span")
    arr = np.array([])
    for i in range(len(initialize_pitcher)):
        arr = np.append(arr,initialize_pitcher[i].text)
    
    arr = np.delete(arr,1)
    return arr

def bs_t_separate():
    initialize_batter = batter_styles.find_elements(By.TAG_NAME,"span")
    arr = np.array([])
    for i in range(len(initialize_batter)):
        arr = np.append(arr,initialize_batter[i].text)
    
    arr = np.delete(arr,1)
    return arr

#csv用データ   
#必要データの多次元配列
baseball_deta_lists = np.array([])
#データ　行
factor_row = 0
#データ　列
factor_column = 10

#page_back()
while True:
      if str(inning.text)!= str(1) or str(top_bottom.text)!="表" or str(batcount.text)!= str(1):
          #5秒待機
          time.sleep(5)
          
          ball_row = ball.find_elements(By.TAG_NAME,"tr")
          factor_row = factor_row + len(ball_row) - 1


          for i in range(1,len(ball_row)):
                #必要データの一次元配列
                baseball_deta_list = np.array([])

                #テーブルの列取得
                ball_column = ball_row[i].find_elements(By.TAG_NAME,"td")

                baseball_deta_list = np.append(baseball_deta_list, ps_t_separate())
                baseball_deta_list = np.append(baseball_deta_list, pitcher.text)

                baseball_deta_list = np.append(baseball_deta_list, bs_t_separate())
                baseball_deta_list = np.append(baseball_deta_list, batter.text)




                for j in range(1,len(ball_column)-1):
                    baseball_deta_list = np.append(baseball_deta_list, ball_column[j].text)

                baseball_deta_lists = np.append(baseball_deta_lists, baseball_deta_list)

          #[前へ]ボタンをクリック
          driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/div/div[1]').click()

      else:break



baseball_deta_lists = baseball_deta_lists.reshape([factor_row, factor_column])
print(baseball_deta_lists)


driver.quit()      

print("終了")  
 