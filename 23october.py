import random


slovar={}
file=open('zadan.txt','w')
spisok = [int(random.random()*1000) for i in range(1000)]
spisok.sort()
for i in spisok:
   if i+4<=len(spisok):
       if (spisok[i+3]>=58)&(spisok[i+4]<=500):
           slovar[spisok[i+3]]=spisok[i+4]
print (slovar)
file.close()




