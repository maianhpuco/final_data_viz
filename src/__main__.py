import streamlit as st
import streamlit.components.v1 as components
from sort_animation import animate_sort;
import numpy as np
from sort import generate_result


st.set_page_config(layout="wide");

if __name__ == "__main__":
    st.title("Final: Data Visualization");

    tab1, tab2, tab3 = st.tabs(["Sorting", "Others", "Member"])
    
    with tab1:
        lcol, rcol = st.columns(2);

        with lcol:
            # Number of element
            n_elem = st.slider("Number of element", 
                    min_value = 5,
                    max_value = 50,
                    step = 1)

            # Inital value
            init_val = np.random.randint(0, n_elem, n_elem);
            init_val = init_val.tolist();
            init_val = [str(x) for x in init_val]
            init_val = " ".join(init_val);
            arr = st.text_area("Input array to be sort", value=init_val);
            arr = [float(num) for num in arr.strip().split(" ")];

            algo = st.selectbox("Sorting algorithm", 
                    ("QUICK_SORT", "BUBBLE_SORT"));
        
        seq = generate_result(arr, algo);
        anim = animate_sort(len(seq[0]), seq);



        with rcol:
            components.html(anim.to_jshtml(), height=1000)

    
    with tab3:
        st.markdown("""## Group 7
**Member**:
- Mai Anh Vu
- Thien Pham
- Tu T. Do""");





