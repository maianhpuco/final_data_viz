from queue import PriorityQueue, Queue
import random
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import math
from graph import Graph
from matplotlib.animation import FuncAnimation

def search(graph, start, end, method):
    last_node_id = -1
    travel_path = [] 
    if method == "bfs":
        last_node_id, traveled_path, edges = bfs(graph, start, end)
    if method == "dfs":
        last_node_id, traveled_path, edges = dfs(graph, start, end)
    print(last_node_id)
    shortest_path, shorted_path_edges, cost = construct_path(last_node_id, graph)
    print(shortest_path) 
    return traveled_path, edges,  shortest_path, shorted_path_edges, cost
        


def heuristics_search(graph, cost_function, start_point, goal_point):
    '''
    g : is property of a point, cost so far (actual cost) to get to that point 
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
            return node, closed, edges 
        
        for neighbor in can_see_vertex(node, graph):
            new_cost_g = node.g + point.euclid_distance(node, neighbor) 
            if (neighbor not in closed) or (new_cost_g < node.g):
                neighbor.g = new_cost_g 
                closed.add(neighbor)
                neighbor.parent = node
                priority_score = cost_function(graph, neighbor)
                opened.put((priority_score, neighbor))

    return -1 

def bfs(graph, start_point, goal_point):
    opened = Queue()   
    closed = [] 
    closed.append(start_point)
    opened.put(start_point)
    edges = [] 

    while not opened.empty(): 
        curr_node_id = opened.get()

        if curr_node_id == goal_point:
            return curr_node_id, closed, edges

        for neighbor_id in graph.get_neighbor_node_ids(curr_node_id):
            new_cost = graph.get_node_cost(curr_node_id) \
                    + euclid_distance(
                            graph.get_node_pos(curr_node_id),
                            graph.get_node_pos(neighbor_id)
                            )

            if neighbor_id not in closed or \
                    new_cost<graph.nodes[curr_node_id]['cost_so_far']:
                graph.set_node_cost(neighbor_id, new_cost)
                closed.append(neighbor_id)
                graph.set_node_parent(neighbor_id, curr_node_id) 
                edges.append((curr_node_id, neighbor_id))
                opened.put(neighbor_id)
    return -1 


def dfs(graph, start_point, goal_point):
    opened = []    
    closed = [] 
    closed.append(start_point)
    opened.append(start_point)
    edges = []
    while len(opened)!=0:
        curr_node_id = opened.pop()

        if curr_node_id == goal_point:
            return curr_node_id, closed, edges 

        for neighbor_id in graph.get_neighbor_node_ids(curr_node_id):
            new_cost = graph.get_node_cost(curr_node_id) \
                    + euclid_distance(
                            graph.get_node_pos(curr_node_id),
                            graph.get_node_pos(neighbor_id)
                            )

            if neighbor_id not in closed or \
                    new_cost<graph.nodes[curr_node_id]['cost_so_far']:
                graph.set_node_cost(neighbor_id, new_cost)
                closed.append(neighbor_id)
                graph.set_node_parent(neighbor_id, curr_node_id) 
                edges.append((curr_node_id, neighbor_id))
                opened.append(neighbor_id)
    return -1 


greedy_cost = lambda graph, neighbor: graph.h(neighbor)   
astar_cost = lambda graph, neighbor: graph.h(neighbor) + neighbor.g

def euclid_distance(pos1, pos2):
    return float(
            math.sqrt(
                (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2
                    )
                 )     

def construct_path(node_id, graph):
    result = []
    cost = 0
    edges = [] 
    print(graph.nodes)
    print(":", graph.get_node_parent(node_id))
    print(":", graph.get_node_parent(0))
    while isinstance(node_id, int):
        result.append(node_id)
        cost += graph.get_node_cost(node_id)
        tmp_node_id = graph.get_node_parent(node_id)
        if isinstance(tmp_node_id, int):
            edges.append((node_id, tmp_node_id))
        node_id = tmp_node_id
    return result[::-1], edges[::-1], cost 


if __name__=="__main__": 
    graph = Graph()
    graph.create_random_graph(20, 0.2)
    
    start = 1 
    end = 19

    traveled_path, traveled_edges, shortest_path, shorted_path_edges, total_cost = search(graph, start, end, "dfs")
    print("edges>>>", shorted_path_edges)


    
    fig, ax = plt.subplots()
    pos = nx.get_node_attributes(graph , "pos") 


    def animation_frame(i):
        ax.clear()
        if i <= len(traveled_path):
            nx.draw_networkx(graph, pos = pos) 
            nx.draw_networkx_nodes(graph, pos=pos, nodelist=traveled_path[:i], node_color="red")
            nx.draw_networkx_edges(graph, pos, edgelist = traveled_edges[:i], edge_color="red") 
        else:
            n = i-len(traveled_path)+1
            print(n)
            nx.draw_networkx(graph, pos=pos)
            nx.draw_networkx_nodes(graph, pos=pos, nodelist=shortest_path[:n], node_color="green")
            nx.draw_networkx_edges(graph, pos=pos, edgelist=shorted_path_edges[:n], edge_color="green")


    anim = FuncAnimation(
            fig, 
            animation_frame, 
            frames=len(traveled_path)+len(shortest_path), 
            interval = 300, 
            repeat=False 
            )

    plt.show() 



     
    
