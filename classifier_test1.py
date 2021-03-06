from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
import random
import jieba
import jieba.posseg
from nltk import classify, NaiveBayesClassifier

        


dir_class1 = "class10"
pcr_class1 = PlaintextCorpusReader(root=dir_class1, fileids=".*\.txt")

c = "class1"
class1_documents = [(pcr_class1.words(fileid),c) for fileid in pcr_class1.fileids()]


dir_class2 = "class20"
pcr_class2 = PlaintextCorpusReader(root=dir_class2, fileids=".*\.txt")

c = "class2"
class2_documents = [(pcr_class2.words(fileid),c) for fileid in pcr_class2.fileids()]
#print(C_Chat_documents[:9])

dir_class3 = "class30"
pcr_class3 = PlaintextCorpusReader(root=dir_class3, fileids=".*\.txt")
c = "class3"
class3_documents = [(pcr_class3.words(fileid),c) for fileid in pcr_class3.fileids()]

dir_class4= "class40"
pcr_class4 = PlaintextCorpusReader(root=dir_class4, fileids=".*\.txt")
c = "class4"
class4_documents = [(pcr_class4.words(fileid),c) for fileid in pcr_class4.fileids()]


documents = class1_documents + class2_documents + class3_documents + class4_documents 
#print(documents[0])
#print(documents[-1])

random.shuffle(x=documents) # Different results each time?


N_features = 500
all_words = FreqDist(pcr_class1.words() + pcr_class2.words() +pcr_class3.words()+pcr_class4.words())   # 20 seconds...
word_features = list(all_words)[:N_features]


def document_features(document_words, word_features):
    document_words = set(document_words)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


N_testing = 200

