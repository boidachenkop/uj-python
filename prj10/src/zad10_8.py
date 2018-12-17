# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-09 13:47:17
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-17 14:21:14

import random
from collections import deque

class QueueEmpty(Exception):
	def __init__(self, val):
		self.val = val

	def __str__(self):
		return str(self.val)

class RandomQueue:

	def __init__(self): 
		self.items = deque();
		self.size = 0;

	def insert(self, item): 
		head_or_tail = random.randint(0, 1);
		if head_or_tail == 1:
			self.items.append(item); #O(1)
		else:
			self.items.appendleft(item); #O(1)
		self.size+=1

	def remove(self):    # zwraca losowy element
		if not self.is_empty():
			head_or_tail = random.randint(0, 1);
			self.size-=1
			if head_or_tail == 1:
				return self.items.pop() #O(1)
			else:
				return self.items.popleft() #O(1)
		else:
			raise QueueEmpty("RandomQueue is empty")


	def is_empty(self): 
		return self.size == 0

	def is_full(self): 
		return False

#testing

import unittest

class RandomQueueTest(unittest.TestCase):
	def setUp(self):
		self.rq0 = RandomQueue()
		self.rq1 = RandomQueue()
		for item in [1, 2, 3, 4]:
			self.rq1.insert(item)

	def testRemove(self):
		self.assertEqual(self.rq1.remove() in [1, 2, 3, 4], True)
		with self.assertRaises(QueueEmpty):
			self.rq0.remove()


if __name__ == '__main__':
	unittest.main()	












