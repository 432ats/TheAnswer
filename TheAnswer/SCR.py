# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 02:20:21 2019

@author: 81802
"""
import numpy as np
import BBD

data = np.load(file="bb_URLs_20190609.npy",)#URL配列ファイル読み込み
for i in(0,len(data)-1):
    bbd = baseballscrape.BBdata(data[i])
    bbd.scr_gamedeta()