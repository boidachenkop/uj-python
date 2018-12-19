# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-19 14:14:12
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-19 15:08:41

import random
import math
import numpy

def unsorted(N):
	data = list(range(N))
	res = random.sample(data, N)
	return res

def almost_sorted(N):
	# swaps two elements 
	data = list(range(N))
	a, b = 0, 0
	while a == b:
		a = random.randint(0, N-1)
		b = random.randint(0, N-1)	
	data[a], data[b] = data[b], data[a]
	return data

def almost_sorted_reverse(N):
	data = almost_sorted(N)
	data.reverse()
	return data

def gaussian_float(N):
	data = []
	for i in range(N):
		data.append(numpy.random.normal())
	return data

def unsorted_repeat(N):
	data = list(range(N))*2
	res = random.sample(data, N)
	return res