# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-08-27 22:17:36
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-09-21 20:25:31


from points import Point

class Rectangle:
	"""Representation of rectangle"""

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

	def intersection(self, other):  # intersection of two rectangles
		p1x = max(self.pt1.x, other.pt1.x)
		p1y = max(self.pt1.y, other.pt1.y)
		p2x = min(self.pt2.x, other.pt2.x)
		p2y = min(self.pt2.y, other.pt2.y)
		if(p1x > p2x or p1y > p2y):
			raise ValueError("no intersection between rectangles")
		return Rectangle(p1x, p1y, p2x, p2y)

	def cover(self, other):         # rectangle that covers both
		p1x = min(self.pt1.x, other.pt1.x)
		p1y = min(self.pt1.y, other.pt1.y)
		p2x = max(self.pt2.x, other.pt2.x)
		p2y = max(self.pt2.y, other.pt2.y)
		return Rectangle(p1x, p1y, p2x, p2y)

	def make4(self):                # returns list of four less rectangles
		if(self == Rectangle()):
			raise ValueError("can't divide zero")
		return [Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.x)/2),
				Rectangle((self.pt2.x + self.pt1.x)/2, self.pt1.y, self.pt2.x, (self.pt2.y + self.pt1.y)/2),
				Rectangle(self.pt1.x, (self.pt2.y + self.pt1.y)/2, (self.pt2.x + self.pt1.x)/2, self.pt2.y),
				Rectangle((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2, self.pt2.x, self.pt2.y)]


# testing

import unittest

class TestRectangle(unittest.TestCase): 
	def setUp(self):
		self.rect1 = Rectangle()
		self.rect2 = Rectangle(1, 2, 3, 4)
		self.rect3 = Rectangle(3, 4, 0, -2)
		self.rect4 = Rectangle(1, 2, 4, 5)
		self.rect5 = Rectangle(2, 1, 5, 4)
		self.rect6 = Rectangle(3, 1, 4, 2)
		self.rect7 = Rectangle(1, 1, 4, 4)
		self.rect8 = Rectangle(2, 2, 3, 3)


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

	def test_intersection(self):
		self.assertEqual(self.rect4.intersection(self.rect5), Rectangle(2, 2, 4, 4))
		with self.assertRaises(ValueError) as context:
			self.rect1.intersection(self.rect6)

	def test_cover(self):
		self.assertEqual(self.rect7.cover(self.rect8), self.rect7)
		self.assertEqual(self.rect4.cover(self.rect5), Rectangle(1, 1, 5, 5))

	def test_make4(self):
		self.assertEqual(self.rect7.make4(), [Rectangle(1, 1, 2.5, 2.5), 
			Rectangle(2.5, 1, 4, 2.5), Rectangle(1, 2.5, 2.5, 4), 
			Rectangle(2.5, 2.5, 4, 4)])
		with self.assertRaises(ValueError):
			self.rect1.make4()

if __name__ == '__main__':
	unittest.main()















