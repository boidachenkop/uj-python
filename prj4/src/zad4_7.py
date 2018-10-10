# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 21:25:39
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 21:29:49

# Description
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać 
# się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do 
# nieograniczonej głębokości. Napisać funkcję flatten(sequence), 
# która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element
# jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
	result=[]
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result+=flatten(item)
		else:
			result.append(item)
	return result
	
# >>> from zad4_7 import flatten
# >>> L=[[1,[2]], [3],[4,[5,6]]]
# >>> flatten(L)
# [1, 2, 3, 4, 5, 6]