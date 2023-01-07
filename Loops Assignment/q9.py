wordlist=[]
t='y'
while t=='y':
    nextword=input("Enter a word: ")
    wordlist.append(nextword)
    t=input("Do you want to enter another word(y/n)")
print(wordlist)
wordset=[*set(wordlist)]
for i in wordset:
    print(i,"occurs",wordlist.count(i),"times")
