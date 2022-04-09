import requests as re
from bs4 import BeautifulSoup as Bs
import time
import random
import jieba
headers = {"content-type": "text/html; charset=UTF-8","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
n = 117
file_count = 1


#從goodlife.tw抓資料
for i in range(1, n+1): #從第一頁到第117頁
    print(i)
    if i == 1:
        url = "https://goodlife.tw/%E5%92%96%E5%95%A1%E5%BA%97/%E6%98%9F%E5%B7%B4%E5%85%8B"
    else:
        url = "https://goodlife.tw/%E5%92%96%E5%95%A1%E5%BA%97/%E6%98%9F%E5%B7%B4%E5%85%8B/page/" +str(i) #每一頁的網址
    res = re.get(url, headers = headers)
    soup = Bs(res.text, "html.parser")
    result = soup.find_all("li", class_="topic expired") #抓每個標題
    
    for r in result:
        if r.find("a"):
            href = r.find("a")["href"]  #抓每個標題的連結
            title = r.find("a").text    #抓標題文字
            
            url = href
            res2 = re.get(url, headers = headers)
            soup2 = Bs(res2.text, "html.parser")
            if soup2.find("div", class_="article"):    
                text = soup2.find("div", class_="article") #抓每個標題的內容
            with open(file="data\\starbucks\\starbucks"+str(file_count)+".txt", mode="w", encoding="UTF-8") as file: #將標題和內容寫入文字檔
                text_cut = jieba.cut(text.text)
                file.write(title+'\n')
                file.write(" ".join(text_cut))
                file_count += 1
    if i % 5 == 0:
        time.sleep(random.randint(2,5)) #每五頁暫停2~5秒
        
