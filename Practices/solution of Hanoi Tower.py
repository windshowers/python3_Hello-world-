# -*- coding: utf-8 -*-
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
n=int(input('Please enter the num of your dishes:'))
print('move solution:')
move(n,'A','B','C')
