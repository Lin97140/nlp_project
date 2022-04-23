# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:04:07 2022

@author: lisha
"""

import requests
from bs4 import BeautifulSoup
import jieba.posseg
import time

n = 1

def library_scraping(url):
    
    articles = []
    for i in range(1,n+1):
        r = requests.get(url=URL, cookies={"over18":"1"})
        soup = BeautifulSoup(r.text, "lxml")
        tag_topic = soup.find_all("td",class_="browseEntryData")
    
        for topic in tag_topic:
            if topic.find("a"):
                tag1 = topic.find("a")
                href = tag1.find_next_sibling("a")["href"]
                num = tag1.find_next_sibling("a").text
            
                url = "https://sierra.lib.ntust.edu.tw"+href
                r2 = requests.get(url,cookies={"over18":"1"})
                soup2 = BeautifulSoup(r2.text,"lxml")
                title_=soup2.find("strong")
            
                articles.append({"name":title_.text,"number":num})
    
    return articles

for i in range(100,191,10):
    a = 1
    print(i)
    for k in range(0,3):
        URL = "https://sierra.lib.ntust.edu.tw/search~S2*cht?/l{}/l{}/{}%2C136%2C152%2CB/browse/indexsort=-".format(i,i,a)
        print(URL)
        articles = library_scraping(URL)
    
        for article in articles:
            with open(file="data/books/"+"book"+article["number"]+".txt", mode="w", encoding="utf-8") as file1:
                tagged_words = jieba.cut(article["name"])
                file1.write(" ".join(tagged_words))        

        a += 50
    
        if k == 2:
            time.sleep(3)


