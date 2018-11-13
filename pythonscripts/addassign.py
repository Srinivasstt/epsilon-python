addr=" no 75, karle town center, bangalore 560024 8556748575"
print(addr)
words=addr.split()
print(words)

#print(help(addr.split()))

for word in words:
        word=word.strip(",./t")
        if word.isnumeric():
                if(len(word)== 6):
                        print("pincode found:",word)
                elif(len(word)== 10):
                        print("mobile Number:",word)




