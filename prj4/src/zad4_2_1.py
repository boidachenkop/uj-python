# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-16 20:04:55
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-06 11:55:02

# Description

# Napisać program rysujący "miarkę" o zadanej długości. Należy 
# prawidłowo obsłużyć liczby składające się z kilku cyfr. Należy 
# zbudować pełny string, a potem go wypisać.

import math

def ruler(length):
	marks="|"
	for n in range(length):
		marks+="....|"

	nums=""
	for n in range(length+1):
		nums+=str(n)
		spaces=4 - math.ceil(len(str(n + 1)) // 2)
		nums+=(" " * spaces)
	return marks + '\n' + nums