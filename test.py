import requests as re
from bs4 import BeautifulSoup as Bs
import time
import random
import jieba
headers = {"content-type": "text/html; charset=UTF-8","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
n = 51
file_count = 469
for i in range(n, 117):
    print(i)
    if i == 1:
        url = "https://goodlife.tw/%E5%92%96%E5%95%A1%E5%BA%97/%E6%98%9F%E5%B7%B4%E5%85%8B"
    else:
        url = "https://goodlife.tw/%E5%92%96%E5%95%A1%E5%BA%97/%E6%98%9F%E5%B7%B4%E5%85%8B/page/" +str(i)
    res = re.get(url, headers = headers)
    soup = Bs(res.text, "html.parser")
    result = soup.find_all("li", class_="topic expired")
    for r in result:
        if r.find("a"):
            href = r.find("a")["href"]
            title = r.find("a").text
            
            url = href
            res2 = re.get(url, headers = headers)
            soup2 = Bs(res2.text, "html.parser")
            if soup2.find("div", class_="article"):    
                text = soup2.find("div", class_="article")
            with open(file="data\\starbucks\\starbucks"+str(file_count)+".txt", mode="w", encoding="UTF-8") as file:
                text_cut = jieba.cut(text.text)
                file.write(title+'\n')
                file.write(" ".join(text_cut))
                file_count += 1
    if i % 5 == 0:
        time.sleep(random.randint(2,5))
        