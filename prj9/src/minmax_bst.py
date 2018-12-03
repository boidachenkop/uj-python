# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-03 13:10:32
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-03 13:26:27

class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)

def bst_max(top):
	if top:
		max = top
		while max.right:
			max = max.right 
		return max
	else:
		raise ValueError("Top node is None")

def bst_min(top):
	if top:
		min = top
		while min.left:
			min = min.left
		return min
	else:
		raise ValueError("Top node is None")

#testing
import unittest

class TestMinMaxBST(unittest.TestCase):
	def setUp(self):
		self.root = Node(6)
		self.root.left = Node(4)
		self.root.right = Node(8)
		self.root.left.left = Node(3)
		self.root.left.right = Node(5)
		self.root.right.left = Node(6)
		self.root.right.right = Node(9)
		# |        6
		# |      /   \
		# |    4       8
		# |   / \     / \
		# |  3   5   6   9

	def test_min(self):
		self.assertEquals(str(bst_min(self.root)), '3')

	def test_max(self):
		self.assertEquals(str(bst_max(self.root)), '9')

	def test_none(self):
		with self.assertRaises(ValueError):
			bst_max(None)


if __name__ == '__main__':
	unittest.main()







