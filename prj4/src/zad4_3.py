# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 20:27:59
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 20:32:27

# Description
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
	res=1
	for i in range(1, n+1):
		res=res*i
	return res