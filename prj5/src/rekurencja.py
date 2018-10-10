# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-25 11:06:00
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-25 11:47:09



def factorial(n):
	res=1
	for i in range(1, n+1):
		res=res*i
	return res

def fibonacci(n):
	f0=0
	f1=1
	for i in range(n):
		tmp=f1
		f1=f1+f0
		f0=tmp
	return f0

