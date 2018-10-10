# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 20:42:55
# @Last Modified by:   pavlo
# @Last Modified time: 2018-08-16 21:11:33

# Description
# Napisać funkcję odwracanie(L, left, right) odwracającą 
# kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję 
# iteracyjną i rekurencyjną.

def odwracanie_iter(L, left, right):
	it=(right - left) // 2
	for i in range(it):
		L[left], L[right] = L[right], L[left] # swap
		left+=1
		right-=1

# >>> L=[x for x in range(11)]
# >>> odwracanie_iter(L, 2, 7)
# >>> L
# [0, 1, 7, 6, 4, 5, 3, 2, 8, 9, 10]

def odwracanie_rekt(L, left, right):
	if left+1 != right and left != right:
		L[left], L[right] = L[right], L[left]
		odwracanie_rekt(L, left+1, right-1)

# >>> L=[x for x in range(11)]
# >>> odwracanie_rekt(L, 2, 7)
# >>> L
# [0, 1, 7, 6, 4, 5, 3, 2, 8, 9, 10]