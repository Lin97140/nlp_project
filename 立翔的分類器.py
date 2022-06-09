from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
import random
from string import printable
from nltk import NaiveBayesClassifier
from nltk import classify
import jieba.posseg

type_list = ["Philosophy","Religions","science","tools","society","history",
             "world_history","literature","art"]

def gen_document(typeList):
    
    a = 0
    documents = []
    fd_list = []
    for dir_file in range(300,501,100):
        type_dir = "data/books/{}/".format(dir_file)
        pcr = PlaintextCorpusReader(root=type_dir, fileids=".*\.txt")
        fd_list += pcr.words()
        c = typeList[a]
        documents += ([(pcr.words(fileid),c) for fileid in pcr.fileids()])
        a += 1
    
    return documents,fd_list

def document_features(document_words,word_features):
    
    document_words = [word for word in document_words if word not in stop_word()]
    document_words = set(document_words)
    #print(document_words)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
        
    return features

def stop_word():
    
    stopwords = []
    with open(file="data/books/fd_stop.txt", mode="r", encoding="UTF-8") as f:
        stop = f.readlines()
        for i in stop[:100]:
            i = i.strip("\n")
            stopwords.append(i)
            
    return stopwords

documents, words_ = gen_document(type_list)
random.shuffle(x=documents)

'''
#num_fir = [word for word in fd1.most_common(n=10) if word not in stopwords]
#num_sec = [word for word in fd2.most_common(n=100) if word not in stopwords and word[0] not in printable]
#print(num_fir)
#print(num_sec)

'''

N_features = 100
all_words = FreqDist(words_)
word_features = list(all_words)[:N_features]

'''
with open (file="data/books/fd_stop"+".txt",mode="w",encoding="utf-8" ) as f:
    for word in word_features:
        f.write(word+"\n")
    f.close()
'''

N_testing = 50
featuresets = [(document_features(d,word_features), c) for (d,c) in documents]
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]


classifier = NaiveBayesClassifier.train(train_set)  

print(classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(5))


while True :
    title = input("輸入書名，輸入-1結束:")
    if title == "-1": 
        break
    title_cut = jieba.lcut(title,cut_all=False)
    print(title_cut)
    class_type = classifier.classify(document_features(title_cut,word_features))
    print(class_type)

print("\n程式結束")

