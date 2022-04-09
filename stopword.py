from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
from string import printable

stopword = []
with open(file="data/stopword2.txt", mode='r', encoding="UTF-8") as f: #讀取stopword表
    stop = f.readlines()

for i in stop:
    i = i.strip('\n') #去除每行後的換行符號
    stopword.append(i) #加入stopword 串列
stop = []

    
#分析出現頻率
n = 300 
source1 = "data/carrefour"  
source2 = "data/lifemoney"
p1 = PlaintextCorpusReader(source1, fileids = ".*\.txt")
f1 = FreqDist(samples=p1.words())

common1 = [word for word, freq in f1.most_common(n) if word not in stopword] #找前300個詞去除頻率後加入common1
common = []

#去除數字
for ele in common1:
    try:
        int(ele) 
    except:
        common.append(ele)
common = [i for i in common if not i.encode("UTF-8").isalpha() and not i.encode("UTF-8").isalnum()]
#去除英文字串和包含英文加數字的字串

print(common)


        
