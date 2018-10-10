# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 20:05:27
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 20:11:04

# Description
# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać. Przykładowy
# prostokąt składający się 2x4 pól ma postać:

# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   | 
# +---+---+---+---+

def squarestr(length, width):
	"""Returns string with square"""
	start="+"
	w=width

	while w != 0:
		start+="---+"
		w-=1
	square=start + "\n"

	for n in range(length):
		k=width
		line1="|"
		line2="+"
		while k != 0:
			line1+="   |"
			line2+="---+"
			k-=1
		square+=line1 + "\n"
		square+=line2 + "\n"
	return square
