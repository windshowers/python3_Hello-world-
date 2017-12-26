# -*- coding: utf-8 -*-
height=input('Please enter your height(unit:m):')
weight=input('Please enter your weight(unit:kg):')
s1=float(height)
s2=float(weight)
bmi=s2/s1**2
if bmi <= 18.5:
	print('Too thin')
elif bmi >= 18.5 and bmi <= 25:
	print('It\'s normal')
elif bmi >= 25 and bmi <= 28:
	print('Too weight')
elif bmi > 28 and bmi < 32:
	print('Fat')
elif bmi >= 32:
	print('Too fat')
	pass
