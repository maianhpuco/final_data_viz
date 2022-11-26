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
