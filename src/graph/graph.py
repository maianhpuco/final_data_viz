import random
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import math


class Graph(nx.Graph):
    def __init__(self):
        super().__init__()

    def get_number_of_node(self):
        return len(self.nodes)

    def create_random_graph(self, n, p):
        new_graph = nx.gnp_random_graph(n, p, seed=123)
        self.add_nodes_from(new_graph.nodes(data=True))
        self.add_edges_from(new_graph.edges(data=True))
        layout_pos = nx.random_layout(self)

        nx.set_node_attributes(self, layout_pos, "pos")
        nx.set_node_attributes(self, dict([(i, 0 ) for i in range(n)]), "cost_so_far")
        nx.set_node_attributes(self, [], "parent")

     
    def set_node_cost(self,node_id, cost):
        nx.set_node_attributes(self, {node_id: cost}, name = "cost_so_far")

    def get_node_cost(self, node_id):
        cost_so_far = nx.get_node_attributes(self, "cost_so_far")
        return cost_so_far[node_id]

    def set_node_parent(self, node_id, parent):
        nx.set_node_attributes(self, {node_id: parent} , name = "parent")

    def get_node_parent(self, node_id):
        return self.nodes[node_id]["parent"]

    def get_node_pos(self, node_id):
        pos = nx.get_node_attributes(self, "pos")
        return pos[node_id]


    def get_neighbor_node_ids(self, node_id):
        return [i for i in nx.all_neighbors(self, node_id)]
    
