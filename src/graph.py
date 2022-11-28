from collections import defaultdict
import networkx as nx;


def generate_random_graph(n:int, p:float):
    """
    n : number of nodes,
    p : probability
    """
    G = nx.gnp_random_graph(n, p);
    return G

