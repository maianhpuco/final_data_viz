import streamlit as st;
import numpy as np;
from sort_animation import animate_sort_v2
import streamlit.components.v1 as components

st.set_page_config(
        page_title = "Sorting",
        layout="wide");
st.title("Visualize sorting algorithms")
st.sidebar.markdown("Sorting");


lcol, rcol = st.columns(2);
arr = None;

with lcol:
    n_elem = st.number_input("Number of element", 
            min_value = 10,
            max_value = 100,
            step = 1)

    algo = st.selectbox("Algorithm",
            ("BUBBLE SORT", "QUICK SORT"));

    if n_elem:
        # Generate random array with n elements
        arr = np.random.randint(1, 100, n_elem);
        arr_str = " ".join([str(x) for x in arr]);
        st.markdown(f"Array to be sorted `{arr_str}`");

    
with rcol:
    if arr is not None:
        if algo == "BUBBLE SORT":
            from sort_v2 import bbsort;
            seq = bbsort(arr);
            anim = animate_sort_v2(seq);
        
            components.html(anim.to_jshtml(), height=600)
        
        if algo == "QUICK SORT":
            from sort_v2 import quick_sort;
            seq = [];
            quick_sort(seq, arr, 0, n_elem - 1);
            anim = animate_sort_v2(seq);
        
            components.html(anim.to_jshtml(), height=600)

