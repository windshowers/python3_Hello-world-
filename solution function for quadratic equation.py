# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
	s=b*b-4*a*c
	x3=('方程无解')
	if s>0:
		x1=-b+math.sqrt(s)/2/a
		x2=-b-math.sqrt(s)/2/a
		print('方程有两根，分别为：',x1,x2)
		return (x1,x2)
	elif s==0:
		x=-b/2/a
		print('方程有一根为x=',x)
		return x
	else:
		return x3
a=float(input('输入二次项系数：'))
b=float(input('输入一次项系数：'))
c=float(input('输入常系数：'))
if a==0:
	print('二次项系数不能为0，请重新输入。')
else:
	print(quadratic(a,b,c))
