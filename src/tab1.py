import streamlit as st
import streamlit.components.v1 as components
from sort_animation import animate_sort, animate_sort_v2
import numpy as np

def tab01():
    left, middle, right = st.columns(3);

    with left:
        n_elem = st.number_input(
                "Number of elememets to sort",
                min_value = 5,
                max_value = 50);

        if st.button("Generate Array"):
            arr = np.random.randint(1, n_elem + 1, n_elem);

            # Convert arr to text to display
            arr_txt = arr.tolist();
            arr_txt = [str(x) for x in arr_txt]
            arr_txt = " ".join(arr_txt);

            st.markdown(f"```{arr_txt}```");

            # Choosing algorithm to sort
            algo = st.selectbox("Sorting algorithm", 
                    ("BUBBLE_SORT", "QUICK_SORT"));
            
            sort_btn = st.button("Sort");

            if sort_btn:
                if algo == "BUBBLE_SORT":
                    from sort_v2 import bbsort;
                    seq = bbsort(arr);
                    anim = animate_sort_v2(seq);

            
            with middle:
                if sort_btn:
                    components.html(anim.to_jshtml(), height=1000)



