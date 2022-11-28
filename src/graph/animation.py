import networkx as nx 
import matplotlib.pyplot as plt 
#from search import gbfs, bfs, dfs, astar 
#TODO 
#input file 

g = nx.Graph()

def read_input():
    pass 
fig, ax = plt.subplots()

def animate(weighed_edges):
    G = nx.Graph()
    G.add_weighted_edges_from(weighted_edges)
    nx.draw(G)


if __name__=='__main__':
    weighted_edges = [(0, 1, 3), (1, 2, 7.5)]
    animate(weighted_edges)
    #nx.draw(g)
    plt.show()

