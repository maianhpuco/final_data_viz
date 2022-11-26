def result_append(result, arr):
  result.append(arr.copy())
def arr_swap(result, arr, i, j):
  (arr[i], arr[j]) = (arr[j], arr[i])
  result_append(result, arr)

def bb_sort(result, arr, n):
  for i in range(n):
      for j in range(i + 1, n):
        if arr[i] > arr[j]:
          arr_swap(result, arr, i, j)

def qs_partition(result, arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      arr_swap(result, arr, i, j)
  arr_swap(result, arr, i+1, high)
  return i + 1
 
def qs_sort(result, arr, low, high):
  if low < high:
    pi = qs_partition(result, arr, low, high)
    qs_sort(result, arr, low, pi - 1)
    qs_sort(result, arr, pi + 1, high)

def generate_result(arr, sort_engine="BUBBLE_SORT"):
  result = [arr]
  if sort_engine == "BUBBLE_SORT":
    n = len(arr)
    bb_sort(result, arr, n)
  elif sort_engine == "QUICK_SORT":
    low, high = 0, len(arr) - 1
    qs_sort(result, arr, low, high)
  return result
