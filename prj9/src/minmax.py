

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

def find_min(node):
	"""Searches min value in single list"""
	if node:
		min = node 
		while node:
			if min.data > node.data:
				min = node
			node = node.next
		return min
	else:
		raise ValueError("Head node is None")

def find_max(node):
	"""Searches max value in single list"""
	if node:
		max = node 
		while node:
			if max.data < node.data:
				max = node
			node = node.next
		return max
	else:
		raise ValueError("Head node is None")

#testing
import unittest

class TestMinMax(unittest.TestCase):
	def setUp(self):
		self.list1 = Node(3, Node(2, Node(0, Node(-1, Node(4, Node(4, Node(7)))))))

	def test_find_min(self):
		self.assertEquals(str(find_min(self.list1)), '-1')

	def test_find_max(self):
		self.assertEquals(str(find_max(self.list1)), '7')

	def test_none(self):
		with self.assertRaises(ValueError):
			find_min(None)


if __name__ == '__main__':
	unittest.main()

