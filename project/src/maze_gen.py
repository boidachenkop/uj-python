# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-12-23 15:18:12
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-12-24 17:32:08

from PIL import Image
import numpy as np 
import random

# RGB colors 
RGB = {'white': [255, 255, 255], 'red': [255, 0, 0],
'black': [0, 0, 0], 'green': [0, 255, 0]}


class WallCell:
	# if type=1 this object will be interpreted as wall
	# if type=0 this object will be interpreted as cell 
	def __init__(self, type, ID=None):
		self.id = ID
		self.type = type
		self.row = None
		self.col = None

	def setRowCol(self, row, col):
		self.row = row 
		self.col = col

	def getRowCol(self):
		return [self.row, self.col]

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
		self.maze = []		# binary matrix where 1 - wall, 0 - cell
		self.walls = [] 	# list of walls
		self.sets = []		# at the begining every cell have it's own set
		self.frames = [] 	# list of images for animation
		for col in range(self.width):
			self.maze.append([])
			for row in range(self.height):
				if (col == 0 or col == self.width-1 or 
				row == self.height-1 or row == 0) or (col%2 == 0 and
				row%2 == 0): # borders
					self.maze[col].append(WallCell(1))
				elif (col-1)%2==0 and (row-1)%2==0: # cells
					self.maze[col].append(WallCell(0, id))
					self.sets.append([id])
					id+=1
				else: # walls
					wall = WallCell(1)
					wall.setRowCol(row, col)
					self.maze[col].append(wall)	
					self.walls.append(wall)

	def inDiffSets(self, cell1, cell2):
		# returns True id cells are in different sets
		id1 = cell1.getId()
		id2 = cell2.getId()
		for item in self.sets:
			if id1 in item and not id2 in item:
				return True 
		return False 

	def mergeCellSets(self, cell1, cell2):
		# merge cell sets
		id1 = cell1.getId()
		id2 = cell2.getId()
		id1set = id2set = []
		for item in self.sets:
			if id1 in item:
				id1set = item
			elif id2 in item:
				id2set = item
		id1set+=id2set
		self.sets.remove(id2set)

	def getWallNeighbourCells(self, wall):
		# returns cells that dividet by wall
		row, col = wall.getRowCol()
		neighbours = []
		if self.maze[row][col+1].getType() == 0:
			neighbours.append(self.maze[row][col+1])
		if self.maze[row][col-1].getType() == 0: 
			neighbours.append(self.maze[row][col-1])
		if self.maze[row+1][col].getType() == 0: 
			neighbours.append(self.maze[row+1][col])
		if self.maze[row-1][col].getType() == 0: 
			neighbours.append(self.maze[row-1][col])
		return neighbours

	def genMaze(self):
		# generuj labirynt
		while(len(self.walls) != 0):
			curr = random.choice(self.walls)
			self.walls.remove(curr)
			nb1, nb2 = self.getWallNeighbourCells(curr)
			if self.inDiffSets(nb1, nb2):
				curr.removeWall()
				self.mergeCellSets(nb1, nb2)
				self.frames.append(self.getImage())

	def getImage(self):
		# interprets maze as image
		imageMtrx = np.zeros((self.height, self.width, 3), dtype=np.uint8)
		for col in range(self.width):
			for row in range(self.height):
				if(self.maze[row][col].getType() == 1):
					imageMtrx[row][col] = RGB['black']
				else:
					imageMtrx[row][col] = RGB['white']
		img = Image.fromarray(imageMtrx, 'RGB')
		img = img.resize((300, 300), Image.NEAREST)
		return img

	def saveMaze(self, name):
		self.getImage().save(name)

	def makeAnimation(self, name):
		# makes gif from frames
		self.frames[0].save(name,
               save_all=True,
               append_images=self.frames[1:],
               duration=100,
               loop=0)

if __name__ == '__main__':
	m = Maze(63)
	m.genMaze()
	m.saveMaze("output.png")
	m.makeAnimation('anim.gif');

