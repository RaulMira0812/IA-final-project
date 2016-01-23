import networkx as nx
import pygraphviz as pgv # pygraphviz should be available
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge('a','aa')
G.add_edge('a','ab')
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
plt.show()