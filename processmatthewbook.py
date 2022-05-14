import pickle
a=['D:/matthew/matthew chapter1.txt','D:/matthew/matthew chapter2.txt','D:/matthew/matthew chapter3.txt','D:/matthew/matthew chapter4.txt',
   'D:/matthew/matthew chapter5i.txt','D:/matthew/matthew chapter6.txt','D:/matthew/matthew chapter7.txt','D:/matthew/matthew chapter8.txt',
   'D:/matthew/matthew chapter9.txt','D:/matthew/matthew chapter10.txt','D:/matthew/matthew chapter11.txt','D:/matthew/matthew chapter12.txt',
   'D:/matthew/matthew chapter13.txt','D:/matthew/matthew chapter14.txt','D:/matthew/matthew chapter15.txt','D:/matthew/matthew chapter16.txt',
   'D:/matthew/matthew chapter17.txt','D:/matthew/matthew chapter18.txt','D:/matthew/matthew chapter19.txt','D:/matthew/matthew chapter20.txt',
   'D:/matthew/matthew chapter21.txt','D:/matthew/matthew chapter22.txt','D:/matthew/matthew chapter23.txt','D:/matthew/matthew chapter24.txt',
   'D:/matthew/matthew chapter25.txt','D:/matthew/matthew chapter26.txt','D:/matthew/matthew chapter27.txt','D:/matthew/matthew chapter28.txt']

word=input('word=?')
while(word!='not'):
 z=1
 for x1 in a:
    f=open(x1,'r')
    s=x1.split('/')
    l1=len(s)
    spilit=s[l1-1].split('.')
    s1=spilit[0]+'wordlinenumber'+str(z)+'.txt'
    f1=open(s1,'rb')
    s2=spilit[0]+'offsetpointer'+str(z)+'.txt'
    f2=open(s2,'rb')
    dictionary=pickle.load(f1)
    dictionary1=pickle.load(f2)
    keys=dictionary.keys()
    if word in keys:
     for c in dictionary[word]:
        f.seek(dictionary1[c])
        print(f.readline())
    z+=1
 if word not in keys:
     print('the word not in matthew chapter book')
 word=input('word=?')