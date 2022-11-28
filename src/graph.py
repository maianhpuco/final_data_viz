from collections import defaultdict
import networkx as nx
from queue import Queue


def generate_random_graph(n:int, p:float):
    """
    n : number of nodes,
    p : probability
    """
    G = nx.gnp_random_graph(n, p);
    # G = nx.connected_caveman_graph(20, 5)
    return G


def DFS(graph, start, end, history):
    """
    seqs : 
        sequence of data to be visualized
        history = [history_i]
            history_i {
                visited: [],
                frontier: [],
                parents: {},
                current_node: int
            }
    """

    visited = [];
    # frontier = Queue();
    frontier = list();

    # Adding start to visited
    visited.append(start);
    frontier.append(start);
    # frontier.put(start);

    # Tracking parent nodes
    parents = dict();
    parents[start] = None;

    # Terminating condition
    path_found = False;
    

    # Track if path found
    while True:
        if len(frontier) == 0:
            break;

        # pop a elem from queue frontier
        current_node = frontier.pop();

        if current_node == end:
            path_found = True;
            break;

        for node in graph[current_node]:
            if node not in visited:
                frontier.append(node);
                
                parents[node]=current_node;

                # Construct history object to visualize
                _hist = {
                    "visited": visited.copy(),
                    "frontier": frontier.copy(),
                    # "parents" : parents.copy(),
                    "current_node": current_node,
                    "new_frontier": node
                }
                visited.append(node);
                history.append(_hist);
    #construct_path;
    path = [];
    if path_found:
        path.append(end);

        while parents[end] is not None:
            path.append(parents[end]);
            end = parents[end];

        path.reverse();

    return path_found, path;


if __name__ == "__main__":
    G = generate_random_graph(30, .25);
    G = nx.to_dict_of_lists(G);

    print(G);
    hist = [];
    path_found, path = DFS(G, 0, 5, hist);
    for hist_i in hist:
        print(hist_i)


    print(path);
