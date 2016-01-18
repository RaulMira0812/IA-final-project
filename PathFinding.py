

# Each node represents the board tile for the algorithm
class Node:
	def __init__(self,pos=[0,0],element = None,parent=None,final_pos = [0,0]):
		#The tile position in the board
		self.pos = pos
		#Parent node
		self.parent = parent
		#Future Knowledge
		self.h = self.manhattanDistance(self.pos,final_pos)#The distance to the goal
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
	def __init__(self,board=None,initPos=[0,0],goalPos=[0,0]):
		self.board = board
		# The init Node
		self.initNode = Node(pos=initPos,element=board[initPos[0]][initPos[1]],final_pos=goalPos)
		# The goal Node
		self.endNode = Node(pos=goalPos,element=board[goalPos[0]][goalPos[1]],final_pos=goalPos)
		  # The open list
		self.open = []
		# The close list
		self.close = []
		# Append the init node
		self.close.append(self.initNode)
		# Get the init node neighbors
		self.open += self.getNeighborsList(self.initNode)

		#self.is_the_goal_in_open_list()
		while not self.is_the_goal_in_open_list():
			self.search()
		self.goalPath = self.final_path()
		

	def search(self):
		self.f_minor()
		self.nextNode = self.close[-1]
		self.nodes = self.getNeighborsList(self.nextNode)
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
		self.close.append(self.open[n])
		del self.open[n]

	# Comprove if the node is in the list
	def on_list(self,node,list):
		for i in range(len(list)):
			if node.pos == list[i].pos:
				return 1
		return 0

	def path(self):
		for i in range(len(self.nodes)):
			if self.on_list(self.nodes[i], self.close):
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
			#print self.endNode.pos,self.open[i].pos
			if self.endNode.pos == self.open[i].pos:
				goal = self.open[i]
 				
		finalPath = []
		while goal.parent != None:
			finalPath.append(goal.pos)
			goal = goal.parent
		finalPath.reverse()
		return finalPath

	# Return the neighbors nodes from a node
	def getNeighborsList(self,node):
		lNeig = []
		x = node.pos[0]
		y = node.pos[1]
		for i in range(3):
			for j in range(3):
				new_x = x - 1 + i
				new_y = y - 1 + j
				if new_x >= 0 and new_x < 10 and new_y >= 0 and new_y < 20:
					if self.board[new_x][new_y].getType() != 0 or (self.board[new_x][new_y].getType() == 1 and self.board[new_x][new_y].getOccupied != 0):
						if new_x != x or new_y != y:
							newNode = Node(pos=[new_x,new_y],element=self.board[new_x][new_y],parent=node,final_pos=self.endNode.pos)
							lNeig.append(newNode)
							#print ((str(x - 1 + i) + ":" + str(y - 1 + j)))
		return lNeig