from matplotlib.animation import FuncAnimation 
from matplotlib import pyplot as plt
import numpy as np
from graph import DFS
import networkx as nx
from matplotlib.animation import FuncAnimation 

def animate_search(graph, start, end):

    # Graph search algorithm
    history = [];
    path_found, path = DFS(graph, start, end, history);

    # Number of frame to animate:
    if path_found:
        N = len(history) + len(path);
    else:
        N = len(history);

    # Visualization parth    
    fig, ax = plt.subplots();

    # Node position on figure
    pos = nx.spring_layout(graph,
            seed= 0,
            iterations = 100);

    def hist2txt(hist):
        return f"""+ visited : ...{hist["visited"][-5:]}
+ frontier : ...{hist["frontier"][-5:]}
+ current : {hist["current_node"]}"""


    def update(i):
        if i < len(history):
            hist = history[i];

            # Update graph
            ax.cla()
            draw_graph(graph,
                    pos,
                    ax,
                    start, end,
                    visited = hist["visited"],
                    frontier = hist["frontier"],
                    current_node = hist["current_node"]
                    )
            ax.text(
                    0, 0, hist2txt(hist),
                    horizontalalignment='left',
                    verticalalignment='center',
                    )
        else:
            i = i - len(history);
            u, v = path[i], path[i+1];

            nx.draw_networkx_edges(graph,
                    pos,
                    edgelist = [(u, v)],
                    ax = ax,
                    alpha = .5,
                    width = 2,
                    edge_color = "tab:green")


    
    anim = FuncAnimation(fig, update,
            init_func = lambda: draw_graph(graph, pos, ax, start, end),
            frames = N-1,
            interval = 250)

    return anim

    


def draw_graph(graph,
        pos,
        ax,
        start, end,
        visited = [],
        frontier = [],
        current_node = None):
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
    start_cfg = {"node_size": 200, "node_color":"tab:green"}
    end_cfg = {"node_size": 200, "node_color":"tab:green"}
    visited_cfg = {"node_size": 200, "node_color":"tab:blue"}
    frontier_cfg = {"node_size": 200, "node_color":"tab:purple"}
    current_cfg = {"node_size": 300, "node_color":"tab:orange"}

    # list of all nodes
    nodes = graph.nodes();

    # Compute current node
    common_nodes = set(nodes) \
            - set([start,end]) \
            - set(visited) \
            - set(frontier) \
            - set([current_node])
    
    if current_node:
        visited = set(visited) - set([current_node])

    frontier = set(frontier) - set(visited)

    # Draw commons node
    nx.draw_networkx_nodes(graph, 
            pos = pos,
            nodelist = common_nodes, 
            **commons,
            **default
            )

    # Draw start & end node
    nx.draw_networkx_nodes(graph,
            pos = pos,
            nodelist = [start],
            **commons,
            **start_cfg)
    
    # Draw start & end node
    nx.draw_networkx_nodes(graph,
            pos = pos,
            nodelist = [end],
            **commons,
            **end_cfg)

    # Draw visited
    nx.draw_networkx_nodes(graph,
            pos = pos,
            nodelist = visited,
            **commons,
            **visited_cfg)
    
    # Draw frontier
    nx.draw_networkx_nodes(graph,
            pos = pos,
            nodelist = frontier,
            **commons,
            **frontier_cfg)
    
    # Draw current
    if current_node:
        nx.draw_networkx_nodes(graph,
                pos = pos,
                nodelist = [current_node],
                **commons,
                **current_cfg)

    # Draw label
    nx.draw_networkx_labels(graph,
            font_size = 5,
            font_color = "black",
            pos = pos)

