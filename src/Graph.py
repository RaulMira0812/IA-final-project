import networkx as nx
import pygraphviz as pgv # pygraphviz should be available
import matplotlib.pyplot as plt

class CustomTree:

	def __init__(self,root = None,leafs =[], filen = None):
		#Variable that contains the tree levels
		self.levels = [{'root':root,'leafs':leafs}]
		self.Graph = self.newGraph(root,leafs)
		self.filen=filen
	
	def newGraph(self,root = None,leafs =[]):
		G = nx.DiGraph()
		for leaf in leafs:
			G.add_edge(root,leaf)
		return G

	def addLevels(self,root = None,leafs =[]):
		for leaf in leafs:
			self.Graph.add_edge(root,leaf)

	def draw(self):
		A = nx.to_agraph(self.Graph)
		A.add_subgraph([root],rank='same')
		for level in self.levels:
			A.add_subgraph(level,rank='same')

		A.draw(self.filen, prog='dot')


root = "[0,0]"
levels = ["[1,1]","[2,3]","[3,4]"]

# = CustomTree(root = root,leafs=levels)
#a.addLevels(root = "[2,3]",leafs=["[5,6]","[7,8]"])
#a.addLevels(root = "[7,8]",leafs=["[9,10]","[11,12]","[3,44]"])
#a.draw()

"""G.add_edge('a','ab')
G.add_edge('a','bbc')
G.add_edge('b','ab')
G.add_edge('b','bb')
G.add_edge('c','bbc')
G.add_edge('bb','bba')
G.add_edge('bb','bbc')

A = nx.to_agraph(G)
one = A.add_subgraph(['a','b','c'],rank='same')
two = A.add_subgraph(['aa','ab','bb'],rank='same')
three = A.add_subgraph(['bba','bbc'],rank='same')

A.draw('example.png', prog='dot')
plt.show()"""