
global final_pos;

final_pos = [0,0]
# Each node represents the board tile for the algorithm 
class Node:
	def __init__(self,pos=[0,0],parent=None,element = None):
		#The tile position in the board
		self.pos = pos
		#Parent node
		self.parent = parent
		#Future Knowledge
		self.h = self.manhattanDistance(self.pos,final_pos)
		#Previous knowledge
		if parent == None:
			self.g = 0
		else:
			self.g = self.parent.g + 1
		#Heuristic Value
		self.f = self.g +self.h
		#Element to wrap
		self.element = element

	# The  Manhattan distance between 2 Nodes
	def  manhattanDistance(self,point1,point2):
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


# The class that implements the path finding algorithm
class PathFinding:
	def __init__(self,board):
		self.board = board
		self.initNode = None # The init Node
		self.endNode = None	 # The goal Node

		self.open = []  # The open list
		self.close = [] # The close list

		self.close.append(self.initNode) # Append the init node

		self.open += [] # Get the init node neighbors 

		while(not self.is_the_goal_in_open_list):
			self.search()


	def search(self):
		self.f_minor()
		self.nextNode = self.close[-1]
		self.nodes = self.vecinos(self.nextNode)
		self.path()

	def is_the_goal_in_open_list(self):
		for i in range(len(self.open)):
			if self.endNode.pos == self.open[i].pos:
				return 1
		return 0

	# Find the node in open with the less f value and put it in on close
	def f_minor(self):
		node = self.open[0]
		n = 0
		for i in range(1, len(self.open)):
			if self.open[i].f < node.f:
				node = self.open[i]
				n = i
		self.cerrada.append(self.abierta[n])
		del self.open[n]

	# Comprove if the node is in the list
	def on_list(self,node,list):
		for i in range(len(list)):
			if node.pos == list[i].pos:
				return 1
		return 0

	def path(self):
		for i in range(len(self.nodes)):
			if self.on_list(self.nodos[i], self.close):
				continue
			elif not self.on_list(self.nodes[i], self.open):
				self.open.append(self.nodes[i])
			else:
				if self.nextNode.g+1 < self.nodes[i].g:
					for j in range(len(self.open)):
						if self.nodes[i].pos == self.open[j].pos:
							del self.open[j]
							self.open.append(self.nodes[i])
							break

	# Return the positions list to the goal
	def final_path(self):
		for i in range(len(self.open)):
			if self.endNode.pos == self.open[i].pos:
				goal = self.open[i]
 
		finalPath = []
		while goal.parent != None:
			finalPath.append(goal.pos)
			goal = goal.parent
		finalPath.reverse()
		return finalPath