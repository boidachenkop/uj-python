# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-09-26 12:37:18
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-09-26 16:10:06


def solve1(a, b, c):
	"""Solves linear equasion with to variebles a * x + b * y + c = 0"""

	if a == 0 and b == 0 and c != 0:
		raise ValueError(str(c)+" is not 0")

	if a == 0 and b != 0:
		print("y = "+str(-c/b))
		return

	if a != 0 and b == 0:
		print("x = "+str(-c/a))
		return

	if a != 0 and b != 0:
		print("Solution is every pair (r, (-"+str(a)+"r - "+str(c)+")/"+str(b))

# testing

import unittest
import sys
import io

class TestLinear(unittest.TestCase):
	def test1(self):                                 # a = 0, b = 0, c != 0
		with self.assertRaises(ValueError):
			solve1(0, 0, 1)

	def test2(self):                                 # a = 0, b != 0
		capturedOutput = io.StringIO()               # Create StringIO object
		sys.stdout = capturedOutput                  #  and redirect stdout.
		solve1(0, 4, 2)
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "y = -0.5\n")

	def test3(self):                                 # a != 0, b = 0
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		solve1(4, 0, 2)
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "x = -0.5\n")

	def test4(self):                                 # a != 0, b != 0
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		solve1(1, 2, 3)
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Solution is every pair (r, (-1r - 3)/2\n")


if __name__ == '__main__':
	unittest.main()








