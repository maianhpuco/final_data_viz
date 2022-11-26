from typing import List
import numpy as np;

def bbsort(arr:List[int]):
    seq = [(arr, (-1, -1))];

    # number of elems
    N = len(arr);

    for i in range(N):
        for j in range(0, N - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j];
                seq.append((arr.copy(), (j, j+1)));

    return seq;

