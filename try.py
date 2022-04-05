# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:04:07 2022

@author: lisha
"""

import requests
from bs4 import BeautifulSoup

articles = []
r = requests.get("https://goodlife.tw/", cookies={"over18":"1"})
soup = BeautifulSoup(r.text, "lxml")
tag_main = soup.find_all(id = "main")
for tag in tag_main:
    list_ = tag.find_all("li",class_="")
    for li in list_:
        hrefs = li.find_all("a")
        for href in hrefs:
            print(href.get("href"))
            print(href.string)

import jieba.posseg
# https://www.costco.com.tw/c/hot-buys?page=1
URL = "https://goodlife.tw/"


