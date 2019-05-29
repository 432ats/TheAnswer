# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:01:14 2019

@author: 81802
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='c:\\chromedriver_win32 (1)\\chromedriver.exe')
driver.get('https://spaia.jp/baseball/npb/game/2019040902')



inning        =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[1]')
top_bottom    =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/p/span[3]')
batcount      =driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/p[2]/span[2]')

#1回表二人目から最後の打者までの情報出力を繰り返す
while True:
 if str(inning.text)!= str(1) or str(top_bottom.text)!="表" or str(batcount.text)!= str(1):

#5秒待機 
       time.sleep(5)
     
#courseクラス,pitcherクラス,batterクラス,ballクラスを参照

       course         = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/div[4]/div[3]')
       pitcher        = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
       pitch_styles   = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
       batter         = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[1]')
       batter_styles  = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[1]/table/tbody/tr[2]/td[1]/p[2]')
       ball           = driver.find_elements_by_xpath('//*[@id="pitching-detail"]/div[2]/table/tbody')


#投手情報、打者情報を出力
       for e in pitcher:
          for f in pitch_styles:
              for g in batter:
                  for h in batter_styles:
                       print(e.text + "(" + f.text+ ") 対 "+ g.text + "(" + h.text + ")")


# courseクラスの中にあるspanタグのclass名を出力
# spanタグ内の球種情報を出力
       for c in course:
          for d in c.find_elements_by_tag_name("span"):
              print(d.get_attribute("class")) 
          #print(c.text)    
          
#上のc.textで球種出力してたけどこっちの方が詳細な情報出る（少し乱雑）
       for i in ball:
           print(i.text)
           
#出力後、[前へ]ボタンをクリック
       driver.find_element_by_xpath('//*[@id="game-live-pane"]/div[2]/div[1]/div/div[5]/div/div[1]').click()
       
          
 else:
           
       break
#最後に1回表一人目の打席の記録を出力
time.sleep(5)
       
for e in pitcher:
          for f in pitch_styles:
              for g in batter:
                  for h in batter_styles:
                       print(e.text + "(" + f.text+ ") 対 "+ g.text + "(" + h.text + ")")        
 
for c in course:
    for d in c.find_elements_by_tag_name("span"):
        print(d.get_attribute("class")) 
    #print(c.text)
    
for i in ball:
    print(i.text)
    
print("終了")  
 
driver.quit()                   

 
 
 