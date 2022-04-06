# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:04:07 2022

@author: lisha
"""

import requests
from bs4 import BeautifulSoup
import jieba.posseg
import time

n = 2
file_number = 1
for i in range(1,n+1):
    URL = "https://goodlife.tw/%E9%87%8F%E8%B2%A9%E5%BA%97/%E5%AE%B6%E6%A8%82%E7%A6%8F/page/"+str(i)
    print(URL)
    r = requests.get(URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_topic = soup.find_all("li",class_="topic expired")

    for topic in tag_topic:
        if topic.find("a"):
            href = topic.find("a")["href"]
            title = topic.find("a").text
        
            url = href
            r2 = requests.get(url,cookies={"over18":"1"})
            soup2 = BeautifulSoup(r2.text,"lxml")
            articles = soup2.find("div",class_="article")
            with open(file="data/carrefour/"+"carrefour"+str(file_number)+".txt", mode="w", encoding="utf-8") as file1:
                text_cut = jieba.posseg.cut(articles.text)
                words = [word for word,pos in text_cut]
                file1.write(title+"\n")
                file1.write(" ".join(words))
                file_number += 1
        
            



