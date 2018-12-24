# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-23 15:18:12
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-24 13:09:56

from PIL import Image
import numpy as np 
import random

RGB = {'white': [255, 255, 255], 'red': [255, 0, 0],
'black': [0, 0, 0], 'green': [0, 255, 0]}


class WallCell:
	def __init__(self, type, ID=0):
		self.id = ID
		self.type = type
		self.set = [self.id]

	def getId(self):
		return self.id

	def removeWall(self):
		if self.type == 1:
			self.type = 0
		else:
			raise Exception("Not a wall")

	def getType(self):
		return self.type

class Maze:
	def __init__(self, size):
		self.height = self.width = size
		id = 0
		# generate grid
		self.maze = []
		self.walls = []
		for col in range(self.width):
			self.maze.append([])
			for row in range(self.height):
				if ((col == 0) or col == self.width-1 or 
				row == self.height-1 or row == 0) or (col%2 == 0 and
				row%2 == 0): # borders
					self.maze[col].append(WallCell(1))
				elif (col-1)%2==0 and (row-1)%2==0: # cells
					self.maze[col].append(WallCell(0, id))
					id+=1
				else: # walls
					wall = WallCell(1)
					self.maze[col].append(wall)	
					self.walls.append(wall)

	def getWallNeighbourCells(self, col, row):


	def genMaze(self):
		while(len(self.walls) != 0):
			curr = random.choice(self.walls)
			self.walls.remove(curr)


	def saveMaze(self, name):
		imageMtrx = np.zeros((self.height, self.width, 3), dtype=np.uint8)
		for col in range(self.width):
			for row in range(self.height):
				if(self.maze[row][col].getType() == 1):
					imageMtrx[row][col] = RGB['black']
				else:
					imageMtrx[row][col] = RGB['white']
		Image.fromarray(imageMtrx, 'RGB').save(name)

if __name__ == '__main__':
	m = Maze(13)
	m.saveMaze("output.png")

