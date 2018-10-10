# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 20:33:22
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 20:39:47

# Description
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz 
# ciągu Fibonacciego.

def fibonacci(n):
	f0=0
	f1=1
	for i in range(n):
		tmp=f1
		f1=f1+f0
		f0=tmp
	return f0
