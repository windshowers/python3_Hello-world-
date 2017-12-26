# -*- coding: utf-8 -*-
def findMaxAndMin(L):
    a=max(L)
    b=min(L)
    for i in L:
        if i >= a:
            Max=i
    for j in L:
        if j <= b:
            Min=j
    return {'Max:':Max,'Min:':Min}
L=eval(input('Please enter a list:'))
print(findMaxAndMin(L))
