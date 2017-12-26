# -*-coding: utf-8 -*-
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
YangHui=triangles()
a=int(input('Please enter the number you wanna get:'))
for n in range(a):
    print(next(YangHui))
