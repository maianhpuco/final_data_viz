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


lcol, rcol = st.columns(2);
arr = None;

with rcol:
    st.markdown('Zachary´s Karate Club Graph')
    G = generate_random_graph(25, .25); 
    fig, ax = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G,pos, with_labels=True)
    st.pyplot(fig)
