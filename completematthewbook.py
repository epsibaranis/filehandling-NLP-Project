import pickle
a=['D:/matthew/matthew chapter1.txt','D:/matthew/matthew chapter2.txt','D:/matthew/matthew chapter3.txt','D:/matthew/matthew chapter4.txt',
   'D:/matthew/matthew chapter5i.txt','D:/matthew/matthew chapter6.txt','D:/matthew/matthew chapter7.txt','D:/matthew/matthew chapter8.txt',
   'D:/matthew/matthew chapter9.txt','D:/matthew/matthew chapter10.txt','D:/matthew/matthew chapter11.txt','D:/matthew/matthew chapter12.txt',
   'D:/matthew/matthew chapter13.txt','D:/matthew/matthew chapter14.txt','D:/matthew/matthew chapter15.txt','D:/matthew/matthew chapter16.txt',
   'D:/matthew/matthew chapter17.txt','D:/matthew/matthew chapter18.txt','D:/matthew/matthew chapter19.txt','D:/matthew/matthew chapter20.txt',
   'D:/matthew/matthew chapter21.txt','D:/matthew/matthew chapter22.txt','D:/matthew/matthew chapter23.txt','D:/matthew/matthew chapter24.txt',
   'D:/matthew/matthew chapter25.txt','D:/matthew/matthew chapter26.txt','D:/matthew/matthew chapter27.txt','D:/matthew/matthew chapter28.txt']
z=1
for x1 in a:
  print(x1)
  f1=open(x1,'r')
  d={}
  a={'am','is','was','are','were','have','had','has','have been','has been','had been'}
  b={'a','an','the','A','An','The','such','also',',','.','all','some','These','those','If','from','either','Neither','it?','be','other','not','From','only','with','upon','by','As','able','he','she','it','i','I','you','You'}
  n={'on','up','his','him','her','which','no','or','on','to','for','and','of','in','as','who','with','than','this','that','because','although','eventhough','where as','but','yet','besides','after','if','they','each','enough','many'}
  m=0
  offset={}
  p=0
  for x in f1: 
    m+=1
    l=x.split()
    e=set(l)
    g=e-a
    h=g-b
    i=h-n
    offset[m]=p 
    p=p+len(x)+1
    for y in i:
     o=y.strip('“‘’[(/)],.”;:??><!#')
     if o not in d: 
      d[o]=[m]
     else:
      d[o].append(m)
  print(d)
  print(offset)
  f1.close()
  s=x1.split('/')
  l1=len(s)
  spilit=s[l1-1].split('.')
  #print(spilit)
  s2=spilit[0]+'wordlinenumber'+str(z)+'.txt'
  #print(s2)
  f2=open(s2,'wb')
  pickle.dump(d,f2)
  f2.close()
  s3=spilit[0]+'offsetpointer'+str(z)+'.txt'
  #print(s3)
  f3=open(s3,'wb')
  pickle.dump(offset,f3)
  f3.close()
  z+=1