# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-19 16:17:57
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-19 19:15:57

def getDigit(num, ndig):
	# returns digit on ndig position in num
	# getDigit(123, 1) == 3 
	strnum = list(str(num))
	strnum.reverse()
	try:
		return int(strnum[ndig-1])
	except IndexError:
		return 0

def radixsort(array, base):
	# Złożoność obliczeniowa O(w+N)
	# sortować można tylko dane typu int(lub podobne)
	# stabilny	
	queues = [] 
	for i in range(10):
		queues.append([])
	i=1
	digit = 1
	while base/i>=1:
		for j in range(len(array)):
			queues[getDigit(array[j], digit)].append(array[j])
		digit+=1
		k=0
		for j in range(10):
			while len(queues[j]) != 0:
				n=queues[j].pop(0)
				array[k]=n
				k+=1
		i*=10

import unittest
import lists_to_sort

class RadixSortTest(unittest.TestCase):
	def setUp(self):
		self.arr1 = lists_to_sort.unsorted(100)
		self.arr2 = self.arr1[:] # copy

	def test1(self):
		radixsort(self.arr1, 100)
		self.arr1copy.sort()
		self.assertEquals(self.arr1 == self.arr1copy, True)


if __name__ == '__main__':
	unittest.main()