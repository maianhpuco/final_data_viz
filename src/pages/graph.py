import streamlit as st;
import numpy as np;
from sort_animation import animate_sort_v2
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from graph import *
from graph_animation import draw_graph

st.set_page_config(
        page_title = "Graph",
        layout="wide");
st.title("Visualize graph algorithms")
st.sidebar.markdown("Graph (DFS/BFS)");


lcol, rcol = st.columns(2);

G = None;
# Graph config
with lcol:
    n_nodes = st.number_input("Node", 
            min_value = 10,
            max_value = 100,
            step = 1)

    p = st.slider("Graph density",
            min_value = .25,
            max_value = 1.00,
            step = 0.01)

    G = generate_random_graph(n_nodes, p); 
    G_lists = nx.to_dict_of_lists(G);
    st.markdown(f"""```json
    {G_lists}```""")
    

with rcol:
    if G is not None:
        from graph_animation import animate_search;
        anim = animate_search(G, 0, n_nodes);
        components.html(anim.to_jshtml(), height=600)
