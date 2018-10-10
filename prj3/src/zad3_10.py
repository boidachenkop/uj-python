# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-13 21:56:22
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-05 15:37:08


def roman2int():
	Roman={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	rnumber=input("Give roman number: ")
	res = 0
	i = 0
 
	while (i < len(rnumber)):
 
		# Getting value of symbol s[i]
		s1 = Roman[rnumber[i]]
 
		if (i+1 < len(rnumber)):
 
			# Getting value of symbol s[i+1]
			s2 = Roman[rnumber[i+1]]
 
			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:
 
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1
 
	return res

# code from: https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

if __name__ == '__main__':
	print(roman2int())