# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-08 17:33:32
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-08 17:56:22

class QueueEmpty(Exception):
	def __init__(self, val):
		self.val = val

	def __str__(self):
		return str(self.val)

class QueueFull(Exception):
	def __init__(self, val):
		self.val = val

	def __str__(self):
		return str(self.val)

class Queue:
	def __init__(self, capacity):
		self.capacity = capacity 
		self.items = []
		self.size = 0    	

	def __str__(self):             # podglądanie kolejki
		return str(self.items)

	def is_empty(self):
		return not self.items

	def is_full(self):             # nigdy nie jest pusta
		return self.size == self.capacity

	def put(self, data):
		if self.is_full():
			raise QueueFull("Queue is full")
		else:
			self.items.append(data)
			self.size+=1

	def get(self):
		if self.is_empty():
			raise QueueEmpty("Queue is empty")
		else:
			self.size-=1
			return self.items.pop(0)   # mało wydajne!

#testing
import unittest

class QueueTest(unittest.TestCase):
	def setUp(self):
		self.q1 = Queue(2)
		self.q2 = Queue(4)
		for item in [1, 2, 3]:
			self.q2.put(item)

	def testPut(self):
		self.q2.put(4)
		self.assertEqual(str(self.q2), '[1, 2, 3, 4]')
		with self.assertRaises(QueueFull):
			self.q2.put(5)

	def testGet(self):
		self.assertEqual(self.q2.get(), 1)
		with self.assertRaises(QueueEmpty):
			self.q1.get()


if __name__ == '__main__':
	unittest.main()










