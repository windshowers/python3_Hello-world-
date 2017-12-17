# -*- coding: utf-8 -*-
def trim(s):
    while s[:1] ==' ':
        s=s[1:]
    while s[-1] ==' ':
        s=s[:-1]
    print(s)
s=str(input('Please enter a string:'))
trim(s)
