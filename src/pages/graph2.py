import streamlit as st;
import numpy as np;
from sort_animation import animate_sort_v2
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from graph import *

st.set_page_config(
        page_title = "Graph",
        layout="wide");
st.title("Visualize graph algorithms")
st.sidebar.markdown("Graph (DFS/BFS)");


lcol, rcol = st.columns([1,2]);

G = None;
# Graph config
with lcol:
    n_nodes = st.number_input("Node", 
            min_value = 20,
            max_value = 50,
            step = 1)

    p = st.slider("Graph density",
            min_value = .25,
            max_value = 1.00,
            step = 0.01)
    
    algo = st.selectbox("Searching Algorithm", 
                                     ["breadth-first-search",
                                      "depth-first-search",
                                      "astar", 
                                      "greedy-best-first-search"])

    G = generate_random_graph(n_nodes, p); 
    G_lists = nx.to_dict_of_lists(G);

    st.markdown(f"""```json
    {G_lsts}```""")
    
    if G is not None:

        # start & end node
        start = st.selectbox("Start",
                [str(node) for node in G.nodes()]);
        
        end = st.selectbox("End",
                index = n_nodes - 1,
                options = [str(node) for node in G.nodes()]);
    
with rcol:
    if G is not None:
        from graph.animation import animation_search_algo;
        algo_map = {
                "breadth-first-search": "bfs", 
                "depth-first-search": "dfs", 
                "astar": "astar",
                "greedy-best-first-search": "gbfs"
                }
        algo_name = algo_map.get(algo)
        anim = animation_search_algo(G, int(start), int(end),algo_name);
        components.html(anim.to_jshtml(), height=600)

