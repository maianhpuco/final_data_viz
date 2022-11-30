from queue import PriorityQueue, Queue
import random
from collections import defaultdict
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import math
from viz_graph.graph import Graph
#from viz_graph.graph import Graph
from matplotlib.animation import FuncAnimation
import copy 


def search(graph, start, end, method):
    greedy_cost = lambda graph, nei, curr, end: heuristic_cost(
            graph.get_node_pos(nei),
            graph.get_node_pos(end))   
    astar_cost  = lambda graph, nei, curr, end: heuristic_cost(
            graph.get_node_pos(nei), 
            graph.get_node_pos(end)) \
                    + euclid_distance(graph.get_node_pos(curr), graph.get_node_pos(nei))
    
    last_node_id = -1
    travel_path = [] 
    if method == "bfs":
        last_node_id, traveled_path, edges, traveled_dict, queues= bfs(graph, start, end)
    if method == "dfs":
        last_node_id, traveled_path, edges , traveled_dict, queues= dfs(graph, start, end)
    if method == "gbfs":
        last_node_id, traveled_path, edges, traveled_dict, queues = heuristics_search(
                graph, 
                greedy_cost,
                start, 
                end
                )
    if method == "astar":
        last_node_id, traveled_path, edges, traveled_dict, queues = heuristics_search(
                graph, 
                astar_cost,
                start, 
                end
                )

    shortest_path, shorted_path_edges, cost = construct_path(last_node_id, graph)
    
    return traveled_path,traveled_dict,  edges,  shortest_path, shorted_path_edges, cost, queues
        
    


def heuristics_search(graph, cost_function, start_point, goal_point):
    '''
    g : is property of a point, cost so far (actual cost) to get to that point 
    '''
    
    opened = PriorityQueue()
    graph.set_node_cost(start_point, 0)
    opened.put((0, start_point))
     
    
    closed = []         
    closed.append(start_point)
    
    edges = []
    count = 0
    
    traveled_dict = defaultdict(list)
    queues=[[node for score, node in list(copy.copy(opened).queue)]]
    

    while not opened.empty():
        cost, curr_node_id = opened.get()
        traveled_dict[curr_node_id] = [] 
        queues.append([node for score, node in list(copy.copy(opened).queue)])
        if curr_node_id == goal_point:
            return curr_node_id, closed, edges, traveled_dict, queues[1:] 
        
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
                priority_score = cost_function(graph, neighbor_id, curr_node_id, goal_point)
                opened.put((priority_score, neighbor_id))
                traveled_dict[curr_node_id].append(neighbor_id)
                queues.append([node for score, node in list(copy.copy(opened).queue)])    
    return -1 

def bfs(graph, start_point, goal_point):
    opened = Queue()   
    closed = [] 
    closed.append(start_point)
    opened.put(start_point)
    edges = [] 

    traveled_dict = defaultdict(list)
    queues=[list(copy.copy(opened).queue)]

    while not opened.empty(): 
        curr_node_id = opened.get()
        queues.append(list(copy.copy(opened).queue))

        traveled_dict[curr_node_id] = [] 
        if curr_node_id == goal_point:
            return curr_node_id, closed, edges, traveled_dict, queues[1:]

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
                traveled_dict[curr_node_id].append(neighbor_id)
                queues.append(list(copy.copy(opened).queue))

    return -1 



def dfs(graph, start_point, goal_point):
    opened = []    
    closed = [] 
    closed.append(start_point)
    opened.append(start_point)
    edges = []

    traveled_dict = defaultdict(list)

    queues=[opened]
    while len(opened)!=0:
        curr_node_id = opened.pop()
        traveled_dict[curr_node_id] = [] 
        queues.append(opened)

        if curr_node_id == goal_point:
            return curr_node_id, closed, edges, traveled_dict, queues[1:]

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
                traveled_dict[curr_node_id].append(neighbor_id)
                queues.append(opened)
    return -1 


def euclid_distance(pos1, pos2):
    return float(
            math.sqrt(
                (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2
                    )
                 )     

def heuristic_cost(pos, end_pos):
    return euclid_distance(pos, end_pos)


def construct_path(node_id, graph):
    result = []
    cost = 0
    edges = [] 
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
    

