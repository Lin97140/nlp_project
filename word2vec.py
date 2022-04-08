# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:42:05 2022

@author: lisha
"""

import urllib
from string import printable
 
file = urllib.request.urlopen(url="https://github.com/stopwords-iso/stopwords-zh/blob/master/stopwords-zh.txt")
stopwords = file.read().decode("utf8").split()

from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist

dir_ = "data/carrefour/"
pcr = PlaintextCorpusReader(dir_, fileids=".*\.txt")
fd = FreqDist(pcr.words())
text = [word for word,fd in fd.most_common(n=100) if word not in stopwords and word[0] not in printable]
print(text)

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences

corpus = PathLineSentences(dir_)
mode = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
print(mode.wv.most_similar(positive=["現金","回饋"], negative=["折扣"]))