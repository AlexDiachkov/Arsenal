# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from random import randint
func=lambda x,y: pow(x, (1/y))
print(func(27,3))




def func1(vse):
    chet=0
    nechet=0
    ed=[]
    prost=[]
    k=0
    
    print(vse)
    print('')
    for j in vse:
        if (j%2!=0):
            nechet=j
            break

    for a in vse:
        if (a%2==0):
            chet=a
    
    for x in vse:
        if (x%10==1):
            ed.append(x)

    for t in vse:
        for f in range(2, t):
            if t % f == 0:
                k = k + 1
        if k == 0:
            prost.append(t)
        else:
            k = 0
        
    return "первое нечетное число=",nechet, "последнее чентое число=",chet,"числа, с окончанием 1:", ed, "САМОЕ СЛОЖНОЕ!!! ПРОСТЫЕ ЧИСЛА:",prost
        
    
el = [randint(1, 1000) for i in range(100)]
    
print(func1(el))