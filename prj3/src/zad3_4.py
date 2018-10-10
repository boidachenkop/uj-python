# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-13 15:33:43
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-04 20:57:59

while True:
	x=input("x: ")
	if x == "stop":
		break
	try:
		print(float(x) ** 3)
	except ValueError:
		print("x is not a number")

