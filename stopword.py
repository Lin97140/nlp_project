from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
from string import printable

stopword = []
with open(file="data/stopword2.txt", mode='r', encoding="UTF-8") as f:
    stop = f.readlines()

for i in stop:
    i = i.strip('\n')
    stopword.append(i)
stop = []

    
n = 300
source1 = "data/carrefour"
source2 = "data/lifemoney"
p1 = PlaintextCorpusReader(source1, fileids = ".*\.txt")
f1 = FreqDist(samples=p1.words())

common1 = [word for word, freq in f1.most_common(n) if word not in stopword]
common = []

for ele in common1:
    try:
        int(ele) 
    except:
        common.append(ele)
common = [i for i in common if not i.encode("UTF-8").isalpha() and not i.encode("UTF-8").isalnum()]

print(common)


        
