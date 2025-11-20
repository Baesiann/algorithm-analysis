import time # track exec time
import random
import tracemalloc

# To heapify a subtree rooted with node i
def heapify(arr, n, i, metrics):
    # count the call
    metrics["recursive_calls"] += 1

    # Initialize largest as root
    largest = i

    # left index = 2*i + 1
    l = 2 * i + 1

    # right index = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n:
        metrics["comparisons"] += 1
        if arr[l] > arr[largest]:
            largest = l

    # If right child is larger than largest so far
    if r < n:
        metrics["comparisons"] += 1
        if arr[r] > arr[largest]:
            largest = r

    # If largest is not root (swap and recurse)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        metrics["swaps"] += 1

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest, metrics)

# Main function to do heap sort
def heapSort(arr):
    metrics = {
        "comparisons": 0,
        "swaps": 0,
        "recursive_calls": 0,
        "execution_time": 0,
        "current_memory": 0,
        "peak_memory": 0
    }

    # Start the timer
    start_time = time.perf_counter()
    tracemalloc.start() # Start mem-use tracker
    n = len(arr)

    # Build heap (rearrange vector)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, metrics)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):

        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # Count it as a swap
        metrics["swaps"] += 1

        # Call max heapify on the reduced heap
        heapify(arr, i, 0, metrics)

    # End the timer
    end_time = time.perf_counter()
    metrics["execution_time"] = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop() # End mem-use tracker
    metrics["current_memory"] = current / 1024
    metrics["peak_memory"] = peak / 1024

    return metrics