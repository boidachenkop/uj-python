# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko 
# @Date:   2018-08-13 16:01:28
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-04 21:00:11


while True:
	try:
		width=int(input("Give width: "))
		length=int(input("Give length: "))
		break
	except ValueError:
		print("Intiger value is required!")

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

print(square)










