# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-26 13:46:50
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-06 17:12:21

import operator 

def mk_len_equal(poly1, poly2):
	"""Makes length of polys equal. Adds '0' to smaler poly"""
	lesser = list(poly2 if len(poly1) > len(poly2) else poly1)
	bigger = list(poly2 if len(poly1) < len(poly2) else poly1)
	zeroes = abs(len(poly1) - len(poly2))
	if zeroes != 0:
		lesser.extend([0 for x in range(zeroes)])
	if bigger == poly1: # want to save order of returned polynominals 
		return [bigger, lesser]
	else:
		return [lesser, bigger]

def add_poly(poly1, poly2):
	poly=mk_len_equal(poly1, poly2)
	return [x for x in map(operator.add, poly[0], poly[1])]

def sub_poly(poly1, poly2):
	poly=mk_len_equal(poly1, poly2)
	return [x for x in map(operator.sub, poly[0], poly[1])]

def mul_poly(poly1, poly2):
	result=[0 for x in range(len(poly1)+len(poly2)-1)]
	for i in range(len(poly1)):
		for j in range(len(poly2)):
			result[i+j]+=poly1[i]*poly2[j]
	return result

def is_zero(poly):
	for x in poly:
		if x != 0:
			return False
	return True

def cmp_poly(poly1, poly2):
	return True if poly1 == poly2 else False

def eval_poly(poly, x0):
	b0 = poly[-1]
	for i in range(-2, -(len(poly)+1), -1):
		b1 = poly[i] + b0*x0
		b0 = b1
	return b0

def combine_poly(poly1, poly2):
	result = [poly1[-1]]
	for i in range(len(poly1)-2, -1, -1):
		result = add_poly(mul_poly(result, poly2), [poly1[i]])
	return result

def pow_poly(poly, n):
	result = poly
	for i in range(n-1):
		result = mul_poly(poly, result)
	return result

def diff_poly(poly):
	result = [0]*len(poly)
	for i in range(len(poly)):
		result[i] = i*poly[i]
	result.pop(0)
	return result


import unittest

class TestPolynominals(unittest.TestCase):
	def setUp(self):
		self.p1 = [0, 1]      # W(x) = x
		self.p2 = [0, 0, 1]   # W(x) = x*x
		self.p3 = [1, 2, 3]   # W(x) = 1 + 2*x + 3*x*x
		self.p4 = [4, 5]      # W(x) = 4 + 5*x
		self.p5 = [3, 3, 2]
		self.p6 = [2, 3, 4, 1]
		self.res1 = [17, 33, 62, 59, 44, 16, 2] # Wolfram Mathematica
		self.res2 = [27, 81, 135, 135, 90, 36, 8]

	def test_add_poly(self):
		self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
		self.assertEqual(add_poly(self.p3, self.p4), [5, 7, 3])

	def test_sub_poly(self):
		self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])
		self.assertEqual(sub_poly(self.p4, self.p3), [3, 3, -3])

	def test_mul_poly(self):
		self.assertEqual(mul_poly(self.p3, self.p4), [4, 13, 22, 15])
		self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

	def test_is_zero(self):
		self.assertEqual(is_zero([0, 0, 1, 0, 0, 0]), False)
		self.assertEqual(is_zero([0, 0, 0, 0, 0, 0]), True)

	def test_eval_poly(self):
		self.assertEqual(eval_poly(self.p1, 4), 4)
		self.assertEqual(eval_poly(self.p3, 4), 57)

	def test_cmp_poly(self):
		self.assertEqual(cmp_poly(self.p1, self.p1), True)
		self.assertEqual(cmp_poly(self.p1, self.p2), False)

	def test_combine_poly(self):
		self.assertEqual(combine_poly(self.p5, self.p6), self.res1)

	def test_pow_poly(self):
		self.assertEqual(pow_poly(self.p5, 3), self.res2)

	def test_diff_poly(self):
		self.assertEqual(diff_poly(self.p2), [0, 2])
		self.assertEqual(diff_poly(self.p6), [3, 8, 3])

if __name__ == '__main__':
	unittest.main()


















