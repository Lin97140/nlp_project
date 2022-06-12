import tkinter as tk
import pickle
import jieba.posseg


win = tk.Tk()
win.title("中文圖書分類器")
win.geometry("500x300")
win.resizable(0, 0)

with open('my_classifier.pickle', 'rb') as f:
    classifier_class = pickle.load(f)
with open('my_classifier1.pickle', 'rb') as f1:
    classifier_class1 = pickle.load(f1)
with open('my_classifier2.pickle', 'rb') as f2:
    classifier_class2 = pickle.load(f2)
with open('my_classifier3.pickle', 'rb') as f3:
    classifier_class3 = pickle.load(f3)
with open('my_classifier4.pickle', 'rb') as f4:
    classifier_class4 = pickle.load(f4)

with open('word_features.pickle', 'rb') as f:
    word_features = pickle.load(f)
with open('word_features1.pickle', 'rb') as f1:
    word_features1 = pickle.load(f1)
with open('word_features2.pickle', 'rb') as f2:
    word_features2 = pickle.load(f2)
with open('word_features3.pickle', 'rb') as f3:
    word_features3 = pickle.load(f3)
with open('word_features4.pickle', 'rb') as f4:
    word_features4 = pickle.load(f4)
   
def document_features(document_words, word_features):
    document_words = set(document_words)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features



type_list = ["nr", "nrt", "vg", "g", "x", "p", "q", "c","ng", "df", "b","eng","r","c", "uj", "zg", "m", "d", "k", "y","nz", "u","ud","uj", "uv", "ug", "ul", "uz", "nrfg", "o", "x", "f", "yg", "j", "i", "zg", "tg", "z", "l", "ag", "h"]
name_list = ["孫文", "蔣經國", "蔣介石","蔣中正", "介石", "中正","中山", "蔣"]
res = {'0':'000 總類', '1':'100 哲學類', '2':'200 宗教類', '3':'300 科學類', '4':'400 應用科學類', '5':'500 社會科學類', '6':'600 中國史地類', '7':'700 世界史地類', '8':'800 語言文學類', '9':'900 藝術類'}
def run():
    if entry.get() != "":
        title = str(entry.get())
        t_cut = jieba.posseg.cut(title)
        title_list = [(word, pos) for word, pos in t_cut]
        title_cut = []
        for word, pos in title_list:
            if pos == 'nr' and word in name_list:
                title_cut.append(word)
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
        
    
        label2.configure(text="類別: "+res[result])
def delete():
    entry.delete("0", "end")
    label2.configure(text="類別: ")    
        

entry = tk.Entry(win, width=44)
entry.place(x=85, y=110)
label1 = tk.Label(win, text="輸入書名")
label1.place(x=20, y=110)
button = tk.Button(win, text="確認", padx=10, pady=5, command=run)
button.place(x=300, y=130)
button2 = tk.Button(win, text="清除", padx=10, pady=5, command=delete)
button2.place(x=360, y=130)

label2 = tk.Label(win, text="類別: ")
label2.place(x=100, y= 140)




win.mainloop()