# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 21:16:04
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 21:27:55

# Description
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb
# zawartych w sekwencji, która może zawierać zagnieżdżone 
# podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a 
# sprawdzanie, czy element jest sekwencją, wykonać przez i
# sinstance(item, (list, tuple)).

def sum_seq(sequence):
	result=0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result+=sum_seq(item)
		else:
			result+=item
	return result

# >>> from zad4_6 import sum_seq
# >>> L=[[1,[2]], [3],[4,[5,6]]]
# >>> L
# [[1, [2]], [3], [4, [5, 6]]]
# >>> sum_seq(L)
# 21