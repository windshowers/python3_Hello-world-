# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize()
L1=str(input('Please enter a name list:'))
L2=L1.split()
L3=list(map(normalize,L2))
print(L3)
