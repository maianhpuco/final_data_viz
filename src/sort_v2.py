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



# Function to find the partition position
def partition(seq, array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            seq.append((array.copy(), (i, j)));

    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    seq.append((array.copy(), (i+1, high)));

    # Return the position from where partition is done
    return i + 1

def quick_sort(seq, array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(seq, array, low, high)

        # Recursive call on the left of pivot
        quick_sort(seq, array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(seq, array, pi + 1, high)
