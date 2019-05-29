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


        

class BBdata:
    def __init__(self,URL):
        self.URL = URL
        self.options                 = Options()
        self.options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        self.driver                  = webdriver.Chrome(executable_path='c:\\chromedriver_win32 (1)\\chromedriver.exe')
        self.driver.get(self.URL)
        
        self.inning                  = self.driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[1]')
        self.top_bottom              = self.driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[3]')
        self.batcount                = self.driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/p[2]/span[2]')
        self.course                  = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[4]/div[3]')
        self.pitcher                 = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
        self.pitch_styles            = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
        self.batter                  = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
        self.batter_styles           = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
        self.ball                    = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[2]/table')
        self.team_p                  = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]/span[1]')
        self.team_b                  = self.driver.find_element_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]/span[1]')
        
    
    def ps_t_separate(self):
        initialize_pitcher = self.pitch_styles.find_elements(By.TAG_NAME,"span")
        arr = np.array([])
        for i in range(len(initialize_pitcher)):
            arr = np.append(arr,initialize_pitcher[i].text)
        
        arr = np.delete(arr,1)
        return arr
        
    
    def bs_t_separate(self):
        initialize_batter = self.batter_styles.find_elements(By.TAG_NAME,"span")
        arr = np.array([])
        for i in range(len(initialize_batter)):
            arr = np.append(arr,initialize_batter[i].text)
        
        arr = np.delete(arr,1)
        return arr
    
    def scr_gamedeta(self):
        
        #必要データの多次元配列
        baseball_deta_lists = np.array([])
        #データ　行
        factor_row = 0
        #データ　列
        factor_column = 10
        
        while True:
            if str(self.inning.text)!=str(1) or str(self.top_bottom.text)!="表" or str(self.batcount.text)!=str(1):
                #5秒待機
                time.sleep(5)
                ball_row = self.ball.find_elements(By.TAG_NAME,"tr")
                factor_row = factor_row + len(ball_row) - 1
                
                for i in range(1,len(ball_row)):
                    #必要データの一次元配列
                    baseball_deta_list = np.array([])
                    
                    #テーブルの列取得
                    ball_column = ball_row[i].find_elements(By.TAG_NAME,"td")
    
                    baseball_deta_list = np.append(baseball_deta_list, self.ps_t_separate())
                    baseball_deta_list = np.append(baseball_deta_list, self.pitcher.text)
    
                    baseball_deta_list = np.append(baseball_deta_list, self.bs_t_separate())
                    baseball_deta_list = np.append(baseball_deta_list, self.batter.text)
                    
                    for j in range(1,len(ball_column)-1):
                        baseball_deta_list = np.append(baseball_deta_list, ball_column[j].text)

                    baseball_deta_lists = np.append(baseball_deta_lists, baseball_deta_list)

                #[前へ]ボタンをクリック
                self.driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/div/div[1]').click()

            else:break
                    
        baseball_deta_lists = baseball_deta_lists.reshape([factor_row, factor_column])
        print(baseball_deta_lists)



        self.driver.quit()      

        print("終了")