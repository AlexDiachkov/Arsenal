# -*- coding: utf-8 -*-
slovo=input("Введите слово: ")
slovar={}
for i in slovo:
    if i not in slovar:
        slovar[i]=1
    else:
        slovar[i]=slovar[i]+1
print(slovar)

