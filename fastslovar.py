# -*- coding: utf-8 -*-
slovo=input("Введите слово: ")
slovar={}
for i in slovo:
    slovar[i]=slovo.count(i)
print(slovar)

