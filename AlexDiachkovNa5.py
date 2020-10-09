# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
x=[int(random.random()*100000) for i in range(100000)]
y=[]
x.sort()
print(x)
print("min = ", x[0])
print("max = ", x[len(x)-1])
print("max2 = ", x[len(x)-2])
print("max3 = ", x[len(x)-3])
print("max4 = ", x[len(x)-4])
y.append(x[len(x)-1])
y.append(x[len(x)-2])
y.append(x[len(x)-3])
y.append(x[len(x)-4])
print("Новый список из максимальных элементов:",y)
random.shuffle(y)
print("Перемешанный список:", y)
