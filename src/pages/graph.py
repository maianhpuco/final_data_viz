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

path = None;

# Graph config
with lcol:
    G = generate_random_graph(50, .25); 
    G_lists = nx.to_dict_of_lists(G);
    
    # Run DFS
    hist = [];
    path_found, path = DFS(G, 1, 24, hist);

    # Plotting shit
    fig, ax = draw_graph(G)

    st.pyplot(fig)

with rcol:
    if path is not None:
        st.markdown(path);
