
stopword = []
with open(file="stopword2.txt", mode="r", encoding="UTF-8") as f:
    stop = f.readlines()
    for i in stop:
        i = i.strip("\n")
        stopword.append(i)

stop = []
for n in range(200, 301):
    with open(file="400/400_test/file"+str(n)+".txt", mode="r", encoding="UTF-8") as file:
        title = file.readlines()
        with open(file="stopword400/testfile"+str(n-5)+".txt", mode="w", encoding="UTF-8") as f2:    
            for t in title:
                for k in t:
                    if k not in stopword:
                        f2.write(k)
            
        