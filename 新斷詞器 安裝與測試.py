# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:27:15 2022

@author: lisha
"""

#套件安裝
#pip install -U ckiptagger[tf,gdown] 


from ckiptagger import data_utils, construct_dictionary, WS, POS
#模型下載(約2G)
data_utils.download_data_gdown("./")

#建立斷詞器(或標註器)
ws = WS("./data/")
pos = POS("./data")

#測試Data
string = ["傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。"]
#斷詞的一行文字要在一個串列裡
word_list = ws(string,sentence_segmentation=True)
print(word_list)