featuresets = [(document_features(d, word_features), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]
print("traning class-----")
classifier_class = NaiveBayesClassifier.train(train_set)  
print("class: ", classify.accuracy(classifier_class, test_set))
#print(classifier_class.show_most_informative_features(5))

#????????????

#class1

dir_0 = "class10/stopword0"
pcr_0 = PlaintextCorpusReader(root=dir_0, fileids=".*\.txt")

c = "0"
documents_0 = [(pcr_0.words(fileid),c) for fileid in pcr_0.fileids()]

dir_1 = "class10/stopword1"
pcr_1 = PlaintextCorpusReader(root=dir_1, fileids=".*\.txt")

c = "1"
documents_1 = [(pcr_1.words(fileid),c) for fileid in pcr_1.fileids()]

dir_2 = "class10/stopword2"
pcr_2 = PlaintextCorpusReader(root=dir_2, fileids=".*\.txt")

c = "2"
documents_2 = [(pcr_2.words(fileid),c) for fileid in pcr_2.fileids()]

documents = documents_0 + documents_1 + documents_2
random.shuffle(x=documents) 
#print(documents[0])
#print(documents[-1])


all_words = FreqDist(pcr_0.words() + pcr_1.words() +pcr_2.words())   # 20 seconds...
word_features1 = list(all_words)[:N_features]

featuresets = [(document_features(d, word_features1), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]

print("traning class1-----")
classifier_class1 = NaiveBayesClassifier.train(train_set)
print("class1: ", classify.accuracy(classifier_class1, test_set))
#print(classifier_class1.show_most_informative_features(5))


#class2

dir_3 = "class20/stopword3"
pcr_3 = PlaintextCorpusReader(root=dir_3, fileids=".*\.txt")

c = "3"
documents_3 = [(pcr_3.words(fileid),c) for fileid in pcr_3.fileids()]

dir_4 = "class20/stopword4"
pcr_4 = PlaintextCorpusReader(root=dir_4, fileids=".*\.txt")

c = "4"
documents_4 = [(pcr_4.words(fileid),c) for fileid in pcr_4.fileids()]

documents = documents_4 + documents_3
random.shuffle(x=documents) 


#print(documents[0])
#print(documents[-1])

all_words = FreqDist(pcr_3.words() + pcr_4.words())   # 20 seconds...
word_features2 = list(all_words)[:N_features]


featuresets = [(document_features(d, word_features2), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]

print("traning class2-----")
classifier_class2 = NaiveBayesClassifier.train(train_set)  
print("class2: ", classify.accuracy(classifier_class2, test_set))
#print(classifier_class2.show_most_informative_features(5))

#class3

dir_5 = "class30/stopword5"
pcr_5 = PlaintextCorpusReader(root=dir_5, fileids=".*\.txt")

c = "5"
documents_5 = [(pcr_5.words(fileid),c) for fileid in pcr_5.fileids()]

dir_6 = "class30/stopword6"
pcr_6 = PlaintextCorpusReader(root=dir_6, fileids=".*\.txt")

c = "6"
documents_6 = [(pcr_6.words(fileid),c) for fileid in pcr_6.fileids()]

dir_7 = "class30/stopword7"
pcr_7 = PlaintextCorpusReader(root=dir_7, fileids=".*\.txt")

c = "7"
documents_7 = [(pcr_7.words(fileid),c) for fileid in pcr_7.fileids()]

documents = documents_5 + documents_6 + documents_7
random.shuffle(x=documents) 
#print(documents[0])
#print(documents[-1])


all_words = FreqDist(pcr_5.words() + pcr_6.words() +pcr_7.words())   # 20 seconds...
word_features3 = list(all_words)[:N_features]

featuresets = [(document_features(d, word_features3), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]

print("traning class3-----")
classifier_class3 = NaiveBayesClassifier.train(train_set)
print("class3: ", classify.accuracy(classifier_class3, test_set))
#print(classifier_class3.show_most_informative_features(5))

#class4

dir_8 = "class40/stopword8"
pcr_8 = PlaintextCorpusReader(root=dir_8, fileids=".*\.txt")

c = "8"
documents_8 = [(pcr_8.words(fileid),c) for fileid in pcr_8.fileids()]

dir_9 = "class40/stopword9"
pcr_9 = PlaintextCorpusReader(root=dir_9, fileids=".*\.txt")

c = "9"
documents_9 = [(pcr_9.words(fileid),c) for fileid in pcr_9.fileids()]

documents = documents_8 + documents_9
random.shuffle(x=documents) 
#print(documents[0])
#print(documents[-1])

all_words = FreqDist(pcr_8.words() + pcr_9.words())   # 20 seconds...
word_features4 = list(all_words)[:N_features]


featuresets = [(document_features(d, word_features4), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]


print("traning class4----")
classifier_class4 = NaiveBayesClassifier.train(train_set)  
print("class4:", classify.accuracy(classifier_class4, test_set))
#print(classifier_class4.show_most_informative_features(5))

'''
def classifier_total():
    a, b, c, d, e = classifier_class, classifier_class1, classifier_class2, classifier_class3, classifier_class4
    return a, b, c, d, e

def word_features_total():
    a, b, c, d, e = word_features, word_features1, word_features2, word_features3, word_features4
    return a, b, c, d, e
'''

#input
type_list = ["nr", "nrt", "vg", "g", "x", "p", "q", "c","ng", "df", "b","eng","r","c", "uj", "zg", "m", "d", "a", "k", "y","nz", "u","ud","uj", "uv", "ug", "ul", "uz", "nrfg", "o", "x", "f", "yg", "j", "i", "zg", "tg", "z", "l", "ag", "h"]
while True:
    title = input("????????????:")
    if title == "0":
        break
    t_cut = jieba.posseg.cut(title)
    title_list = [(word, pos) for word, pos in t_cut]
    title_cut = []
    for word, pos in title_list:
        if pos not in type_list:
            title_cut.append(word)
            
    class_type = classifier_class.classify(document_features(title_cut, word_features))
    if class_type == "class1":
        result = classifier_class1.classify(document_features(title_cut, word_features1))
    elif class_type == "class2":
        result = classifier_class2.classify(document_features(title_cut, word_features2))
    elif class_type == "class3":
        result = classifier_class3.classify(document_features(title_cut, word_features3))
    else:
        result = classifier_class4.classify(document_features(title_cut, word_features4))
        
    print("result: %s" %result)
    
    
    
    
    