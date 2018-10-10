# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-09-21 20:22:29
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-09-30 21:41:08

from points import Point

class Circle:
	"""Class represents circle"""

	def __init__(self, x=0, y=0, radius=1):
		if radius < 0:
			raise ValueError("negative radius")
		self.pt = Point(x, y)
		self.radius = radius

	def __repr__(self):            # "Circle(x, y, radius)"
		return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

	def __eq__(self, other):
		return self.pt == other.pt and self.radius == other.radius

	def __ne__(self, other):
		return not self == other

	def area(self): 	           # pole powierzchni
		import math
		return math.pi*self.radius**2

	def move(self, x, y):          # przesuniecie o (x, y)
		self.pt += Point(x, y)

	def cover(self, other):        # circle that covers both
		import math
		center = Point((self.pt.x + other.pt.x)/2, (self.pt.y + other.pt.y)/2)
		base_radius = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)/2
		add_radius = max(self.radius, other.radius)
		return Circle(center.x, center.y, base_radius + add_radius)

	def p_inside(self, point):     # check if point inside the circle
		return (point.x - self.pt.x)**2 + (point.y - self.pt.y)**2 <= self.radius**2


# testing

import unittest

class TestCircle(unittest.TestCase):
	def setUp(self):
		self.c1 = Circle(1, 1, 1)
		self.c2 = Circle(1, 2, 1)
		self.c3 = Circle(4, 4, 2)
		self.p1 = Point(4, 4)
		self.p2 = Point(1, 1)

	def test_repr(self):
		self.assertEqual(self.c1.__repr__(), "Circle(1, 1, 1)") 

	def test_area(self):
		import math
		self.assertEqual(self.c1.area(), math.pi)

	def test_move(self):
		self.c1.move(1, 1)
		self.assertTrue(self.c1 == Circle(2, 2, 1))

	def test_cover(self):
		import math
		self.assertEquals(self.c2.cover(self.c3), Circle(2.5, 3, math.sqrt(13)/2 + 2))	# sqrt((4 - 1)**2 + (4 - 2)**2)	

	def test_p_inside(self):
		self.assertTrue(not self.c1.p_inside(self.p1))
		self.assertTrue(self.c1.p_inside(self.p2))


if __name__ == '__main__':
	unittest.main()
















