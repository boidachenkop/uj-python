# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko 
# @Date:   2018-08-13 15:33:49
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-04 20:58:10

import math

while True:
	try:
		length=int(input("Give ruler length: "))
		break
	except ValueError:
		print("Wrong length!")

print("|", end="")
for n in range(length):
	print("....", end="|")
print("")

for n in range(length+1):
	print(str(n), end="")
	spaces=4 - math.ceil(len(str(n + 1)) // 2)
	print(" "*spaces, end="")
print("")			
