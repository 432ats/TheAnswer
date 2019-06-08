# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:37:17 2019

@author: 81802
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

def URL_CREATER(x):#　x=西暦
    array=[]
    for l in range(3,12):
         if l<=9:
            SCH_URL='http://npb.jp/games/'+str(x)+'/schedule_'+str(0)+str(l)+'_detail.html'
            r = requests.get(SCH_URL)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,'html5lib')
            for k in range(int(l)*100+1,int(l)*100+32):
                a="date0"+str(k)
                d = soup.find_all(id=a)
                for m in range(0,len(d)):
                    if "勝：" in str(d[m]) or "分：" in str(d[m]):array.append( "https://spaia.jp/baseball/npb/game/"+str(x)+str(0)+str(k)+str(0)+str(m+1))
         else:
            SCH_URL='http://npb.jp/games/'+str(x)+'/schedule_'+str(l)+'_detail.html' 
            r = requests.get(SCH_URL)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,'html5lib')
            for k in range(int(l)*100+1,int(l)*100+32):
                a="date"+str(k)
                d = soup.find_all(id=a)
                for m in range(0,len(d)):
                    if "勝：" in str(d[m]) or "分：" in str(d[m]):array.append( "https://spaia.jp/baseball/npb/game/"+str(x)+str(k)+str(0)+str(m+1))
                
         
    df = pd.DataFrame(array)       
    return df
       
print(URL_CREATER(2019))