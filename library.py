import requests as req
from bs4 import BeautifulSoup
from time import sleep
import jieba
import random 
headers = {"content-type": "text/html; charset=UTF-8","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
file_count =881

for i in range(90, 101, 5):
    if i == 1:
        h = ""
    else:
        h = str(i)
    print(f"{i}:")
    url2="https://sierra.lib.ntust.edu.tw/search~S2*cht?/l2/l2/m"+h+"1%2C3410%2C3909%2CB/browse/indexsort=-"
    url3 = "https://sierra.lib.ntust.edu.tw/search~S2*cht?/l3/l3/"+h+"1%2C8842%2C10000%2CB/browse/indexsort=-"
    url4 = "https://sierra.lib.ntust.edu.tw/search~S2*cht?/l4/l4/"+h+"1%2C9309%2C10000%2CB/browse/indexsort=-"
    url5 = "https://sierra.lib.ntust.edu.tw/search~S2*cht?/l5/l5/"+h+"1%2C7789%2C10000%2CB/browse/indexsort=-"
    re = req.get(url=url2, headers = headers)
    soup = BeautifulSoup(re.text, "html.parser")
    results = soup.find_all("td", class_="browseEntryData")
    for r in results:
        r2 = r.find_all("a")
        href = r2[-1]["href"]
        url2 = "https://sierra.lib.ntust.edu.tw" + href
        re2 = req.get(url=url2, headers=headers)
        soup2 = BeautifulSoup(re2.text, "html.parser")
        result = soup2.find("span", class_="briefcitTitle")
        if result == None:
            title = soup2.find("strong").text
        else:
            title = result.text
        title_cut = jieba.cut(title)
        print(file_count)
        with open(file="200/2file"+str(file_count)+".txt", mode="w", encoding="UTF-8") as file:
            file.write(" ".join(title_cut))
            file_count+=1
        if file_count % 5 == 0:        
            sleep(random.randint(2, 5))
        
   # https://sierra.lib.ntust.edu.tw/search~S2*cht?/l5/l5/251%2C7789%2C10000%2CB/browse/indexsort=-
    #https://sierra.lib.ntust.edu.tw/search~S2*cht?/l1/l1/1%2C7998%2C10000%2CB/browse/indexsort=-

