# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-06 17:59:36
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-06 18:12:55

import math

def heron(a, b, c):
	"""Calculating triangle area using Heron formula"""
	if(not (a < b + c and b < c + a and c < a + b)):
		raise ValueError

	s = (a + b + c)/2 # semiperimeter

	return math.sqrt(s * (s - a) * (s - b) * (s - c))

# testing

import unittest

class TestHeron(unittest.TestCase):
	def test_heron(self):
		self.assertEqual(heron(4, 13, 15), 24)
		with self.assertRaises(ValueError):
			heron(5, 1, 2)

if __name__ == '__main__':
	unittest.main()

