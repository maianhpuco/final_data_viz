from queue import PriorityQueue, Queue
#from graph import Graph, Point, Edge
import random
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt


def search(graph, cost_function, start_point, goal_point):
    '''
    g : is property of a Point, cost so far (actual cost) to get to that point 
    '''
    opened = PriorityQueue()
    start_point.g = 0
    opened.put((start_point.g + cost_function(graph, start), start_point))
    
    closed = set()
    closed.add(start_point)
    
    count = 0
    while not opened.empty():
        g, node = opened.get()

        if node == goal_point:
            return node 
        
        for neighbor in can_see_vertex(node, graph):
            new_cost_g = node.g + Point.euclid_distance(node, neighbor) 
            if (neighbor not in closed) or (new_cost_g < node.g):
                neighbor.g = new_cost_g 
                closed.add(neighbor)
                neighbor.parent = node
                priority_score = cost_function(graph, neighbor)
                opened.put((priority_score, neighbor))

    return -1   

def bfs(graph, start_point, goal_point):
    opened = Queue()
    closed = set()
    closed.add(start_point)
    opened.put(start_point)
    
    while not opened.empty():
        node = opened.get()

        if node == goal_point:
            return node

        for neighbor in can_see_vertex(node, graph):
            new_cost = node.g +  Point.euclid_distance(node, neighbor) 

            if neighbor not in closed or new_cost < node.g: 
                neighbor.g = new_cost
                closed.add(neighbor)
                neighbor.parent = node 
                opened.put(neighbor)
    return -1

def dfs(graph, start_point, goal_point):
    opened = []    
    closed = set()
    closed.add(start_point)
    opened.append(start_point)
    
    while len(opened)!=0:
        node = opened.pop()

        if node == goal_point:
            return node

        for neighbor in can_see_vertex(node, graph):
            new_cost = node.g +  Point.euclid_distance(node, neighbor) 

            if neighbor not in closed or new_cost < node.g: 
                neighbor.g = new_cost
                closed.add(neighbor)
                neighbor.parent = node 
                opened.append(neighbor)
    return -1


greedy_cost = lambda graph, neighbor: graph.h(neighbor)   
astar_cost = lambda graph, neighbor: graph.h(neighbor) + neighbor.g

def euclid_distance(A, B):
    pass 
    

def traceback(last_node):
    result = []
    cost = 0
    while last_node:
        result.append(last_node)
        cost += last_node.g 
        last_node = last_node.parent
    return result[::-1], cost



#def adding_nodes(positions, G):
#    for idx, pos in enumerate(positions):
#        G.add_node(idx,pos=pos)
        

#def adding_edges(edges, G):
#    for edge in edges:
#        G.add_edge(edge[0], edge[1])

    

class Graph(nx.Graph):
    def __init__(self, n, p):
        super().__init__()
        self.graph = None

    def create_random_graph(self, n, p):
        self.graph = nx.create_random_graph(n, p)

    def set_node_cost(node_index, cost):
        G.nodes[node_index]["current_cost"] = cost


if __name__=="__main__": 
    def randomNodes(n, seed=123, width=999, height=666):
        random.seed((n, seed))
        return [(random.randint(1, width), 
                    random.randint(1, height))
    #               for i in range(n)
                ]

    def randomEdges(
            n, 
            max_num_edges_per_node=None, 
            seed=123
            ):
        edges = []
        for node in range(n):
            num_adjnc = random.randint(1, max_num_edges_per_node)
            adjnc_nodes = np.random.randint(n-1, size=num_adjnc)
            edges.extend([(node, i) for i in adjnc_nodes if i!=node])
        return edges 
        
    n = 10
    coors = randomNodes(n)
    
    edges = randomEdges(n, n-4) 
    print(edges)

    #adding_nodes(coors, g) 
    #adding_edges(edges, g)
    #positions = nx.get_node_attributes(g, 'pos')
    #nx.draw(g, positions)
    #plt.show()
 
    g = nx.gnp_random_graph(n, p=0.5)
    nx.draw(g)
    plt.show()
    

   
