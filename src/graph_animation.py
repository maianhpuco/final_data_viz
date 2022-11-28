from matplotlib.animation import FuncAnimation 
from matplotlib import pyplot as plt
import numpy as np
from graph import DFS
import networkx as nx
from matplotlib.animation import FuncAnimation 

def animate_search(graph, start, end):
    history = [];
    path_found, path = DFS(graph, start, end, history);
    
    fig, ax = plt.subplots();


    def update(i):
        hist = history[i];
        # print(hist);


    anim = FuncAnimation(fig, update,
            init_func = lambda: draw_graph(graph, fig, ax),
            frames = len(history),
            interval = 100)

    return anim

    



def draw_graph(graph, fig, ax):
    # layout:
    pos = nx.spring_layout(graph,
            seed= 0,
            iterations = 100);

    # Draw edge
    nx.draw_networkx_edges(graph,
            pos = pos,
            edge_color = "#AAAAAA",
            style = "dashed",
            width = .5,
            alpha = .5,
            ax = ax)

    # Node options
    commons = {"alpha": .5}
    default = {"node_size": 100, "node_color":"tab:gray"}

    # Draw node
    nx.draw_networkx_nodes(graph, 
            pos = pos,
            **commons,
            **default
            )

    # Draw label
    nx.draw_networkx_labels(graph,
            font_size = 5,
            font_color = "black",
            pos = pos)

