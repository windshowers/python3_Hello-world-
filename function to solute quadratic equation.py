# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
	s=b*b-4*a*c
	if s>0:
		x1=-b+math.sqrt(s)/2/a
		x2=-b-math.sqrt(s)/2/a
		print('方程有两根，分别为：x1=%.2f,x2=%.2f。'%(x1,x2))
		return (x1,x2)
	elif s==0:
		x=-b/2/a
		print('方程有一根，为x=%.2f。'%x)
	else:
		print('方程无解。')
a=float(input('输入二次项系数：'))
b=float(input('输入一次项系数：'))
c=float(input('输入常数项系数：'))
if a==0:
	print('二次项系数不能为0，请重新输入。')
else:
	quadratic(a,b,c)
