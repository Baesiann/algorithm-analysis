import time # track execution time
import random
import tracemalloc # track memory usage

# partition function
def partition(arr, low, high, metrics):
    #global comparisons

    # choose the pivot
    pivot = arr[high]

    # index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        metrics["comparisons"] += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j, metrics)

    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high, metrics)
    return i + 1

# swap function
def swap(arr, i, j, metrics):
    #global swaps
    arr[i], arr[j] = arr[j], arr[i]
    metrics["swaps"] += 1

# the QuickSort function implementation
def quickSort(arr, low, high, metrics):
    #global recursive_calls
    metrics["recursive_calls"] += 1

    if low < high:

        # pi is the partition return index of pivot
        pi = partition(arr, low, high, metrics)

        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1, metrics)
        quickSort(arr, pi + 1, high, metrics)


# Metrics wrapper
def quickSort_tracked(arr):
    metrics = {
        "unsorted_list": arr.copy(),
        "sorted_list": [],
        "sizes": len(arr),
        "comparisons": 0,
        "swaps": 0,
        "recursive_calls": 0,
        "execution_time": 0,
        "current_memory": 0,
        "peak_memory": 0
    }

    tracemalloc.start() # Start mem-use tracker
    start_time = time.perf_counter() # Start exec timer

    # Sort the array
    quickSort(arr, 0, len(arr) - 1, metrics)

    # Store the sorted list
    metrics["sorted_list"] = arr.copy()

    # End and track exec timer
    end_time = time.perf_counter()
    metrics["execution_time"] = end_time - start_time

    # End and track memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop() # End mem-use tracker
    metrics["current_memory"] = current / 1024
    metrics["peak_memory"] = peak / 1024

    return arr, metrics


if __name__ == "__main__":

    # arr = [42, 7, 18, 93, 2, 56, 11, 74, 29, 5] # Random list
    # arr = [1, 2, 3, 4, 6, 5, 7, 8, 10, 9] # Nearly sorted list
    # arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Reverse sorted list
    # arr = [5, 5, 5, 3, 3, 7, 7, 5, 3, 7] # Heavy duplicate list

    # Large dataset
    size = 15000
    arr = [random.randint(0, 15000) for _ in range(size)]

    n = len(arr)
    #print("Unsorted: ", arr)

    tracemalloc.start() # Start mem-use tracker
    start_time = time.perf_counter() # Start exec timer
    metrics = quickSort_tracked(arr)
    end_time = time.perf_counter() # End exec timer
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop() # End mem-use tracker

    # Print statistics
    #print("Sorted: ", arr)
    print(f"Comparisons: ", metrics["comparisons"])
    print(f"Swaps: ", metrics["swaps"])
    print(f"Recursive calls: ", metrics["recursive_calls"])
    print(f"Execution time: {metrics["execution_time"]:.8f} seconds")
    print(f"Current memory usage: {metrics["current_memory"]:.2f} KB")
    print(f"Peak memory usage: {metrics["peak_memory"]:.2f} KB")