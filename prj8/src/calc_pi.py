# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-09-26 16:10:27
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-09-30 22:19:51

import random
import math
from points import Point
from circles import Circle
from rectangles import Rectangle


def get_random_point(S):
	"""gives random point in square S"""
	x = random.uniform(S.pt1.x, S.pt2.y)
	y = random.uniform(S.pt1.y, S.pt2.y)
	return Point(x, y)


def calc_pi(n=1000000):
	"""Calculation pi using Monte Carlo method
	n - number of random points"""
	C = Circle(0, 0, 0.5)
	S = Rectangle(-0.5, -0.5, 0.5, 0.5)
	PointInCircle, PointInSquare = 0, 0 
	for i in range(n):
		point = get_random_point(S)
		PointInSquare += 1
		if C.p_inside(point):
			PointInCircle += 1
	return 4 * PointInCircle/PointInSquare

# testing

import unittest

class TestCalcPi(unittest.TestCase):
	def test(self):
		self.assertAlmostEquals(calc_pi(2000000), math.pi, 2)


if __name__ == '__main__':
	unittest.main()










