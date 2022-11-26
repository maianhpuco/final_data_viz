import numpy as np
from matplotlib.animation import FuncAnimation 
from matplotlib import pyplot as plt

def animate_sort(n_elem:int, seq):
    """
    Animating sorting algorithms

    Args:
        - n_elem: length of the array to be sorted

    """

    fig, ax = plt.subplots();

    X = range(n_elem);
    bar = ax.bar(X, seq[1]);

    def init():
        # heights = np.random.uniform(0, 1, 10);
        heights = seq[1];
        for rect, height in zip(bar, heights):
            rect.set_height(height);

    def animate(i):
        # bar.set_data(range(10), np.random.uniform(0, 1, 10));
        # heights = np.random.uniform(0, 1, 10);
        heights = seq[i];

        for rect, height in zip(bar, heights):
            rect.set_height(height);

    anim = FuncAnimation(fig, animate, init_func = init,
            frames = len(seq), interval = 50,)

    # components.html(anim.to_jshtml(), height=1000)
    return anim;

def animate_sort_v2(seq):
    """
    Animating sorting algorithms


    Args:
        - n_elem: length of the array to be sorted
        - seq   : list of the state of the array sorted
          (arr, (i, j)): i, j in the index of the previous exchanged elem

    """

    fig, ax = plt.subplots();
    ax.axis("off");
    fig.tight_layout();

    # Initial state
    arr, _  = seq[0];
    n_elem = len(arr);

    # x-axis
    X = range(n_elem);

    # color
    colors = ["gray"] * n_elem;
    bar     = ax.bar(X, arr, color=colors);

    def init():
        for rect, height in zip(bar, arr):
            rect.set_height(height);

    def animate(i):
        # bar.set_data(range(10), np.random.uniform(0, 1, 10));
        # heights = np.random.uniform(0, 1, 10);

        arr, (i, j) = seq[i+1];

        colors = ["gray"] * n_elem;
        
        for idx in range(n_elem):
            if idx == i or idx == j:
                colors[idx] = "blue"

        for rect, height, color in zip(bar, arr, colors):
            rect.set_height(height);
            rect.set_color(color);

    anim = FuncAnimation(fig, animate, init_func = init,
            frames = len(seq)-1, interval = 100,)

    # components.html(anim.to_jshtml(), height=1000)
    return anim;
