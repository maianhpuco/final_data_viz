import networkx as nx 
import matplotlib.pyplot as plt
from graph import Graph
from search import search 
from matplotlib.animation import FuncAnimation

def animation_frame(i):
    ax.clear()
    if i <= len(traveled_path):
        nx.draw_networkx(graph, pos = pos) 
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=traveled_path[:i], node_color="red")
        nx.draw_networkx_edges(graph, pos, edgelist = traveled_edges[:i], edge_color="red") 
    else:
        n = i-len(traveled_path)+1
        nx.draw_networkx(graph, pos=pos)
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=shortest_path[:n], node_color="green")
        nx.draw_networkx_edges(graph, pos=pos, edgelist=shorted_path_edges[:n], edge_color="green")



if __name__=='__main__':
    fig, ax = plt.subplots()
    graph = Graph()
    graph.create_random_graph(20, 0.2)
    start = 1 
    end = 10 
    pos = nx.get_node_attributes(graph, "pos")

    traveled_path, traveled_edges, shortest_path, shorted_path_edges, total_cost = search(graph, start, end, "dfs")


    anim = FuncAnimation(
            fig, 
            animation_frame, 
            frames=len(traveled_path)+len(shortest_path), 
            interval = 300, 
            repeat=False 
            )

    plt.show() 

