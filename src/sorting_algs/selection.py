import time
import random

# -----------------------------
#   SELECTION SORT FUNCTION
# -----------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the smallest element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap into correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# -----------------------------
#   TESTING FUNCTION
# -----------------------------
def test_selection_sort(size, data_type):
    # Generate different types of input
    if data_type == "sorted":
        arr = list(range(size))
    elif data_type == "reverse":
        arr = list(range(size, 0, -1))
    elif data_type == "random":
        arr = [random.randint(0, size) for _ in range(size)]
    else:
        raise ValueError("Choose: 'sorted', 'reverse', or 'random'")

    start = time.time()       # start timer
    selection_sort(arr)       # run sorting
    end = time.time()         # end timer

    return round(end - start, 6)

# -----------------------------
#   EXAMPLE USAGE
# -----------------------------
print("Testing Selection Sort on 5000 elements:")
print("Best case (sorted):     ", test_selection_sort(5000, "sorted"),  "seconds")
print("Worst case (reverse):   ", test_selection_sort(5000, "reverse"), "seconds")
print("Average case (random):  ", test_selection_sort(5000, "random"),  "seconds")
