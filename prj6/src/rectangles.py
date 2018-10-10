# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-27 22:17:36
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-08-27 22:56:40


from points import Point

class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie."""

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):              # "[(x1, y1), (x2, y2)]"
		return "[{0}, {1}]".format(self.pt1, self.pt2)

	def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
		return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, 
			self.pt1.y, self.pt2.x, self.pt2.y)

	def __eq__(self, other):       # rect1 == rect2
		return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

	def __ne__(self, other):        # rect1 != rect2
		return not self == other

	def center(self):               # center of rectangle
		return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

	def area(self):                 # area
		return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

	def move(self, x, y):           # move rectangle for (x, y)
		self.pt1 = self.pt1 + Point(x, y)
		self.pt2 = self.pt2 + Point(x, y)



# testing

import unittest

class TestRectangle(unittest.TestCase): 
	def setUp(self):
		self.rect1 = Rectangle()
		self.rect2 = Rectangle(1, 2, 3, 4)
		self.rect3 = Rectangle(3, 4, 0, -2)

	def test_str(self):
		self.assertEqual(self.rect2.__str__(), "[(1, 2), (3, 4)]")	

	def test_repr(self):
		self.assertEqual(self.rect2.__repr__(), "Rectangle(1, 2, 3, 4)")

	def test_eq(self):
		self.assertEqual(self.rect2 == self.rect2, True)
		self.assertEqual(self.rect2 == self.rect1, False)

	def test_center(self):
		self.assertEqual(self.rect1.center(), Point())
		self.assertEqual(self.rect2.center(), Point(2, 3))

	def test_area(self):
		self.assertEqual(self.rect1.area(), 0)
		self.assertEqual(self.rect2.area(), 4)
		self.assertEqual(self.rect3.area(), 18)

	def test_move(self):
		self.rect1.move(2, 1)
		self.rect2.move(2, 1)
		self.assertEqual(self.rect1, Rectangle(2, 1, 2, 1))
		self.assertEqual(self.rect2, Rectangle(3, 3, 5, 5))


if __name__ == '__main__':
	unittest.main()















